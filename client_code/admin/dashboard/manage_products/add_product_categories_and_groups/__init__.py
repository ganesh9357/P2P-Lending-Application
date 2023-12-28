from ._anvil_designer import add_product_categories_and_groupsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class add_product_categories_and_groups(add_product_categories_and_groupsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    options = app_tables.product_group.search()
    option_strings = [option['name'] for option in options]
    self.drop_down_1.items = option_strings
    self.drop_down_1.selected_value = option_strings[0] if option_strings else None   

  def name_change(self, **event_args):

        # Check the selected value of drop_down_1
        selected_group = self.drop_down_1.selected_value

        # Make additional features visible if a group is selected
        if selected_group:
            self.label_2.visible = True
            self.drop_down_2.visible = True
        else:
            # Hide additional features if no group is selected
            self.label_2.visible = False
            self.drop_down_2.visible = False