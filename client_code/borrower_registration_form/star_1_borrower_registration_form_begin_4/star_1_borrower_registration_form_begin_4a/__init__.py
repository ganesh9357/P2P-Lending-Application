from ._anvil_designer import star_1_borrower_registration_form_begin_4aTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_begin_4a(star_1_borrower_registration_form_begin_4aTemplate):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    user_data=app_tables.user_profile.get(coustmer_id=user_id)
    if user_data:
      self.borrower_registration_spouse_name_text.text=user_data['spouse_name']
      self.marriage_date_date_pickeer.date=user_data['Date_mariage']
      self.borrower_registration_spouse_mobile_text_copy_1.text=user_data['spouse_mobile']
      user_data.update()
    self.init_components(**properties)
  def home_borrower_registration_form_copy_1_click(self, **event_args):
    open_form('bank_users.user_form')
    
  def submit_4_borrower_registration_form_click(self, **event_args):
    spouse_name = self.borrower_registration_spouse_name_text.text
    marrege_date = self.marriage_date_date_pickeer.date
    spouse_mobile_no=self.borrower_registration_spouse_mobile_text_copy_1.text
    user_id = self.userId
    if not spouse_name or not marrege_date or not spouse_mobile_no:
      Notification("please provide all Details")
    else:
      anvil.server.call('add_borrower_step4a',spouse_name,marrege_date,spouse_mobile_no,user_id)
      open_form('borrower_registration_form.star_1_borrower_registration_form_begin_5',user_id=user_id)

  def button_1_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin_4',user_id=self.userId)
