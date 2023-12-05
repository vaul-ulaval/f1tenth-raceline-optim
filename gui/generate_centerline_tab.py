from matplotlib import pyplot as plt
import numpy as np
from inputs_helper.centerline import ImageCenterline, gen_centerline_from_img, read_map_pgm
from .ui_generatecenterlinetab import Ui_GenerateCenterlineTab

from PySide6.QtWidgets import QDialog, QGraphicsScene, QGraphicsPixmapItem
from PySide6.QtGui import QPixmap, QImage

from .workspace import Workspace

from .objects import Map, Centerline

class GenerateCenterlineTab(QDialog):
    _workspace : Workspace
    _selected_map : Map

    def __init__(self):
        super(GenerateCenterlineTab, self).__init__()
        self.ui = Ui_GenerateCenterlineTab()
        self.ui.setupUi(self)

        self.scene = QGraphicsScene()
        self.ui.centerLineView.setScene(self.scene)
        
        
        self.ui.thresholdSlider.valueChanged.connect(
            lambda: self.ui.thresholdValue.setText(str(self.ui.thresholdSlider.value()/100))
        )

        self.ui.map_cb.currentIndexChanged.connect(self.map_selected)

        self.ui.thresholdSlider.setEnabled(False)
        self.ui.reverseCheckBox.setEnabled(False)

        self.ui.thresholdSlider.sliderReleased.connect(self.generate_centerline)
        self.ui.reverseCheckBox.stateChanged.connect(self.generate_centerline)
    
    def set_workspace(self, workspace : Workspace):
        self._workspace = workspace
        self.ui.map_cb.clear()
        for map in self._workspace.get_maps():
            self.ui.map_cb.addItem(map.name)
    
    def map_selected(self):
        map_name = self.ui.map_cb.currentText()
        self._selected_map = self._workspace.get_map(map_name)
        self.ui.thresholdSlider.setEnabled(True)
        self.ui.reverseCheckBox.setEnabled(True)
        img = QImage(self._selected_map.image_path)
        img.scaledToWidth(self.ui.centerLineView.width())
        img.scaledToHeight(self.ui.centerLineView.height())
        self.draw_image(img)
        
    def generate_centerline(self):
        the_img = read_map_pgm(self._selected_map.image_path)
        img_centerline = gen_centerline_from_img(
            the_img,
            float(self.ui.thresholdValue.text()),
            self.ui.reverseCheckBox.isChecked()
        )

        name = self._selected_map.name.replace(".yaml", "")
        self._workspace.save_centerline(name, img_centerline)

        img = self.draw_centerline_img(self._selected_map.image_path, img_centerline)
        img = QImage(img, img.shape[1], img.shape[0], QImage.Format_RGB888)

        self.draw_image(img)

    def draw_image(self, img):
        self.scene = QGraphicsScene()
        self.ui.centerLineView.setScene(self.scene)
        pic = QGraphicsPixmapItem()
        pic.setPixmap(QPixmap.fromImage(img))
        self.scene.addItem(pic)

    def draw_centerline_img(self, img_path: str, img_centerline: ImageCenterline):
        map_img = read_map_pgm(img_path)
        waypoints = img_centerline.waypoints

        x = list(map(lambda p: p[0], waypoints))
        y = list(map(lambda p: p[1], waypoints))

        # Display the waypoints on the map
        fig = plt.figure(figsize=(7, 3))
        plt.imshow(map_img, cmap="gray", origin="lower")
        plt.plot(x, y)
        plt.axis("off")
        plt.tight_layout()

        # Add an arrow to indicate direction
        arrow_start = waypoints[0]
        arrow_end = waypoints[10]  # You can adjust this index
        plt.arrow(arrow_start[0], arrow_start[1], arrow_end[0] - arrow_start[0], arrow_end[1] - arrow_start[1],
                head_width=5, head_length=5, fc='red', ec='red')
        
        fig.canvas.draw()
        image = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)

        return image.reshape(fig.canvas.get_width_height()[::-1] + (3,))