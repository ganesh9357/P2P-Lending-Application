from ._anvil_designer import view_details_1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...import lendor_main_form_module as main_form_module
from datetime import datetime


class view_details_1(view_details_1Template):
  def __init__(self,selected_row, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    # Display loan details
    self.loan_id_label.text = f"{selected_row['loan_id']}"
    self.loan_amount_label.text=f"{selected_row['loan_amount']}"
    self.intrest_rate_label.text=f"{selected_row['interest_rate']}"
    self.tenure_label.text=f"{selected_row['tenure']}"
    #timestamp = selected_row['timestamp']
    #date_of_apply = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ").date()
    #self.date_of_apply_label.text = f"{date_of_apply}"
    self.loan_updated_status_label.text=f"{selected_row['loan_updated_status']}"

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.lender_view_loans")

  def button_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('lendor_registration_form.dashboard')

