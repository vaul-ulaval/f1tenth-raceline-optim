import sys
from ui_comparetab import Ui_CompareTab

from PySide6.QtWidgets import QDialog, QGraphicsScene, QGraphicsPixmapItem, QApplication, QListWidgetItem
from PySide6.QtGui import QPixmap, QColor, QImage
from PySide6.QtCore import Qt
import matplotlib.pyplot as plt

from workspace import Workspace
import numpy as np
from PIL import Image


class CompareTab(QDialog):
    _workspace : Workspace

    def __init__(self):
        super(CompareTab, self).__init__()
        self.ui = Ui_CompareTab()
        self.ui.setupUi(self)
        self.ui.listWidget.itemClicked.connect(self.item_clicked)

    
    def set_workspace(self, workspace):
        self.ui.listWidget.clear()
        self._workspace = workspace
        
        for raceline in self._workspace.get_racelines():
            item = QListWidgetItem()
            item.setText(raceline.name)

            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            item.setForeground(QColor(raceline.color))

            self.ui.listWidget.addItem(item)

    def item_clicked(self):
        item_names = []
        for index in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(index)
            if (item.checkState() == Qt.Checked):
                item_names.append(item.text())
        
        self.draw_racelines(item_names)
    
    def draw_racelines(self, raceline_names):
        racelines = list(filter(lambda x: x.name in raceline_names, self._workspace.get_racelines()))
        if len(racelines) == 0: return

        map = self._workspace.get_map(racelines[0].map_name)

        raw_map_img = np.array(Image.open(map.image_path).transpose(Image.FLIP_TOP_BOTTOM))
        raw_map_img = raw_map_img.astype(np.float64)
        

        centerline_name = map.name.replace(".yaml", ".csv")
        centerline = self._workspace.get_centerline(centerline_name)


        racelines_xs = []
        racelines_ys = []
        racelines_colors = []
        for raceline in racelines:
            xs, ys = self.scale_points(raceline.xs, raceline.ys, map.origin, map.resolution)
            racelines_xs.append(xs)
            racelines_ys.append(ys)
            
            racelines_colors.append(raceline.color)

        fig = plt.figure(figsize=(10, 10))
        plt.imshow(raw_map_img, cmap="gray", origin="lower")

        
        centerlineXsScaled, centerlineYsScaled = self.scale_points(centerline.xs, centerline.ys, map.origin, map.resolution)
        plt.plot(centerlineXsScaled, centerlineYsScaled, color="red")

        for i in range(len(racelines_xs)):
            plt.plot(racelines_xs[i], racelines_ys[i], color=racelines_colors[i])
    
        fig.canvas.draw()
        image = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)

        img = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

        img = QImage(img, img.shape[1], img.shape[0], QImage.Format_RGB888)

        self.draw_image(img)


    def scale_points(self, xs, ys, origin, map_resolution):
        scaled_xs = []
        scaled_ys = []
        for i in range(len(xs)):
            x = xs[i]
            y = ys[i]
            x, y = self.scale_point(x, y, origin, map_resolution)
            scaled_xs.append(x)
            scaled_ys.append(y)
        return scaled_xs, scaled_ys
        

    def scale_point(self, x, y, origin, map_resolution):
        orig_x = origin[0]
        orig_y = origin[1]
        x -= orig_x
        y -= orig_y

        x /= map_resolution
        y /= map_resolution
        return x, y

    def draw_image(self, img):
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        pic = QGraphicsPixmapItem()
        pic.setPixmap(QPixmap.fromImage(img))
        self.scene.addItem(pic)