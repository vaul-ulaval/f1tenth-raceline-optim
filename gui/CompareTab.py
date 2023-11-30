import sys
from ui_comparetab import Ui_CompareTab

from PySide6.QtWidgets import QDialog, QGraphicsScene, QGraphicsPixmapItem, QApplication, QListWidgetItem
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtCore import Qt

from Workspace import Workspace


from gen_centerline import gen_centerline, display_centerline


class CompareTab(QDialog):
    _workspace = None

    def __init__(self, workspace : Workspace):
        super(CompareTab, self).__init__()
        self.ui = Ui_CompareTab()
        self.ui.setupUi(self)

        self._workspace = workspace
        
        for raceline in self._workspace.getRacelines():
            item = QListWidgetItem()
            item.setText(raceline.name)

            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            item.setForeground(QColor(raceline.color))
            

            self.ui.listWidget.addItem(item)

        # img = QImage(img, img.shape[1], img.shape[0], QImage.Format_RGB888)

        # self.draw_image(img)
        # self.ui.SaveCenterLineButton.setEnabled(True)

    def draw_image(self, img):
        self.scene = QGraphicsScene()
        self.ui.centerLineView.setScene(self.scene)
        pic = QGraphicsPixmapItem()
        pic.setPixmap(QPixmap.fromImage(img))
        self.scene.addItem(pic)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = CompareTab()
    mainWindow.show()
    sys.exit(app.exec())