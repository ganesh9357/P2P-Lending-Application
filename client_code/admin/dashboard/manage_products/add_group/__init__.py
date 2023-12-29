from ._anvil_designer import add_groupTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class add_group(add_groupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.text_box_1 = TextBox()

    # Any code you write here will run before the form opens.
  def add_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        # Get the text entered in the TextBox
        group_name = self.text_box_1.text
        # Check if the entered group_name is not empty
        if group_name:
            # Add the group_name to the "product_group" data table
            app_tables.product_group.add_row(name=group_name)
            # Optionally, you can clear the TextBox after adding the group
            self.text_box_1.text = ''
            # Optionally, provide feedback to the user
            alert(f' "{group_name}" added successfully!')
            open_form('admin.dashboard.manage_products.add_product_categories_and_groups')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_products')
