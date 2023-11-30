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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGraphicsView, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 642)
        self.actionLoadMap = QAction(MainWindow)
        self.actionLoadMap.setObjectName(u"actionLoadMap")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Tabs = QTabWidget(self.centralwidget)
        self.Tabs.setObjectName(u"Tabs")
        self.Centerline = QWidget()
        self.Centerline.setObjectName(u"Centerline")
        self.verticalLayout_3 = QVBoxLayout(self.Centerline)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.loadMapButton = QPushButton(self.Centerline)
        self.loadMapButton.setObjectName(u"loadMapButton")
        self.loadMapButton.setToolTipDuration(-1)

        self.horizontalLayout.addWidget(self.loadMapButton)

        self.SaveCenterLineButton = QPushButton(self.Centerline)
        self.SaveCenterLineButton.setObjectName(u"SaveCenterLineButton")

        self.horizontalLayout.addWidget(self.SaveCenterLineButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.centerLineView = QGraphicsView(self.Centerline)
        self.centerLineView.setObjectName(u"centerLineView")

        self.horizontalLayout_3.addWidget(self.centerLineView)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.reverseCheckBox = QCheckBox(self.Centerline)
        self.reverseCheckBox.setObjectName(u"reverseCheckBox")
        self.reverseCheckBox.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.reverseCheckBox)

        self.thresholdLabel = QLabel(self.Centerline)
        self.thresholdLabel.setObjectName(u"thresholdLabel")

        self.verticalLayout_2.addWidget(self.thresholdLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.thresholdSlider = QSlider(self.Centerline)
        self.thresholdSlider.setObjectName(u"thresholdSlider")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thresholdSlider.sizePolicy().hasHeightForWidth())
        self.thresholdSlider.setSizePolicy(sizePolicy)
        self.thresholdSlider.setMinimum(0)
        self.thresholdSlider.setMaximum(100)
        self.thresholdSlider.setSingleStep(1)
        self.thresholdSlider.setPageStep(10)
        self.thresholdSlider.setValue(50)
        self.thresholdSlider.setSliderPosition(50)
        self.thresholdSlider.setTracking(True)
        self.thresholdSlider.setOrientation(Qt.Horizontal)
        self.thresholdSlider.setTickPosition(QSlider.TicksBothSides)
        self.thresholdSlider.setTickInterval(10)

        self.horizontalLayout_2.addWidget(self.thresholdSlider)

        self.thresholdValue = QLabel(self.Centerline)
        self.thresholdValue.setObjectName(u"thresholdValue")
        self.thresholdValue.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.thresholdValue)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.genCenterlineButton = QPushButton(self.Centerline)
        self.genCenterlineButton.setObjectName(u"genCenterlineButton")

        self.verticalLayout_2.addWidget(self.genCenterlineButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

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
        self.menubar.setGeometry(QRect(0, 0, 1024, 22))
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
#if QT_CONFIG(tooltip)
        self.loadMapButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.loadMapButton.setText(QCoreApplication.translate("MainWindow", u"Load map...", None))
        self.SaveCenterLineButton.setText(QCoreApplication.translate("MainWindow", u"Save centerline ...", None))
        self.reverseCheckBox.setText(QCoreApplication.translate("MainWindow", u"Reverse", None))
        self.thresholdLabel.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.thresholdValue.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.genCenterlineButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.Centerline), QCoreApplication.translate("MainWindow", u"Centerline", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.Raceline), QCoreApplication.translate("MainWindow", u"Raceline", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.Compare), QCoreApplication.translate("MainWindow", u"Compare", None))
        self.menuHello.setTitle(QCoreApplication.translate("MainWindow", u"Hello", None))
    # retranslateUi

