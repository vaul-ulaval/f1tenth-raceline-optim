import sys
import os
import csv
import yaml

from ui_mainwindow import Ui_MainWindow

from PySide6.QtWidgets import QMainWindow, QPushButton, QFileDialog, QGraphicsScene, QGraphicsPixmapItem, QGraphicsView
from PySide6.QtGui import QImage, QPixmap

from gen_centerline import gen_centerline, display_centerline


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        # self.form_widget = QCheckBox(self)
        # print(self)
        # self.tabs.compare.setCentralWidget(self.form_widget)


        
        self.ui.loadMapButton.clicked.connect(self.load_map)

        self.scene = QGraphicsScene()
        self.ui.centerLineView.setScene(self.scene)
        

        self.ui.genCenterlineButton.clicked.connect(self.generate_centerline)

        self.centerLineView = self.findChild(QGraphicsView, 'centerLineView')

        self.thresholdSlider = self.findChild(QSlider, 'thresholdSlider')
        self.thresholdValue = self.findChild(QLabel, 'thresholdValue')
        self.thresholdSlider.valueChanged.connect(
            lambda: self.thresholdValue.setText(str(self.thresholdSlider.value()/100))
        )

        self.reverseCheckBox = self.findChild(QCheckBox, 'reverseCheckBox')

        self.genCenterlineButton = self.findChild(QPushButton, 'genCenterlineButton')
        self.genCenterlineButton.setEnabled(False)
        self.genCenterlineButton.clicked.connect(self.generate_centerline)

        self.loadMapButton = self.findChild(QPushButton, 'loadMapButton')
        self.loadMapButton.clicked.connect(self.load_map)

        self.saveCenterlineButton = self.findChild(QPushButton, 'SaveCenterLineButton')
        self.saveCenterlineButton.setEnabled(False)
        self.saveCenterlineButton.clicked.connect(self.save_centerline)

        self.show()

    def load_map(self):
        map_yaml_path, _ = QFileDialog.getOpenFileName(self, 'Open file', '../racetracks/maps', "Image files (*.yaml)")
        base_path = os.path.split(map_yaml_path)[0]
        with open(map_yaml_path, 'r') as yaml_stream:
            map_metadata = yaml.safe_load(yaml_stream)
            self.map_resolution = map_metadata['resolution']
            self.origin = map_metadata['origin']
            self.map_img_path = os.path.join(base_path, map_metadata['image'])

        img = QImage(self.map_img_path)
        self.draw_image(img)
        self.genCenterlineButton.setEnabled(True)

    def generate_centerline(self):
        waypoints, track_widths, self.transformed_data = gen_centerline(
            self.map_img_path,
            self.map_resolution,
            self.origin,
            float(self.thresholdValue.text()),
            self.reverseCheckBox.isChecked()
        )
        img = display_centerline(self.map_img_path, waypoints)
        img = QImage(img, img.shape[1], img.shape[0], QImage.Format_RGB888)

        self.draw_image(img)
        self.saveCenterlineButton.setEnabled(True)

    def save_centerline(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save file', '../racetracks/centerlines', "CSV files (*.csv)")
        header = ['x_m', 'y_m', 'w_tr_right_m', 'w_tr_left_m']

        with open(f"{str(file_name)}.csv", 'w', newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(header)
            for row in self.transformed_data:
                round_row = [round(elem, 3) for elem in row]
                csv_writer.writerow(round_row)

    def draw_image(self, img):
        self.scene = QGraphicsScene()
        self.centerLineView.setScene(self.scene)
        pic = QGraphicsPixmapItem()
        pic.setPixmap(QPixmap.fromImage(img))
        self.scene.addItem(pic)


    def find_center_point(self):
        pass

