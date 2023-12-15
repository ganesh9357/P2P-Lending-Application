from ._anvil_designer import star_1_borrower_registration_form_begin_3aTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import re
class star_1_borrower_registration_form_begin_3a(star_1_borrower_registration_form_begin_3aTemplate):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    user_data=app_tables.user_profile.get(coustmer_id=user_id)
    if user_data:
      self.father_name_br3a_text.text=user_data['father_name']
      self.father_age_br3a_text.text=user_data['father_age']
      self.mother_name_br3a_text.text=user_data['mother_name']
      self.mother_age_br3a_text.text=user_data['mother_age']
      user_data.update()
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  

  def home_borrower_registration_form_copy_1_click(self, **event_args):
    open_form('bank_users.user_form')

  def button_1_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3a_1',user_id = self.userId)

  def button_2_click(self, **event_args):
    father_name = self.father_name_br3a_text.text
    father_age = self.father_age_br3a_text.text
    mother_name = self.mother_name_br3a_text.text
    mother_age = self.mother_age_br3a_text.text
    user_id = self.userId
    if not re.match(r'^[A-Za-z\s]+$', father_name):
      self.label_1.text='enter valid name'
      self.label_1.visible=True
    elif not re.match(r'^[A-Za-z\s]+$', mother_name):
      self.label_2.text='enter valid name'
      self.label_2.visible=True
    elif not father_name or not father_age or not mother_name or not mother_age:
      Notification("Please fill all required fields").show()
    else:
      anvil.server.call('add_borrower_step3a',father_name,father_age,mother_name,mother_age,user_id)
      open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3c',user_id=user_id)
      self.label_1.visible=False
      self.label_2.visible=False

