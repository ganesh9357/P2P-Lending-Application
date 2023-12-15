from ._anvil_designer import Lender_reg_individual_form_3Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_individual_form_3(Lender_reg_individual_form_3Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user_data = anvil.server.call('get_user_data', user_id)
        
    if user_data:
            self.annual_salary = user_data.get('annual_salary', '')
            self.designation = user_data.get('designation', '')
            
            
            
    else:
        self.annual_salary = ''
        self.designation = ''
        
        

       #Restore previously entered data if available
    if self.annual_salary:
            self.text_box_1.text= self.annual_salary
    if self.designation:
            self.text_box_2.text= self.designation
    

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    #self.userId = user_id
    open_form('lendor_registration_form.Lender_reg_individual_form_2',user_id=self.userId)
    

  def button_1_click(self, **event_args):
    annual_salary = self.text_box_1.text
    designation = self.text_box_2.text
    emp_id_proof = self.file_loader_1.file
    last_six_month = self.file_loader_2.file
    user_id = self.userId
    anvil.server.call('add_lendor_individual_form_3',annual_salary, designation,emp_id_proof,last_six_month,user_id)
    open_form('lendor_registration_form.Lender_reg_bothdirect_bank_form_1',user_id=self.userId)

  def button_3_click(self, **event_args):
    open_form("bank_users.user_form")
    
    
