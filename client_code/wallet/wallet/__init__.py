from ._anvil_designer import walletTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class wallet(walletTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.deposit_placeholder = "5000"
    self.withdraw_placeholder = "0.00"
    # self.amount_text_box.placeholder = self.deposit_placeholder

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
    self.amount_text_box.placeholder = self.deposit_placeholder
    self.deposit_money_btn.visible = True
    self.withdraw_money_btn.visible = False


  def withdraw_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_9.visible = True
    self.text_box_5.visible = True
    self.amount_text_box.placeholder = self.withdraw_placeholder
    self.deposit_money_btn.visible = False
    self.withdraw_money_btn.visible = True
    self.deposit_btn.visible = True
    
    

  
    

  

  
   
    
    
    

