import sys
import os

import yaml

from ui_mainwindow import Ui_MainWindow

from PySide6.QtWidgets import QMainWindow, QPushButton, QFileDialog, QGraphicsScene, QGraphicsPixmapItem
from PySide6.QtGui import QImage, QPixmap

from PySide6.QtCore import QFile

from gen_centerline import gen_centerline, display_centerline


class MainWindow(QMainWindow):
    centerline_file = ""

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        # self.form_widget = QCheckBox(self)
        # print(self)
        # self.tabs.compare.setCentralWidget(self.form_widget)


        
        self.ui.loadMapButton.clicked.connect(self.load_file)

        self.scene = QGraphicsScene()
        self.ui.centerLineView.setScene(self.scene)
        

        self.ui.genCenterlineButton.clicked.connect(self.generate_centerline)


        self.show()


    def load_file(self):
        map_yaml_path, _ = QFileDialog.getOpenFileName(self, 'Open file', '..', "Image files (*.yaml)")
        base_path = os.path.split(map_yaml_path)[0]
        with open(map_yaml_path, 'r') as yaml_stream:
            map_metadata = yaml.safe_load(yaml_stream)
            self.map_resolution = map_metadata['resolution']
            self.origin = map_metadata['origin']
            self.map_img_path = os.path.join(base_path, map_metadata['image'])

        img = QImage(self.map_img_path)
        pic = QGraphicsPixmapItem()
        pic.setPixmap(QPixmap.fromImage(img))
        self.scene.setSceneRect(0, 0, self.ui.centerLineView.width(), self.ui.centerLineView.height())
        self.scene.addItem(pic)

        # map_img = cv2.imread(map_img_path, cv2.IMREAD_GRAYSCALE)
        # self.map_img = np.array(map_img)

    def generate_centerline(self):
        waypoints, track_widths, transformed_data = gen_centerline(
            self.map_img_path, 
            self.map_resolution,
            self.origin,
            self.ui.thresholdSlider.value()/100,
            self.ui.reverseCheckBox.isChecked()
            )
        img = display_centerline(self.map_img_path, waypoints)

        img = QImage(img, img.shape[1], img.shape[0], QImage.Format_RGB888)
        pic = QGraphicsPixmapItem()
        pic.setPixmap(QPixmap.fromImage(img))
        self.scene.setSceneRect(0, 0, self.ui.centerLineView.width(), self.ui.centerLineView.height())
        self.scene.addItem(pic)

    def save_centerline(self):
        pass