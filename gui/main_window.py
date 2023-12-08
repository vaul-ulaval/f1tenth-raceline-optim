from .ui_mainwindow import Ui_MainWindow
from .generate_centerline_tab import GenerateCenterlineTab
from .compare_tab import CompareTab
from .workspace import Workspace

from PySide6.QtWidgets import QMainWindow, QFileDialog, QVBoxLayout

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
        path = QFileDialog.getExistingDirectory(self, 'Open file', './racetracks', QFileDialog.ShowDirsOnly)
        self._workspace = Workspace(path)
        self._compare_tab.set_workspace(self._workspace)
        self._centerline_tab.set_workspace(self._workspace)
    
    def connect_tabs(self):
        self._compare_tab = CompareTab()
        compare_tab_layout = QVBoxLayout()
        compare_tab_layout.addWidget(self._compare_tab)
        self.ui.Compare.setLayout(compare_tab_layout)

        self._centerline_tab = GenerateCenterlineTab()
        generate_centerline_tab_layout = QVBoxLayout()
        generate_centerline_tab_layout.addWidget(self._centerline_tab)
        self.ui.Centerline.setLayout(generate_centerline_tab_layout)
    