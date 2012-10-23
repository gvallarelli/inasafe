"""
InaSAFE Disaster risk assessment tool developed by AusAid -
**Script to check InaSAFE widgets behavior**

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

from PyQt4.QtGui import *
from safe_qgis.dock import Dock
from safe_qgis.options_dialog import OptionsDialog

import safe_qgis.macro as macro

def runScript(iface):

    ## widgets
    mainWindow = iface.mainWindow()
    dock = mainWindow.findChild(Dock, 'InaSAFEDock')
    actionDock = mainWindow.findChild(QAction, 'InaSAFEActionDock')
    actionOptions = mainWindow.findChild(
        QAction, 'InaSAFEActionOptions')

    ## default state of widgets
    dock.setVisible(False)
    actionDock.setChecked(False)

    dock.showOnlyVisibleLayersFlag = True
    dock.cboHazard.setCurrentIndex(0)
    dock.cboExposure.setCurrentIndex(0)
    dock.cboFunction.setCurrentIndex(0)
    dock.runInThreadFlag = False
    dock.showOnlyVisibleLayersFlag = False
    dock.setLayerNameFromTitleFlag = False
    dock.zoomToImpactFlag = False
    dock.hideExposureFlag = False
    dock.showPostProcessingLayers = False

    ## when we click the dock button, InsafeDock widget must be visible
    actionDock.trigger()

    macro.assertTrue(actionDock.isChecked())
    macro.assertTrue(dock.isVisible())

    ## when we click options button, OptionsDialog must be visible
    actionOptions.trigger()

    optionsDialog = mainWindow.findChild(
        OptionsDialog, 'InaSAFEOptionsDialog')

    #assert optionsDialog.isHidden() is False
    macro.assertTrue(optionsDialog.isVisible())

    ## check OptionsDialog flags
    optionsDialog.cbxUseThread.setChecked(True)
    optionsDialog.cbxVisibleLayersOnly.setChecked(True)
    optionsDialog.accept()

    macro.assertTrue(dock.runInThreadFlag)
    macro.assertTrue(dock.showOnlyVisibleLayersFlag)
