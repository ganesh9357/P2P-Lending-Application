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
    under_process_items = list(app_tables.loan_details.search(loan_updated_status=q.like('under process%'), borrower_customer_id=self.user_id))
    approved_items = list(app_tables.loan_details.search(loan_updated_status=q.like('approved%'), borrower_customer_id=self.user_id))
    close_items = list(app_tables.loan_details.search(loan_updated_status=q.like('close%'), borrower_customer_id=self.user_id))
    
    all_items = under_process_items + approved_items + close_items
    
    self.repeating_panel_5.items = all_items
    self.label_1.text = str(len(all_items))
  



  
  def home_borrower_registration_button_click(self, **event_args):
    open_form('bank_users.borrower_dashboard')
