from ._anvil_designer import foreclose_details_approvedTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables




class foreclose_details_approved(foreclose_details_approvedTemplate):
  def __init__(self, selected_row, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.selected_row = selected_row
    self.name.text = f"{selected_row['borrower_name']}"
    self.loan.text = f"{selected_row['loan_amount']}"
    self.reason.text = f"{selected_row['reason']}"
    self.oa.text = f"{selected_row['outstanding_amount']}"
    self.total.text = f"{selected_row['paid_amount']}"

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vlfr")

