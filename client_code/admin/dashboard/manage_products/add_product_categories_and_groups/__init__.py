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

    # Any code you write here will run before the form opens.

  def home_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def button_1_click(self, **event_args):
    # Assuming text_box_1 is used for both groups and as a new category
    groups = self.text_box_1.text
    category = groups  # Set the category to the user input
    
    # Convert category to string explicitly
    category_str = str(category)
    
    # Add the user input (category) to the dropdown options only if it's not already present
    if category_str not in self.drop_down_1.items:
        self.drop_down_1.items.append(category_str)
    
    # Set the selected value to the user input (category)
    self.drop_down_1.selected_value = category_str
    
    # Call the server function with the updated values
    anvil.server.call('manage_products', groups, category_str)
