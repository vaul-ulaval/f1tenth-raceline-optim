# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGraphicsView, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QStatusBar, QTabWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(907, 670)
        self.actionLoadMap = QAction(MainWindow)
        self.actionLoadMap.setObjectName(u"actionLoadMap")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Tabs = QTabWidget(self.centralwidget)
        self.Tabs.setObjectName(u"Tabs")
        self.Tabs.setGeometry(QRect(0, 0, 911, 631))
        self.Centerline = QWidget()
        self.Centerline.setObjectName(u"Centerline")
        self.loadMapButton = QPushButton(self.Centerline)
        self.loadMapButton.setObjectName(u"loadMapButton")
        self.loadMapButton.setGeometry(QRect(60, 20, 101, 31))
        self.loadMapButton.setToolTipDuration(-1)
        self.SaveCenterLineButton = QPushButton(self.Centerline)
        self.SaveCenterLineButton.setObjectName(u"SaveCenterLineButton")
        self.SaveCenterLineButton.setGeometry(QRect(200, 20, 161, 31))
        self.thresholdSlider = QSlider(self.Centerline)
        self.thresholdSlider.setObjectName(u"thresholdSlider")
        self.thresholdSlider.setGeometry(QRect(690, 190, 160, 16))
        self.thresholdSlider.setMinimum(0)
        self.thresholdSlider.setMaximum(100)
        self.thresholdSlider.setSingleStep(10)
        self.thresholdSlider.setPageStep(10)
        self.thresholdSlider.setValue(50)
        self.thresholdSlider.setSliderPosition(50)
        self.thresholdSlider.setTracking(True)
        self.thresholdSlider.setOrientation(Qt.Horizontal)
        self.thresholdSlider.setTickPosition(QSlider.TicksBothSides)
        self.thresholdSlider.setTickInterval(10)
        self.thresholdLabel = QLabel(self.Centerline)
        self.thresholdLabel.setObjectName(u"thresholdLabel")
        self.thresholdLabel.setGeometry(QRect(740, 170, 71, 16))
        self.thresholdValue = QLabel(self.Centerline)
        self.thresholdValue.setObjectName(u"thresholdValue")
        self.thresholdValue.setGeometry(QRect(850, 190, 41, 16))
        self.thresholdValue.setAlignment(Qt.AlignCenter)
        self.reverseCheckBox = QCheckBox(self.Centerline)
        self.reverseCheckBox.setObjectName(u"reverseCheckBox")
        self.reverseCheckBox.setGeometry(QRect(730, 120, 91, 21))
        self.reverseCheckBox.setIconSize(QSize(20, 20))
        self.centerLineView = QGraphicsView(self.Centerline)
        self.centerLineView.setObjectName(u"centerLineView")
        self.centerLineView.setGeometry(QRect(10, 70, 661, 521))
        self.genCenterlineButton = QPushButton(self.Centerline)
        self.genCenterlineButton.setObjectName(u"genCenterlineButton")
        self.genCenterlineButton.setGeometry(QRect(710, 240, 121, 25))
        self.Tabs.addTab(self.Centerline, "")
        self.Raceline = QWidget()
        self.Raceline.setObjectName(u"Raceline")
        self.Tabs.addTab(self.Raceline, "")
        self.Compare = QWidget()
        self.Compare.setObjectName(u"Compare")
        self.Tabs.addTab(self.Compare, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 907, 22))
        self.menuHello = QMenu(self.menubar)
        self.menuHello.setObjectName(u"menuHello")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHello.menuAction())

        self.retranslateUi(MainWindow)
        self.thresholdSlider.valueChanged.connect(self.thresholdValue.setNum)

        self.Tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLoadMap.setText(QCoreApplication.translate("MainWindow", u"LoadMap", None))
#if QT_CONFIG(tooltip)
        self.actionLoadMap.setToolTip(QCoreApplication.translate("MainWindow", u"Click here to load a .pgm file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.loadMapButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.loadMapButton.setText(QCoreApplication.translate("MainWindow", u"Load map...", None))
        self.SaveCenterLineButton.setText(QCoreApplication.translate("MainWindow", u"Save centerline ...", None))
        self.thresholdLabel.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.thresholdValue.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.reverseCheckBox.setText(QCoreApplication.translate("MainWindow", u"Reverse", None))
        self.genCenterlineButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.Centerline), QCoreApplication.translate("MainWindow", u"Centerline", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.Raceline), QCoreApplication.translate("MainWindow", u"Raceline", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.Compare), QCoreApplication.translate("MainWindow", u"Compare", None))
        self.menuHello.setTitle(QCoreApplication.translate("MainWindow", u"Hello", None))
    # retranslateUi

