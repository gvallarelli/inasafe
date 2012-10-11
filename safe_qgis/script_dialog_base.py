# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'script_dialog.ui'
#
# Created: Thu Oct 11 14:12:10 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ScriptDialogBase(object):
    def setupUi(self, ScriptDialogBase):
        ScriptDialogBase.setObjectName(_fromUtf8("ScriptDialogBase"))
        ScriptDialogBase.resize(597, 365)
        self.tblScript = QtGui.QTableWidget(ScriptDialogBase)
        self.tblScript.setGeometry(QtCore.QRect(10, 10, 551, 181))
        self.tblScript.setObjectName(_fromUtf8("tblScript"))
        self.tblScript.setColumnCount(2)
        self.tblScript.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblScript.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblScript.setHorizontalHeaderItem(1, item)
        self.horizontalLayoutWidget = QtGui.QWidget(ScriptDialogBase)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(160, 250, 241, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnRunSelected = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnRunSelected.setObjectName(_fromUtf8("btnRunSelected"))
        self.horizontalLayout.addWidget(self.btnRunSelected)
        self.btnRefresh = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnRefresh.setObjectName(_fromUtf8("btnRefresh"))
        self.horizontalLayout.addWidget(self.btnRefresh)

        self.retranslateUi(ScriptDialogBase)
        QtCore.QMetaObject.connectSlotsByName(ScriptDialogBase)

    def retranslateUi(self, ScriptDialogBase):
        ScriptDialogBase.setWindowTitle(QtGui.QApplication.translate("ScriptDialogBase", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tblScript.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("ScriptDialogBase", "Script", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tblScript.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("ScriptDialogBase", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRunSelected.setText(QtGui.QApplication.translate("ScriptDialogBase", "Run Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRefresh.setText(QtGui.QApplication.translate("ScriptDialogBase", "Refresh List", None, QtGui.QApplication.UnicodeUTF8))

