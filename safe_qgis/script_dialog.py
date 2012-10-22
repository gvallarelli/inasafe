"""
InaSAFE Disaster risk assessment tool developed by AusAid -
**Impact Functions Dialog.**

Contact : ole.moller.nielsen@gmail.com

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'bungcip@gmail.com'
__revision__ = '$Format:%H$'
__date__ = '01/10/2012'
__copyright__ = ('Copyright 2012, Australia Indonesia Facility for '
                 'Disaster Reduction')

import os
import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSignature
from script_dialog_base import Ui_ScriptDialogBase

import qgis.utils


class ScriptDialog(QtGui.QDialog, Ui_ScriptDialogBase):
    """Script Dialog for InaSAFE."""

    def __init__(self, theParent=None):
        """Constructor for the dialog.

        Args:
           * theParent - Optional widget to use as parent
        Returns:
           not applicable
        Raises:
           no exceptions explicitly raised
        """
        QtGui.QDialog.__init__(self, theParent)
        self.setupUi(self)
        self.setWindowTitle(self.tr('Script Dialog'))

        self.tblScript.setColumnWidth(0, 200)
        self.tblScript.setColumnWidth(1, 50)


        # add script folder to sys.path
        sys.path.append(self.getScriptPath())

        self.populateTable()

    def getScriptPath(self):
        """ Get base path for directory that contains the script files

        Returns:
        String containing absolute base path for script files
        """
        myRoot = os.path.dirname(__file__)
        return os.path.abspath(os.path.join(myRoot, '..', 'script_runner'))

    def populateTable(self):
        """ Populate table list in script dialog with file
        from folder 'script_runner'

        Returns:
        None
        """

        self.tblScript.clearContents()

        # load the list of files in 'script_runner' folder
        myPath = self.getScriptPath()

        # get '.py' files in folder
        myFiles = [
            x for x in os.listdir(myPath) if os.path.splitext(x)[1] == '.py']

        # insert files to table widget
        self.tblScript.setRowCount(len(myFiles))
        for index, filename in enumerate(myFiles):
            self.tblScript.setItem(index, 0, QtGui.QTableWidgetItem(filename))
            self.tblScript.setItem(index, 1, QtGui.QTableWidgetItem(''))


    def runScript(self, theFilename):
        """ runs script in QGIS
        Args:
           * theFilename - the script filename
        Returns:
           not applicable
        Raises:
           no exceptions explicitly raised
        """

        # set status to 'running'


        # run script
        myModule, _ = os.path.splitext(theFilename)
        myScript = __import__(myModule)

        myScript.run_script(qgis.utils.iface)


    @pyqtSignature('')
    def on_btnRunSelected_clicked(self):
        myCurrentRow = self.tblScript.currentRow()
        myFilename = str(self.tblScript.item(myCurrentRow, 0).text())

        # set status to 'running'
        myStatusItem = self.tblScript.item(myCurrentRow, 1)
        myStatusItem.setText(self.tr('Running'))

        # run script
        try:
            self.runScript(myFilename)
        except Exception as ex:
            # set status to 'fail'
            myStatusItem.setText(self.tr('Fail'))
            # just reraise the exception
            raise

        # set status to 'OK'
        myStatusItem.setText(self.tr('OK'))

    @pyqtSignature('')
    def on_btnRefresh_clicked(self):
        self.populateTable()
