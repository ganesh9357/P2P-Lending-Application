from ._anvil_designer import RowTemplate19Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

class RowTemplate19(RowTemplate19Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    selected_row=self.item
    open_form("lendor_registration_form.dashboard.vcl.closed_loans_details",selected_row=selected_row)
