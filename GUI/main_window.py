import sys
import numpy as np
import yaml
import os

from gen_centerline import gen_centerline, display_centerline
from PyQt5 import uic
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QCheckBox, QSlider, QFileDialog, QGraphicsView, QGraphicsScene, \
    QGraphicsPixmapItem


class UI(QMainWindow):
    centerline_file = ""

    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('MainWindow.ui', self)

        self.loadMapButton = self.findChild(QPushButton, 'loadMapButton')
        self.loadMapButton.clicked.connect(self.load_file)

        self.centerLineView = self.findChild(QGraphicsView, 'centerLineView')
        self.scene = QGraphicsScene()
        self.centerLineView.setScene(self.scene)
        
        self.thresholdSlider = self.findChild(QSlider, 'thresholdSlider')
        self.reverseCheckBox = self.findChild(QCheckBox, 'reverseCheckBox')

        self.genCenterlineButton = self.findChild(QPushButton, 'genCenterlineButton')
        self.genCenterlineButton.clicked.connect(self.generate_centerline)

        self.saveCenterlineButton = self.findChild(QPushButton, 'SaveCenterLineButton')

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
        self.scene.setSceneRect(0, 0, self.centerLineView.width(), self.centerLineView.height())
        self.scene.addItem(pic)

        # map_img = cv2.imread(map_img_path, cv2.IMREAD_GRAYSCALE)
        # self.map_img = np.array(map_img)

    def generate_centerline(self):
        waypoints, track_widths, transformed_data = gen_centerline(
            self.map_img_path, 
            self.map_resolution,
            self.origin,
            self.thresholdSlider.value()/100,
            self.reverseCheckBox.isChecked()
            )
        img = display_centerline(self.map_img_path, waypoints)

        img = QImage(img, img.shape[1], img.shape[0], QImage.Format_RGB888)
        pic = QGraphicsPixmapItem()
        pic.setPixmap(QPixmap.fromImage(img))
        self.scene.setSceneRect(0, 0, self.centerLineView.width(), self.centerLineView.height())
        self.scene.addItem(pic)

    def save_centerline(self):
        pass

app = QApplication(sys.argv)

window = UI()
app.exec()
