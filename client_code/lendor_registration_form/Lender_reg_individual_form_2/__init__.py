from ._anvil_designer import Lender_reg_individual_form_2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_individual_form_2(Lender_reg_individual_form_2Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user_data = anvil.server.call('get_user_data', user_id)
        
    if user_data:
            self.business_phone_number = user_data.get('business_no', '')
            self.landmark = user_data.get('company_landmark', '')
            self.comp_address = user_data.get('company_address', '')
            
            
    else:
        self.business_phone_number = ''
        self.landmark = ''
        self.comp_address = ''
        

       #Restore previously entered data if available
    if self.business_phone_number:
            self.text_box_1.text = self.business_phone_number
    if self.landmark:
            self.text_box_2.text = self.landmark
    if self.comp_address:
            self.text_box_3.text= self.comp_address

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    comp_address = self.text_box_1.text
    landmark = self.text_box_1.text
    business_phone_number = self.text_box_3.text
    user_id = self.userId
    if not comp_address or not landmark or not business_phone_number:
      Notification("please fill the required fields").show()
    else:
      anvil.server.call('add_lendor_individual_form_2',business_phone_number, landmark,comp_address,user_id)
      open_form('lendor_registration_form.Lender_reg_individual_form_3',user_id=self.userId)
    

  def button_1_click(self, **event_args):
    user_id = self.userId
    open_form('lendor_registration_form.Lender_reg_individual_form_1', user_id=self.userId)

  def button_3_click(self, **event_args):
    open_form("bank_users.user_form")
    
