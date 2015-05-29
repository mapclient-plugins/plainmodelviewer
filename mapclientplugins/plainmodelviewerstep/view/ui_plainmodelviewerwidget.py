# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/plainmodelviewerwidget.ui'
#
# Created: Wed May 27 23:27:35 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_PlainModelViewerWidget(object):
    def setupUi(self, PlainModelViewerWidget):
        PlainModelViewerWidget.setObjectName("PlainModelViewerWidget")
        PlainModelViewerWidget.resize(626, 505)
        self.horizontalLayout = QtGui.QHBoxLayout(PlainModelViewerWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolBox = QtGui.QToolBox(PlainModelViewerWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setObjectName("toolBox")
        self.pageView = QtGui.QWidget()
        self.pageView.setGeometry(QtCore.QRect(0, 0, 118, 450))
        self.pageView.setObjectName("pageView")
        self.verticalLayout = QtGui.QVBoxLayout(self.pageView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonDone = QtGui.QPushButton(self.pageView)
        self.pushButtonDone.setObjectName("pushButtonDone")
        self.horizontalLayout_2.addWidget(self.pushButtonDone)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(20, 381, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.toolBox.addItem(self.pageView, "")
        self.horizontalLayout.addWidget(self.toolBox)
        self.widgetZinc = SceneviewerWidget(PlainModelViewerWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetZinc.sizePolicy().hasHeightForWidth())
        self.widgetZinc.setSizePolicy(sizePolicy)
        self.widgetZinc.setObjectName("widgetZinc")
        self.horizontalLayout.addWidget(self.widgetZinc)

        self.retranslateUi(PlainModelViewerWidget)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PlainModelViewerWidget)

    def retranslateUi(self, PlainModelViewerWidget):
        PlainModelViewerWidget.setWindowTitle(QtGui.QApplication.translate("PlainModelViewerWidget", "Plain Model Viewer Widget", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDone.setText(QtGui.QApplication.translate("PlainModelViewerWidget", "Done", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageView), QtGui.QApplication.translate("PlainModelViewerWidget", "View", None, QtGui.QApplication.UnicodeUTF8))

from opencmiss.zincwidgets.sceneviewerwidget import SceneviewerWidget
