from ._anvil_designer import star_1_borrower_registration_form_begin_3b_studentTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import re

class star_1_borrower_registration_form_begin_3b_student(star_1_borrower_registration_form_begin_3b_studentTemplate):
  def __init__(self,user_id, **properties):
    self.user_id=user_id
    user_data=app_tables.user_profile.get(coustmer_id=user_id)
    if user_data:
     self.borrower_college_name_text.text=user_data['college_name']
     self.borrower_college_id_text.text=user_data['college_id']
     self.borrower_college_address_text.text=user_data['college_address']
     user_data.update()
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.

  def button_1_copy_1_copy_1_copy_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3c',user_id=self.user_id)

  def home_borrower_registration_form_copy_1_click(self, **event_args):
    open_form('bank_users.user_form')

  def button_1_next_copy_1_click(self, **event_args):
    college_name=self.borrower_college_name_text.text
    college_id=self.borrower_college_id_text.text
    college_proof=self.borrower_college_proof_img.file
    college_address=self.borrower_college_address_text.text
    user_id=self.user_id
    if not re.match(r'^[A-Za-z\s]+$', college_name):
      self.label_5.text='enter valid college name'
      self.label_5.visible=True
    elif not college_address:
      self.label_6.text='enter valid college address'
      self.label_6.visible=True
    elif not college_id:
      self.label_7.text='please enter valid id'
      self.label_7.visible=True
    elif not college_proof or not isinstance(college_proof, anvil.BlobMedia):
      self.label_8.text='enter valid college proof'
    elif not college_name or not college_id or not college_proof or not college_address:
      Notification("please fill all requrired fields").show()
    else:
      anvil.server.call('add_borrower_student',college_name,college_id,college_proof,college_address,user_id)
      open_form('borrower_registration_form.star_1_borrower_registration_form_begin_4',user_id=user_id)
