from ._anvil_designer import Lender_reg_form_4Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_form_4(Lender_reg_form_4Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user_data = anvil.server.call('get_user_data', user_id)
        
    if user_data:
            self.street_adress_1 = user_data.get('street_adress_1', '')
            self.street_address_2 = user_data.get('street_address_2', '')
            self.city = user_data.get('city', '')
            
            
    else:
        self.street_adress_1 = ''
        self.street_address_2 = ''
        self.city = ''
        

       #Restore previously entered data if available
    if self.street_adress_1:
            self.text_box_1.text = self.street_adress_1
    if self.street_address_2:
            self.text_box_2.text = self.street_address_2
    if self.city:
            self.text_box_3.text = self.city

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    street_adress_1 = self.text_box_1.text
    street_address_2 = self.text_box_2.text
    city = self.text_box_3.text
    user_id = self.userId
    if not street_adress_1 or not street_address_2 or not city:
      Notification("Please fill all the fields").show()
    else:
      anvil.server.call('add_lendor_four_form',street_adress_1,street_address_2,city,user_id)
      open_form('lendor_registration_form.Lender_reg_form_5',user_id = user_id)

  def button_1_click(self, **event_args):
    user_id = self.userId
    open_form('lendor_registration_form.Lender_reg_form_3',user_id=user_id)

  def button_3_click(self, **event_args):
    open_form("bank_users.user_form")
