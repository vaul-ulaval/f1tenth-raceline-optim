# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CompareTab.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QListWidget,
    QListWidgetItem, QSizePolicy, QWidget)

class Ui_CompareTab(object):
    def setupUi(self, CompareTab):
        if not CompareTab.objectName():
            CompareTab.setObjectName(u"CompareTab")
        CompareTab.resize(700, 412)
        self.horizontalLayout = QHBoxLayout(CompareTab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget = QListWidget(CompareTab)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QSize(50, 0))
        self.listWidget.setBaseSize(QSize(50, 0))

        self.horizontalLayout.addWidget(self.listWidget)

        self.graphicsView = QGraphicsView(CompareTab)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.graphicsView)


        self.retranslateUi(CompareTab)

        QMetaObject.connectSlotsByName(CompareTab)
    # setupUi

    def retranslateUi(self, CompareTab):
        CompareTab.setWindowTitle(QCoreApplication.translate("CompareTab", u"Form", None))
    # retranslateUi

