# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(728, 389)
        self.actionLoadMap = QAction(MainWindow)
        self.actionLoadMap.setObjectName(u"actionLoadMap")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.loadWorkspace = QPushButton(self.centralwidget)
        self.loadWorkspace.setObjectName(u"loadWorkspace")

        self.horizontalLayout_4.addWidget(self.loadWorkspace)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.Tabs = QTabWidget(self.centralwidget)
        self.Tabs.setObjectName(u"Tabs")
        self.Centerline = QWidget()
        self.Centerline.setObjectName(u"Centerline")
        self.Tabs.addTab(self.Centerline, "")
        self.Raceline = QWidget()
        self.Raceline.setObjectName(u"Raceline")
        self.Tabs.addTab(self.Raceline, "")
        self.Compare = QWidget()
        self.Compare.setObjectName(u"Compare")
        self.Tabs.addTab(self.Compare, "")

        self.verticalLayout.addWidget(self.Tabs)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 728, 22))
        self.menuHello = QMenu(self.menubar)
        self.menuHello.setObjectName(u"menuHello")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHello.menuAction())

        self.retranslateUi(MainWindow)

        self.Tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLoadMap.setText(QCoreApplication.translate("MainWindow", u"LoadMap", None))
#if QT_CONFIG(tooltip)
        self.actionLoadMap.setToolTip(QCoreApplication.translate("MainWindow", u"Click here to load a .pgm file", None))
#endif // QT_CONFIG(tooltip)
        self.loadWorkspace.setText(QCoreApplication.translate("MainWindow", u"Load workspace...", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.Centerline), QCoreApplication.translate("MainWindow", u"Centerline", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.Raceline), QCoreApplication.translate("MainWindow", u"Raceline", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.Compare), QCoreApplication.translate("MainWindow", u"Compare", None))
        self.menuHello.setTitle(QCoreApplication.translate("MainWindow", u"Hello", None))
    # retranslateUi

