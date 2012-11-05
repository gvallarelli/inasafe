# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'script_dialog.ui'
#
# Created: Mon Nov  5 13:12:56 2012
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
        ScriptDialogBase.resize(515, 514)
        self.tblScript = QtGui.QTableWidget(ScriptDialogBase)
        self.tblScript.setGeometry(QtCore.QRect(20, 10, 481, 181))
        self.tblScript.setAlternatingRowColors(False)
        self.tblScript.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tblScript.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblScript.setCornerButtonEnabled(False)
        self.tblScript.setObjectName(_fromUtf8("tblScript"))
        self.tblScript.setColumnCount(2)
        self.tblScript.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblScript.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblScript.setHorizontalHeaderItem(1, item)
        self.tblScript.horizontalHeader().setDefaultSectionSize(100)
        self.horizontalLayoutWidget = QtGui.QWidget(ScriptDialogBase)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 210, 241, 41))
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
        self.gboOptions = QtGui.QGroupBox(ScriptDialogBase)
        self.gboOptions.setGeometry(QtCore.QRect(10, 290, 501, 161))
        self.gboOptions.setCheckable(False)
        self.gboOptions.setObjectName(_fromUtf8("gboOptions"))
        self.verticalLayout = QtGui.QVBoxLayout(self.gboOptions)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cboNewProject = QtGui.QCheckBox(self.gboOptions)
        self.cboNewProject.setChecked(True)
        self.cboNewProject.setObjectName(_fromUtf8("cboNewProject"))
        self.verticalLayout.addWidget(self.cboNewProject)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.gboOptions)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.sboCount = QtGui.QSpinBox(self.gboOptions)
        self.sboCount.setSuffix(_fromUtf8(""))
        self.sboCount.setPrefix(_fromUtf8(""))
        self.sboCount.setMinimum(1)
        self.sboCount.setObjectName(_fromUtf8("sboCount"))
        self.horizontalLayout_2.addWidget(self.sboCount)
        self.label_2 = QtGui.QLabel(self.gboOptions)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pbnAdvanced = QtGui.QPushButton(ScriptDialogBase)
        self.pbnAdvanced.setGeometry(QtCore.QRect(10, 260, 503, 32))
        self.pbnAdvanced.setCheckable(True)
        self.pbnAdvanced.setChecked(False)
        self.pbnAdvanced.setObjectName(_fromUtf8("pbnAdvanced"))

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
        self.gboOptions.setTitle(QtGui.QApplication.translate("ScriptDialogBase", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.cboNewProject.setText(QtGui.QApplication.translate("ScriptDialogBase", "Run in new project", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ScriptDialogBase", "Run selected script ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ScriptDialogBase", "times", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnAdvanced.setText(QtGui.QApplication.translate("ScriptDialogBase", "Show advanced options", None, QtGui.QApplication.UnicodeUTF8))

