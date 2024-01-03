from ._anvil_designer import RowTemplate28Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
#from .EditDetailsForm import EditDetailsForm

class RowTemplate28(RowTemplate28Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  # def link_1_click(self, **event_args):
  #   """This method is called when the link is clicked"""
    
  #   open_form('admin.dashboard.manage_products.view_products_and_categories.EditDetailsForm')

  def link_1_click(self, **event_args):
        """This method is called when the link is clicked"""
        # Assuming you have access to the necessary data in this class
        selected_group = self.item['name_group']
        selected_category = self.item['name_categories']

        # Create a new instance of the EditDetailsForm and show it
        edit_form = EditDetailsForm(selected_group, selected_category)
        edit_form.show()