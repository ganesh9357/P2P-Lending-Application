from ._anvil_designer import star_1_borrower_registration_form_begin_3b_business_3Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_begin_3b_business_3(star_1_borrower_registration_form_begin_3b_business_3Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    user_data=app_tables.user_profile.get(coustmer_id=user_id)
    if user_data:
      self.text_box_1.text=user_data['industry_type']
      self.text_box_2.text=user_data['six_month_turnover']
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def button_2_click(self, **event_args):
    industry_type = self.text_box_1.text
    turn_over = self.text_box_2.text
    last_six_statements = self.file_loader_1.file
    user_id = self.userId
    if not industry_type or not turn_over or not last_six_statements:
      Notification("Please fill all the fields")
    else:
     anvil.server.call('add_lendor_institutional_form_3',industry_type,turn_over,last_six_statements,user_id)
     open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3b_business_3.star_1_borrower_registration_form_begin_3b_business_4',user_id = user_id)

  def button_1_click(self, **event_args):
    user_id = self.userId
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3b_business_3.star_1_borrower_registration_form_begin_3b_business_2',user_id = user_id)
    """This method is called when the button is clicked"""

  def home_borrower_registration_form_copy_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.user_form')
