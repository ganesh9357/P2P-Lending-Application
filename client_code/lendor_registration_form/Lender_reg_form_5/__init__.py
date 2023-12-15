from ._anvil_designer import Lender_reg_form_5Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_form_5(Lender_reg_form_5Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user_data = anvil.server.call('get_user_data', user_id)
        
    if user_data:
            self.pincode = user_data.get('pincode', '')
            self.state = user_data.get('state', '')
            self.country = user_data.get('country', '')
            
            
    else:
        self.pincode = ''
        self.state = ''
        self.country = ''
        

       #Restore previously entered data if available
    if self.pincode:
            self.text_box_1.text = self.pincode
    if self.state:
            self.text_box_2.text = self.state
    if self.country:
            self.text_box_3.text = self.country

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    pincode = self.text_box_1.text
    state = self.text_box_2.text
    country = self.text_box_3.text
    user_id = self.userId
    if not pincode or not state or not country:
      Notification("Please fill all the filelds").show()
    else:
     anvil.server.call('add_lendor_five_form',pincode,state,country,user_id)
     open_form('lendor_registration_form.Lender_reg_form_6',user_id = user_id)
    

  def button_1_click(self, **event_args):
    user_id = self.userId
    open_form('lendor_registration_form.Lender_reg_form_4',user_id=user_id)
    

  def button_3_click(self, **event_args):
    open_form("bank_users.user_form")
    
