from ._anvil_designer import Lender_reg_form_3Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import re

class Lender_reg_form_3(Lender_reg_form_3Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user_data = anvil.server.call('get_user_data', user_id)
        
    if user_data:
            self.aadhaar_no = user_data.get('aadhaar_no', '')
            self.pan_number = user_data.get('pan_number', '')
            
            
    else:
        self.aadhaar_no = ''
        self.pan_number = ''
        

       #Restore previously entered data if available
    if self.aadhaar_no:
            self.text_box_1.text = self.aadhaar_no
    if self.pan_number:
            self.text_box_2.text = self.pan_number

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    aadhaar_card = self.text_box_1.text
    aadhaar_photo = self.file_loader_2.file
    pan_card = self.text_box_2.text
    pan_id = self.file_loader_1.file
    user_id = self.userId
    if not aadhaar_card or not aadhaar_photo or not pan_card or not pan_id:
      Notification("Please fill all the fields").show()
# Validate PAN card details
    pan_pattern = re.compile(r'^[A-Za-z]{5}\d{4}[A-Za-z]$')
    if not pan_pattern.match(pan_card) or len(pan_card) != 10:
       Notification("Please enter a valid PAN card number").show()
       return
       

        # Validate Aadhaar card details
    if len(aadhaar_card) != 12 or not aadhaar_card.isdigit():
        Notification("Please enter a valid Aadhaar number").show()
        return
      
        

        # If all validations pass, call the server function
    anvil.server.call('add_lendor_third_form', aadhaar_photo, pan_card, pan_id, aadhaar_card, user_id)
    open_form('lendor_registration_form.Lender_reg_form_4', user_id=user_id)


    '''else:
     anvil.server.call('add_lendor_third_form', aadhaar_photo, pan_card, pan_id,aadhaar_card,user_id)
     open_form('lendor_registration_form.Lender_reg_form_4',user_id = user_id)'''


  def button_1_click(self, **event_args):
    user_id = self.userId
    open_form('lendor_registration_form.Lender_reg_education_form',user_id=user_id)
    """This method is called when the button is clicked"""

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("bank_users.user_form")
    
