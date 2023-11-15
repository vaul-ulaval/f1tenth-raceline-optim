import sys

from PyQt5 import uic
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QGraphicsView, QGraphicsScene, \
    QGraphicsPixmapItem


class UI(QMainWindow):
    centerline_file = ""

    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('MainWindow.ui', self)

        self.loadMapButton = self.findChild(QPushButton, 'loadMapButton')
        self.centerLineView = self.findChild(QGraphicsView, 'centerLineView')
        self.scene = QGraphicsScene()
        self.centerLineView.setScene(self.scene)

        self.loadMapButton.clicked.connect(self.load_file)

        self.show()


    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open file', '..', "Image files (*.pgm)")
        img = QImage(file_name)

        pic = QGraphicsPixmapItem()
        pic.setPixmap(QPixmap.fromImage(img))
        self.scene.setSceneRect(0, 0, self.centerLineView.width(), self.centerLineView.height())
        self.scene.addItem(pic)



app = QApplication(sys.argv)

window = UI()
app.exec()
