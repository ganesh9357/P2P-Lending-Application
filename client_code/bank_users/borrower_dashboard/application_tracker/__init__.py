from ._anvil_designer import application_trackerTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import borrower_main_form_module as main_form_module

class application_tracker(application_trackerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_id=main_form_module.userId
    #self.user_id=1000
    # Any code you write here will run before the form oopens.
    self.repeating_panel_5.items=app_tables.loan_details.search(loan_updated_status='underprocess',coustmer_id=self.user_id)
    self.label_1.text=str(len(self.repeating_panel_5.items))
  def home_borrower_registration_button_click(self, **event_args):
   
    open_form('bank_users.borrower_dashboard')
