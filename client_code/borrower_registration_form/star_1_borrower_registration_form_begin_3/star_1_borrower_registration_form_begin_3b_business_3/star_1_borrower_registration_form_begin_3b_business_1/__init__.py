from ._anvil_designer import star_1_borrower_registration_form_begin_3b_business_1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_begin_3b_business_1(star_1_borrower_registration_form_begin_3b_business_1Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    user_data=app_tables.user_profile.get(coustmer_id=user_id)
    if user_data:
      self.text_box_1.text=user_data['business_name']
      self.text_box_2.text=user_data['business_location']
      self.text_box_3.text=user_data['business_add']
      self.text_box_4.text=user_data['branch_name']
      user_data.update()
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    business_name = self.text_box_1.text
    business_add = self.text_box_2.text
    business_location = self.text_box_3.text
    branch_name = self.text_box_4.text
    user_id = self.userId
    if not business_name or not business_add or not business_location or not branch_name:
      Notification("Please fill all the fields")
    else:
      anvil.server.call('add_lendor_institutional_form_1',business_name,business_add,business_location,branch_name,user_id)
      open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3b_business_3.star_1_borrower_registration_form_begin_3b_business_2',user_id=self.userId)


  def button_1_click(self, **event_args):
    user_id = self.userId
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3c',user_id=self.userId)
    

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("bank_users.user_form")
