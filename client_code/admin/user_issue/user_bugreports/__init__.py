from ._anvil_designer import user_bugreportsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class user_bugreports(user_bugreportsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data = tables.app_tables.user_profile.search()
    
    self.email_user = []

    a = -1
    for i in self.data:
      a+=1
      self.email_user.append(i['email_user'])

    if a == -1:
      alert("No Data Available Here!!")
    else:
      self.label_8.text = self.email_user[a]

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    user_issues = self.drop_down_1.selected_value
    specific_issues = self.drop_down_2.selected_value
    user_discription = self.text_area_1.text
    image = self.file_loader_1.file
    feedback_form = self.text_area_2.text

    name = tables.app_tables.user_profile.search()
    
    email_user = []
    coustmer_id = []

    c = -1
    for i in name:
      c+=1
      email_user.append(i['email_user'])
      coustmer_id.append(i['coustmer_id'])

    
    data = tables.app_tables.user_issues_bugreports.search()
    b = -1
    for i in data:
      b+=1

    if user_issues == "" or specific_issues == "" or user_discription == "" or image == "" or feedback_form == ""  :
      Notification("Fill All Required Details").show()
    else:
     anvil.server.call('user_issues_bugreports',user_issues,specific_issues,user_discription,image,feedback_form,email_user[-1],str(coustmer_id[-1]))
     alert("Submited successfull")
     open_form('bank_users.main_form')
     
  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_1.selected_value == 'Account Inquiries':
            # Add items to the dropdown dynamically
      items_to_add = [ 'Balance Inquiries', 'Transaction History' ]
      self.drop_down_2.items = items_to_add
    elif self.drop_down_1.selected_value == 'Loan and Mortgage Inquiries':
            # Add items to the dropdown dynamically
      items_to_add = ['Loan Application Status ', 'Mortgage Payment Inquiries']
      self.drop_down_2.items = items_to_add  
    elif self.drop_down_1.selected_value == 'Account Management':
            # Add items to the dropdown dynamically
      items_to_add = ['Account Closure','Change of Contact Information']
      self.drop_down_2.items = items_to_add  
    elif self.drop_down_1.selected_value == 'Financial Planning and Advice':
            # Add items to the dropdown dynamically
      items_to_add = ['Inquiries About Investment Options', 'Retirement Planning Assistance']
      self.drop_down_2.items = items_to_add  

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.main_form.about_main_form')

    
