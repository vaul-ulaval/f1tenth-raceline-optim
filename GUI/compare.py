import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

compare_ui_file = 'Compare.ui'
form_1, base_1 = uic.loadUiType(compare_ui_file)


class CompareUI(base_1, form_1):
    def __init__(self):
        super(base_1, self).__init__()
        self.setupUi(self)

        self.show()


app = QApplication(sys.argv)

window = CompareUI()
app.exec()
