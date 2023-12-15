
from ._anvil_designer import Lender_reg_form_2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_form_2(Lender_reg_form_2Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
   
    user_data = anvil.server.call('get_user_data', user_id)
        
    if user_data:
            self.mobile = user_data.get('mobile', '')
            self.another_email = user_data.get('another_email', '')
            
            
    else:
        self.mobile = ''
        self.another_email = ''
        

       #Restore previously entered data if available
    if self.mobile:
            self.text_box_1.text = self.mobile
    if self.another_email:
            self.text_box_2.text = self.another_email
    
            
        

    # Any code you write here will run before the form opens.

  
    
  def button_1_click(self, **event_args):
    user_id = self.userId
    open_form('lendor_registration_form.Lender_reg_form_1',user_id=user_id)
    
    

  def button_2_click(self, **event_args):
    #investment=self.drop_down_1.selected_value
    mobile = self.text_box_1.text
    email = self.text_box_2.text
    photo = self.file_loader_1.file
    user_id = self.userId
    if len(mobile) != 10 or not mobile.isdigit():
     Notification("Please enter a valid 10-digit mobile number").show()
     return

    if not email or not photo:
      Notification("Please fill all the fields").show()
    else:
     anvil.server.call('add_lendor_second_form', mobile, email, photo, user_id)
     open_form('lendor_registration_form.Lender_reg_education_form', user_id=user_id)



  
  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("bank_users.user_form")
