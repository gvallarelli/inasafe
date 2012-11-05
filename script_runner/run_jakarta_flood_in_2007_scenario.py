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
import safe_qgis.macro as macro

def runScript():
    myRoot = os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(
        __file__)),
          '..',
          '..',
          'inasafe_data'))

    myDock = macro.findInaSAFEDock()
    myDock.show()

    # open jakarta layer
    macro.addLayers(myRoot, [
        'exposure//DKI_Buildings.shp',
        'hazard/Jakarta_RW_2007flood.shp',
        'test/Population_Jakarta_geographic.asc',
    ])

#    macro.addVectorLayer(myRoot, [
#        'exposure/DKI_Buildings.shp',
#        'hazard/Jakarta_RW_2007flood.shp',
 #       'hazard/Flood_Current_Depth_Jakarta_geographic.asc',
#        'hazard/Population_Jakarta_geographic.asc',
#        'exposure/DKI_buildings.shp',
#        'hazard/jakarta_flood_category_123.asc',
#        'exposure/kabupaten_jakarta_singlepart.shp',
#    ])

    macro.setupScenario(
        theHazard='A flood in Jakarta',
        theExposure='Bangunan-bangunan penting',
        theFunction='Terkena banjir',
    )

#    myResult, myMessage = macro.setupScenario(
#        theHazard='A flood in Jakarta like in 2007',
#        theExposure='People',
#        theFunction='Need evacuation',
#        theFunctionId='Flood Evacuation Function',
#        theAggregation='kabupaten jakarta singlepart',
#        theAggregationEnabledFlag=True)
#
#    assert myResult, myMessage

    macro.runScenario()
