import sys
import os
import csv
import yaml

from ui_mainwindow import Ui_MainWindow
from CompareTab import CompareTab
from Workspace import Workspace

from PySide6.QtWidgets import QMainWindow, QPushButton, QFileDialog, QGraphicsScene, QGraphicsPixmapItem, QVBoxLayout
from PySide6.QtGui import QImage, QPixmap

from gen_centerline import gen_centerline, display_centerline


class MainWindow(QMainWindow):
    _compare_tab = None
    _centerline_tab = None
    _workspace = None

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._workspace = Workspace()
        self._workspace.loadRacelines()

        _compare_tab = CompareTab(self._workspace)
        compare_tab_layout = QVBoxLayout()
        compare_tab_layout.addWidget(_compare_tab)
        self.ui.Compare.setLayout(compare_tab_layout)



        
        self.ui.loadMapButton.clicked.connect(self.load_map)

        self.scene = QGraphicsScene()
        self.ui.centerLineView.setScene(self.scene)
        
        self.ui.thresholdSlider.valueChanged.connect(
            lambda: self.ui.thresholdValue.setText(str(self.ui.thresholdSlider.value()/100))
        )

        self.ui.genCenterlineButton.setEnabled(False)
        self.ui.genCenterlineButton.clicked.connect(self.generate_centerline)

        self.ui.SaveCenterLineButton.setEnabled(False)
        self.ui.SaveCenterLineButton.clicked.connect(self.save_centerline)

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
        self.ui.genCenterlineButton.setEnabled(True)

    def generate_centerline(self):
        waypoints, track_widths, self.transformed_data = gen_centerline(
            self.map_img_path,
            self.map_resolution,
            self.origin,
            float(self.ui.thresholdValue.text()),
            self.ui.reverseCheckBox.isChecked()
        )
        img = display_centerline(self.map_img_path, waypoints)
        img = QImage(img, img.shape[1], img.shape[0], QImage.Format_RGB888)

        self.draw_image(img)
        self.ui.SaveCenterLineButton.setEnabled(True)

    def save_centerline(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save file', '/racetracks/centerlines', "CSV files (*.csv)")
        header = ['x_m', 'y_m', 'w_tr_right_m', 'w_tr_left_m']

        with open(f"{str(file_name)}.csv", 'w', newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(header)
            for row in self.transformed_data:
                round_row = [round(elem, 3) for elem in row]
                csv_writer.writerow(round_row)

    def draw_image(self, img):
        self.scene = QGraphicsScene()
        self.ui.centerLineView.setScene(self.scene)
        pic = QGraphicsPixmapItem()
        pic.setPixmap(QPixmap.fromImage(img))
        self.scene.addItem(pic)


    def find_center_point(self):
        pass

