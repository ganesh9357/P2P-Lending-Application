from ._anvil_designer import Lender_reg_Institutional_form_4Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_Institutional_form_4(Lender_reg_Institutional_form_4Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user_data = anvil.server.call('get_user_data', user_id)
        
    if user_data:
            self.director_name = user_data.get('director_name', '')
            self.director_no= user_data.get('director_no', '')
            self.din = user_data.get('din', '')
            self.cin= user_data.get('cin', '')
    
    else:
        self.director_name = ''
        self.director_no = ''
        self.din = ''
        self.cin= ''
       
       #Restore previously entered data if available
    if self.director_name:
            self.text_box_1.text= self.director_name
    if self.director_no:
            self.text_box_2.text= self.director_no
    if self.din:
            self.text_box_3.text= self.din
    if self.cin:
            self.text_box_4.text= self.cin

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    director_name = self.text_box_1.text
    director_no = self.text_box_2.text
    din = self.text_box_3.text
    cin = self.text_box_4.text
    user_id = self.userId
    if not director_name or not director_no or not din or not cin:
      Notification("Please fill all the fields")
    else:
     anvil.server.call('add_lendor_institutional_form_4',director_name,director_no,din,cin,user_id)
     open_form('lendor_registration_form.Lender_reg_Institutional_form_5',user_id = user_id)

  def button_1_click(self, **event_args):
    user_id = self.userId
    open_form('lendor_registration_form.Lender_reg_Institutional_form_3',user_id = user_id)
    """This method is called when the button is clicked"""

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("bank_users.user_form")
    
