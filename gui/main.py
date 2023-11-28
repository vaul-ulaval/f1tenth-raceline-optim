from MainWindow import MainWindow

from PySide6.QtWidgets import QApplication
import sys
import PySide6

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
