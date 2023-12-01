import sys
import os
import csv
import yaml

from ui_mainwindow import Ui_MainWindow

from GenerateCenterlineTab import GenerateCenterlineTab
from CompareTab import CompareTab
from Workspace import Workspace

from PySide6.QtWidgets import QMainWindow, QPushButton, QFileDialog, QGraphicsScene, QGraphicsPixmapItem, QVBoxLayout
from PySide6.QtGui import QImage, QPixmap



class MainWindow(QMainWindow):
    _compare_tab : CompareTab
    _centerline_tab = None
    _workspace : Workspace

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.loadWorkspace.clicked.connect(self.load_workspace)

        self.connect_tabs()

        self.show()

    def load_workspace(self):
        path = QFileDialog.getExistingDirectory(self, 'Open file', '../racetracks', QFileDialog.ShowDirsOnly)
        self._workspace = Workspace(path)
        self._compare_tab.setWorkspace(self._workspace)
        self._centerline_tab.setWorkspace(self._workspace)
    
    def connect_tabs(self):
        self._compare_tab = CompareTab()
        compare_tab_layout = QVBoxLayout()
        compare_tab_layout.addWidget(self._compare_tab)
        self.ui.Compare.setLayout(compare_tab_layout)

        self._centerline_tab = GenerateCenterlineTab()
        generate_centerline_tab_layout = QVBoxLayout()
        generate_centerline_tab_layout.addWidget(self._centerline_tab)
        self.ui.Centerline.setLayout(generate_centerline_tab_layout)
    