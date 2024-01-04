from ._anvil_designer import RowTemplate28Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..EditDetailsForm import EditDetailsForm


class RowTemplate28(RowTemplate28Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


  def link_1_click(self, **event_args):
        # Assuming you have access to the necessary data in this class
        item_data = self.item

        # Open the EditDetailsForm and pass the selected item_data as a row
        open_form('admin.dashboard.manage_products.view_products_and_categories.EditDetailsForm', selected_row=item_data)