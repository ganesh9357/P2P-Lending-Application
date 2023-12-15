from ._anvil_designer import star_1_borrower_registration_form_begin_8Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_begin_8(star_1_borrower_registration_form_begin_8Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    user_data=app_tables.user_profile.get(coustmer_id=user_id)
    if user_data:
      self.text_box_1.text=user_data['account_name']
      self.drop_down_1.selected_value=user_data['account_type']
      self.text_box_3.text=user_data['account_number']
      self.text_box_4.text=user_data['branch_name']
      user_data.update()
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    account_name = self.text_box_1.text
    account_type = self.drop_down_1.selected_value
    account_number = self.text_box_3.text
    bank_branch = self.text_box_4.text
    user_id = self.userId
    if not account_name or not account_type or not account_number or not bank_branch:
      Notification("please fill the all required fields").show()
    else:
      anvil.server.call('add_borrower_step8', account_name, account_type,account_number,bank_branch, user_id)
      open_form('borrower_registration_form.star_1_borrower_registration_form_begin_9',user_id=self.userId)

  def button_1_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin_7',user_id=self.userId)

  def button_3_click(self, **event_args):
    open_form("bank_users.user_form")
