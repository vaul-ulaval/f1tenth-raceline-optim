import sys
from ui_comparetab import Ui_CompareTab

from PySide6.QtWidgets import QDialog, QGraphicsScene, QGraphicsPixmapItem, QApplication, QListWidgetItem
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtCore import Qt

from Workspace import Workspace


class CompareTab(QDialog):
    _workspace : Workspace

    def __init__(self):
        super(CompareTab, self).__init__()
        self.ui = Ui_CompareTab()
        self.ui.setupUi(self)

    
    def setWorkspace(self, workspace):
        self.ui.listWidget.clear()
        self._workspace = workspace
        
        for raceline in self._workspace.getRacelines():
            item = QListWidgetItem()
            item.setText(raceline.name)

            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            item.setForeground(QColor(raceline.color))
            

            self.ui.listWidget.addItem(item)
