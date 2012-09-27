from safe.impact_functions.core import FunctionProvider
from safe.impact_functions.core import get_hazard_layer, get_exposure_layer
from safe.impact_functions.core import get_question
from safe.storage.vector import Vector
from safe.common.utilities import ugettext as _
from safe.common.tables import Table, TableRow
from safe.common.dynamic_translations import names as internationalised_values
from safe.engine.interpolation import assign_hazard_values_to_exposure_data


class VolcanoBuildingImpactFunction(FunctionProvider):
    """Impact plugin for volcanic hazards on buildings

    :param requires category=='hazard' and \
                    subcategory in ['volcano']
                    layertype=='raster'

    :param requires category=='exposure' and \
                    subcategory in ['building', 'structure'] and \
                    layertype=='vector'
    """

    title = _('Be affected') # To be seen in the Might drop down
    target_field = 'alert_level' # Output attribute field name
    

    def run(self, layers):
        """Impact plugin for volcanic hazards on buildings

        Input
          layers: List of layers expected to contain
              H: Polygon of volcanic hazard zones
              P: Polygon or points of buildings or Points of Interest
              

        Counts number of buildings exposed to the specific volcanic
        hazard zones.

        Return
          Map of buildings exposed to each Volcanic Hazard zone
          Table with number of buildings affected by each Volcanic Hazard zone
        """
             

        # Extract data
        H = get_hazard_layer(layers)    # Polygon Volcanic Hazard Zone
        E = get_exposure_layer(layers)  # Building locations

        question = get_question(H.get_name(),
                                E.get_name(),
                                self)

        # Check that hazard is polygon type
        if not H.is_vector:
            msg = ('Input hazard %s  was not a vector layer as expected '
                   % H.get_name())
            raise Exception(msg)

        msg = ('Input hazard must be a polygon layer. I got %s with layer '
               'type %s' % (H.get_name(),
                            H.get_geometry_name()))
        if not H.is_polygon_data:
            raise Exception(msg)

        # Interpolate volcanic hazard zone to building locations
        I = assign_hazard_values_to_exposure_data(H, E)

        # Extract relevant exposure data
        attribute_names = I.get_attribute_names()
        attributes = I.get_data()
        N = len(I)

        # Initialise attributes of output dataset with all attributes
        # from input polygon and a building count of zero
        new_attributes = H.get_data()
       
        aggregate_attribute_name = self.target_field # hazard attribute name
        categories = {}
        for attr in new_attributes:
            attr[self.target_field] = 0
            alert = attr[aggregate_attribute_name]
            categories[alert] = 0

        # Count affected buildings per polygon and per category in alert zone
        for attr in I.get_data():
            
            # Count buildings in each category per polygon
            poly_id = attr['polygon_id']
            new_attributes[poly_id][self.target_field] += 1

            # Total building count for each category
            alert = new_attributes[poly_id][aggregate_attribute_name]
            categories[alert] += 1
            
          
        # Generate impact report for the pdf map and on-screen display
        table_body = [question,
                      TableRow([_('Alert Level'),
                                _('Total')],header=True)]
        for name, count in categories.iteritems():
            table_body.append(TableRow([name, int(count)]))

        table_body.append(TableRow(_('Map shows buildings affected in '
                                     'each of volcano hazard alert levels.')))
        impact_table = Table(table_body).toNewlineFreeString()

        # Extend impact report for on-screen display
        table_body.extend([TableRow(_('Notes'), header=True),
                           _('Total buildings %i in view port') % total,
                           _('Alert levels refer to:')])
        #FIXME need to be able to grab from the attribute table and show
        #alert_level vs hazard_desc

        impact_summary = Table(table_body).toNewlineFreeString()
        map_title = _('Buildings affected by volcanic hazard zone')

     
        # Create style
        style_classes = [dict(label=_('4'), min=4, max=4,
                              colour='#1EFC7C', transparency=0, size=1),
                         dict(label=_('3'), min=3, max=3,
                              colour='#1EFC2FC', transparency=0, size=1),
                         dict(label=_('2'), min=2, max=2,
                              colour='#1E1E7C', transparency=0, size=1)]
        style_info = dict(target_field=self.target_field,
                          style_classes=style_classes)

        # Create vector layer and return
        V = Vector(data=attributes,
                   projection=I.get_projection(),
                   geometry=I.get_geometry(),
                   name=_('Estimated buildings affected'),
                   keywords={'impact_summary': impact_summary,
                             'impact_table': impact_table,
                             'map_title': map_title},
                   style_info=style_info)
        return V
