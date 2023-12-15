from ._anvil_designer import closed_loans_detailsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class closed_loans_details(closed_loans_detailsTemplate):
  def __init__(self, selected_row,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name.text = f"{selected_row['full_name']}"
    self.amount.text=f"{selected_row['loan_amount']}"
    self.tenure.text = f"{selected_row['tenure']}"
    self.emi.text = f"{selected_row['monthly_emi']}"
    self.interest.text = f"{selected_row['interest_rate']}"
    self.closed.text = f"{selected_row['closed_date']}"
   

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vcl")