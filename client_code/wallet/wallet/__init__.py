from ._anvil_designer import walletTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import open_form, server


class wallet(walletTemplate):
  def __init__(self, user_id, **properties):
    user_id = self.user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.deposit_placeholder = "5000"
    self.withdraw_placeholder = "0.00"

    lender_wallet_amount = None

    user_data = app_tables.wallet.search(lender_customer_id=user_id)

    if user_data and len(user_data) > 0:
      lender_wallet_amount = user_data[0]['lender_wallet_amount']

    if lender_wallet_amount:
      self.amount_text_box.text = lender_wallet_amount

    # Any code you write here will run before the form opens.

  def home_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard")

  def about_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.dasboard_about")

  def contact_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.dasboard_contact")

  def notification_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('lendor_registration_form.dashboard.notification')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def deposit_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_9.visible = False
    self.text_box_5.visible = False
    self.icon1.visible = False
    self.amount_text_box.placeholder = self.deposit_placeholder
    self.deposit_money_btn.visible = True
    self.withdraw_money_btn.visible = False


  def withdraw_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_9.visible = True
    self.text_box_5.visible = True
    self.icon1.visible = True
    self.amount_text_box.placeholder = self.withdraw_placeholder
    self.deposit_money_btn.visible = False
    self.withdraw_money_btn.visible = True
    self.deposit_btn.visible = True

  def wallet_dashboard_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def deposit_money_btn_click(self,**event_args):
    """This method is called when the button is clicked"""
    user_data = app_tables.wallet.search(lender_customer_id=user_id)
    user_id = self.user_id
    
    lender_wallet_amount = self.amount_text_box.text
   
    if lender_wallet_amount:
      user_data = app_tables.wallet.search(lender_customer_id=user_id)

    if user_data and len(user_data) > 0:
      user_row = user_data[0]
      user_row['lender_wallet_amount'] = int(lender_wallet_amount)
    
    else:
      # If the row doesn't exist, add a new row
      app_tables.wallet.add_row(lender_customer_id=user_id, lender_wallet_amount=lender_wallet_amount)

 
           
    
    

  
    

  

  
   
    
    
    

