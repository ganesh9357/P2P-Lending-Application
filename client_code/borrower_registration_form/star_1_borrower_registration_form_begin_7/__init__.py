from ._anvil_designer import star_1_borrower_registration_form_begin_7Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_begin_7(star_1_borrower_registration_form_begin_7Template):
  def __init__(self,user_id, **properties):
    self.init_components(**properties)
    self.userId = user_id
    user_data=app_tables.user_profile.get(coustmer_id=user_id)
    if user_data:
      self.text_box_1.text=user_data['running_Home_Loan']
      self.text_box_2.text=user_data['running_or_live loans']
      self.text_box_3.text=user_data['other_loan']
      user_data.update()
  def button_1_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin_4',user_id = self.userId)

  def button_2_click(self, **event_args):
    home_loan = self.text_box_1.text
    other_loan = self.text_box_2.text
    live_loan = self.text_box_3.text
    user_id = self.userId
    if not home_loan or not other_loan or not live_loan:
      Notification("please fill the all required fields")
    else:
      anvil.server.call('add_borrower_step7',home_loan,other_loan,live_loan,user_id)
      open_form('borrower_registration_form.star_1_borrower_registration_form_begin_8',user_id=user_id)

  def home_borrower_registration_form_click(self, **event_args):
    open_form('bank_users.user_form')
