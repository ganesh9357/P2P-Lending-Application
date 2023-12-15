from ._anvil_designer import Lender_reg_Institutional_form_1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_Institutional_form_1(Lender_reg_Institutional_form_1Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user_data = anvil.server.call('get_user_data', user_id)
        
    if user_data:
            self.business_name = user_data.get('business_name', '')
            self.business_add = user_data.get('business_add', '')
            self.business_location = user_data.get('business_location', '')
            self.branch_name = user_data.get('branch_name', '')
            
            
            
            
    else:
        self.business_name = ''
        self.business_add = ''
        self.business_location= ''
        self.branch_name = ''
        
        

       #Restore previously entered data if available
    if self.business_name:
            self.text_box_1.text= self.business_name
    if self.business_add:
            self.text_box_2.text= self.business_add
    if self.business_location:
            self.text_box_3.text= self.business_location
    if self.branch_name:
            self.text_box_4.text= self.branch_name

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
      open_form('lendor_registration_form.Lender_reg_Institutional_form_2',user_id=self.userId)
    

  def button_1_click(self, **event_args):
    user_id = self.userId
    open_form('lendor_registration_form.Lender_reg_form_6',user_id=self.userId)
    """This method is called when the button is clicked"""

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("bank_users.user_form")
    
