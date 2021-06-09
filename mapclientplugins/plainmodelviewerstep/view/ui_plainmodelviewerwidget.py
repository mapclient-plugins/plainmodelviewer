# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plainmodelviewerwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from opencmiss.zincwidgets.sceneviewerwidget import SceneviewerWidget


class Ui_PlainModelViewerWidget(object):
    def setupUi(self, PlainModelViewerWidget):
        if not PlainModelViewerWidget.objectName():
            PlainModelViewerWidget.setObjectName(u"PlainModelViewerWidget")
        PlainModelViewerWidget.resize(626, 505)
        self.horizontalLayout = QHBoxLayout(PlainModelViewerWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolBox = QToolBox(PlainModelViewerWidget)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.pageView = QWidget()
        self.pageView.setObjectName(u"pageView")
        self.pageView.setGeometry(QRect(0, 0, 118, 450))
        self.verticalLayout = QVBoxLayout(self.pageView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonDone = QPushButton(self.pageView)
        self.pushButtonDone.setObjectName(u"pushButtonDone")

        self.horizontalLayout_2.addWidget(self.pushButtonDone)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 381, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.pageView, u"View")

        self.horizontalLayout.addWidget(self.toolBox)

        self.widgetZinc = SceneviewerWidget(PlainModelViewerWidget)
        self.widgetZinc.setObjectName(u"widgetZinc")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(4)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widgetZinc.sizePolicy().hasHeightForWidth())
        self.widgetZinc.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.widgetZinc)


        self.retranslateUi(PlainModelViewerWidget)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PlainModelViewerWidget)
    # setupUi

    def retranslateUi(self, PlainModelViewerWidget):
        PlainModelViewerWidget.setWindowTitle(QCoreApplication.translate("PlainModelViewerWidget", u"Plain Model Viewer Widget", None))
        self.pushButtonDone.setText(QCoreApplication.translate("PlainModelViewerWidget", u"Done", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageView), QCoreApplication.translate("PlainModelViewerWidget", u"View", None))
    # retranslateUi

