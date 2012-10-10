"""
InaSAFE Disaster risk assessment tool developed by AusAid and World Bank
- **UI Test Cases.**

Contact : ole.moller.nielsen@gmail.com

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'bungcip@gmail.com'
__version__ = '0.5.0'
__date__ = '10/10/2012'
__copyright__ = ('Copyright 2012, Australia Indonesia Facility for '
                 'Disaster Reduction')

import unittest
import sys
import os


# Add PARENT directory to path to make test aware of other modules
pardir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(pardir)


#!/usr/bin/python

from qgis.core import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *


from safe_qgis.dock import Dock
from safe_qgis.options_dialog import OptionsDialog


def run_script(iface):
    global IFACE

    IFACE = iface

    test = UiTest()
    test.setUp()

    test.test_dock()
    test.test_options_dialog()

    test.tearDown()


class UiTest(unittest.TestCase):
    """Test for User Interface
    """

    def setUp(self):
        """Fixture run before all tests"""

        ## widgets
        mainWindow = IFACE.mainWindow()
        self.dock = mainWindow.findChild(Dock, 'InaSAFEDock')
        self.actionDock = mainWindow.findChild(QAction, 'InaSAFEActionDock')
        self.actionOptions = mainWindow.findChild(
            QAction, 'InaSAFEActionOptions')

        ## default state of widgets
        self.dock.setVisible(False)
        self.actionDock.setChecked(False)

        self.dock.showOnlyVisibleLayersFlag = True
        #loadStandardLayers()
        self.dock.cboHazard.setCurrentIndex(0)
        self.dock.cboExposure.setCurrentIndex(0)
        self.dock.cboFunction.setCurrentIndex(0)
        self.dock.runInThreadFlag = False
        self.dock.showOnlyVisibleLayersFlag = False
        self.dock.setLayerNameFromTitleFlag = False
        self.dock.zoomToImpactFlag = False
        self.dock.hideExposureFlag = False
        self.dock.showPostProcessingLayers = False

    def tearDown(self):
        pass

    def test_dock(self):

        ## when we click the dock button, InsafeDock widget must be visible
        self.actionDock.trigger()

        assert self.actionDock.isChecked()
        assert self.dock.isVisible()

    def test_options_dialog(self):

        ## when we click options button, OptionsDialog must be visible
        self.actionOptions.trigger()

        self.optionsDialog = IFACE.mainWindow().findChild(
            OptionsDialog, 'InaSAFEOptionsDialog')

        #assert self.optionsDialog.isHidden() is False
        assert self.optionsDialog.isVisible()

        ## check OptionsDialog flags
        self.optionsDialog.cbxUseThread.setChecked(True)
        self.optionsDialog.cbxVisibleLayersOnly.setChecked(True)
        self.optionsDialog.accept()

        assert self.dock.runInThreadFlag is True
        assert self.dock.showOnlyVisibleLayersFlag is True


## iface is None when running test from command line
import qgis.utils
IFACE = qgis.utils.iface

if __name__ == '__main__':
    #QGISAPP, CANVAS, IFACE, PARENT = getQgisTestApp()


    suite = unittest.makeSuite(UiTest)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

