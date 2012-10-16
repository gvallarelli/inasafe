"""
InaSAFE Disaster risk assessment tool developed by AusAid -
**Script to run jakarta flood scenariol**

Contact : ole.moller.nielsen@gmail.com

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'bungcip@gmail.com'
__revision__ = '$Format:%H$'
__date__ = '10/10/2012'
__copyright__ = ('Copyright 2012, Australia Indonesia Facility for '
                 'Disaster Reduction')

import os

from PyQt4.QtGui import *
from safe_qgis.dock import Dock
from safe_qgis.options_dialog import OptionsDialog

import qgis.utils

def run_script(iface):
    root = '/Users/bungcip/inasafe-dev/inasafe_data'

    iface.newProject()

    # open jakarta layer
    iface.addVectorLayer(os.path.join(root, 'exposure/DKI_Buildings.shp'), '', 'ogr')
    iface.addVectorLayer(os.path.join(root, 'hazard/Jakarta_RW_2007flood.shp'), '', 'ogr')

    # show inasafe dock
    dock = iface.mainWindow().findChild(Dock)
    dock.show()

    # select

    # klik 'Hitung' button
    dock.pbnRunStop.click()
