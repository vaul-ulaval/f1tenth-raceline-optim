import sys
from ui_generatecenterlinetab import Ui_GenerateCenterlineTab

from PySide6.QtWidgets import QDialog, QGraphicsScene, QGraphicsPixmapItem, QApplication, QListWidgetItem
from PySide6.QtGui import QPixmap, QColor, QImage
from PySide6.QtCore import Qt

from Workspace import Workspace

from objects import Map, Centerline

from gen_centerline import gen_centerline, display_centerline

class GenerateCenterlineTab(QDialog):
    _workspace : Workspace
    _selected_map : Map

    def __init__(self):
        super(GenerateCenterlineTab, self).__init__()
        self.ui = Ui_GenerateCenterlineTab()
        self.ui.setupUi(self)

        # self.ui.loadMapButton.clicked.connect(self.load_map)

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

        # self.ui.SaveCenterLineButton.setEnabled(False)
        # self.ui.SaveCenterLineButton.clicked.connect(self.save_centerline)

    
    def setWorkspace(self, workspace : Workspace):
        self._workspace = workspace
        self.ui.map_cb.clear()
        for map in self._workspace.getMaps():
            self.ui.map_cb.addItem(map.name)
    
    def map_selected(self):
        map_name = self.ui.map_cb.currentText()
        self._selected_map = self._workspace.getMap(map_name)
        self.ui.thresholdSlider.setEnabled(True)
        self.ui.reverseCheckBox.setEnabled(True)
        img = QImage(self._selected_map.imagePath)
        img.scaledToWidth(self.ui.centerLineView.width())
        img.scaledToHeight(self.ui.centerLineView.height())
        self.draw_image(img)
        

        
    # def load_map(self):
    #     map_yaml_path, _ = QFileDialog.getOpenFileName(self, 'Open file', '../racetracks/maps', "Image files (*.yaml)")
    #     base_path = os.path.split(map_yaml_path)[0]
    #     with open(map_yaml_path, 'r') as yaml_stream:
    #         map_metadata = yaml.safe_load(yaml_stream)
    #         self.map_resolution = map_metadata['resolution']
    #         self.origin = map_metadata['origin']
    #         self.map_img_path = os.path.join(base_path, map_metadata['image'])

    #     self.ui.genCenterlineButton.setEnabled(True)

    def generate_centerline(self):
        waypoints, track_widths, transformed_data = gen_centerline(
            self._selected_map.imagePath,
            self._selected_map.resolution,
            self._selected_map.origin,
            float(self.ui.thresholdValue.text()),
            self.ui.reverseCheckBox.isChecked()
        )

        name = self._selected_map.name.split(".yaml")[0]

        self._workspace.saveCenterline(name, transformed_data)

        img = display_centerline(self._selected_map.imagePath, waypoints)
        img = QImage(img, img.shape[1], img.shape[0], QImage.Format_RGB888)

        self.draw_image(img)


    def draw_image(self, img):
        self.scene = QGraphicsScene()
        self.ui.centerLineView.setScene(self.scene)
        pic = QGraphicsPixmapItem()
        pic.setPixmap(QPixmap.fromImage(img))
        self.scene.addItem(pic)