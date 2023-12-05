# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GenerateCenterlineTab.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGraphicsView,
    QHBoxLayout, QLabel, QSizePolicy, QSlider,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_GenerateCenterlineTab(object):
    def setupUi(self, GenerateCenterlineTab):
        if not GenerateCenterlineTab.objectName():
            GenerateCenterlineTab.setObjectName(u"GenerateCenterlineTab")
        GenerateCenterlineTab.resize(666, 386)
        self.verticalLayout = QVBoxLayout(GenerateCenterlineTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(GenerateCenterlineTab)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.map_cb = QComboBox(GenerateCenterlineTab)
        self.map_cb.setObjectName(u"map_cb")
        self.map_cb.setMinimumSize(QSize(400, 0))

        self.horizontalLayout.addWidget(self.map_cb)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.centerLineView = QGraphicsView(GenerateCenterlineTab)
        self.centerLineView.setObjectName(u"centerLineView")

        self.horizontalLayout_3.addWidget(self.centerLineView)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.reverseCheckBox = QCheckBox(GenerateCenterlineTab)
        self.reverseCheckBox.setObjectName(u"reverseCheckBox")
        self.reverseCheckBox.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.reverseCheckBox)

        self.thresholdLabel = QLabel(GenerateCenterlineTab)
        self.thresholdLabel.setObjectName(u"thresholdLabel")
        self.thresholdLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.thresholdLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.thresholdSlider = QSlider(GenerateCenterlineTab)
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

        self.thresholdValue = QLabel(GenerateCenterlineTab)
        self.thresholdValue.setObjectName(u"thresholdValue")
        self.thresholdValue.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.thresholdValue)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(GenerateCenterlineTab)

        QMetaObject.connectSlotsByName(GenerateCenterlineTab)
    # setupUi

    def retranslateUi(self, GenerateCenterlineTab):
        GenerateCenterlineTab.setWindowTitle(QCoreApplication.translate("GenerateCenterlineTab", u"Form", None))
        self.label.setText(QCoreApplication.translate("GenerateCenterlineTab", u"Select map:", None))
        self.reverseCheckBox.setText(QCoreApplication.translate("GenerateCenterlineTab", u"Reverse", None))
        self.thresholdLabel.setText(QCoreApplication.translate("GenerateCenterlineTab", u"Threshold", None))
        self.thresholdValue.setText(QCoreApplication.translate("GenerateCenterlineTab", u"0.5", None))
    # retranslateUi

