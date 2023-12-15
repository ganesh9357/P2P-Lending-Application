from ._anvil_designer import borrower_today_duesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime,timedelta
from .. import borrower_main_form_module as main_form_module 

class borrower_today_dues(borrower_today_duesTemplate):
    def __init__(self, **properties):
        self.user_id = main_form_module.userId
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        
        # Fetch all loan details
        all_loans = app_tables.loan_details.search()
        
        # Calculate days left and days gone for each loan
        for loans in all_loans:
          due_date=loans['due_date']
          days_left=(due_date-datetime.now()).days()
          loans['days_left']=days_left
          self.repeating_panel_1.items=all_loans

    def home_borrower_registration_form_copy_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('bank_users.borrower_dashboard')
