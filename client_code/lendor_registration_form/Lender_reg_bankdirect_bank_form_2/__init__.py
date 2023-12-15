from ._anvil_designer import Lender_reg_bankdirect_bank_form_2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_bankdirect_bank_form_2(Lender_reg_bankdirect_bank_form_2Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user_data = anvil.server.call('get_user_data', user_id)
    if user_data:
            self.ifsc = user_data.get('ifsc_code', '')
            self.salary_type = user_data.get('salary_type', '')
            self.branch_name = user_data.get('branch_name', '')
            self.net_bank= user_data.get('net_bank', '')
            
            
    else:
        self.ifsc = ''
        self.salary_type = ''
        self.branch_name = ''
        self.net_bank = ''
        

       #Restore previously entered data if available
    if self.ifsc:
            self.text_box_1.text= self.ifsc
    if self.salary_type:
            self.drop_down_1.selected_value = self.salary_type
    if self.branch_name:
          self.text_box_2.text = self.branch_name
    if self.net_bank:
           self.drop_down_2.selected_value = self.net_bank

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    ifsc = self.text_box_1.text
    salary_type = self.drop_down_1.selected_value
    branch_name = self.text_box_2.text
    net_bank = self.drop_down_2.selected_value
    user_id = self.userId
    if not ifsc or not salary_type or not branch_name or not net_bank:
      Notification("please fill all required fields").show()
    else:
      anvil.server.call('add_lendor_bank_details_form_2', ifsc,salary_type,branch_name,net_bank, user_id)
      open_form('lendor_registration_form.dashboard')

  def button_1_click(self, **event_args):
    user_id = self.userId
    open_form('lendor_registration_form.Lender_reg_bothdirect_bank_form_1',user_id=self.userId)

  def button_3_click(self, **event_args):
    open_form("bank_users.user_form")
    
    
