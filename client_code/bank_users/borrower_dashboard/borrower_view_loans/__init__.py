from ._anvil_designer import borrower_view_loansTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import borrower_main_form_module as main_form_module
class borrower_view_loans(borrower_view_loansTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_id=main_form_module.userId
    self.repeating_panel_1.items=app_tables.loan_details.search(loan_updated_status=q.like('open%'),coustmer_id=self.user_id)
    self.repeating_panel_2.items=app_tables.loan_details.search(loan_updated_status=q.like('close%'),coustmer_id=self.user_id)
    self.repeating_panel_3.items=app_tables.loan_details.search(loan_updated_status=q.like('reject%'),coustmer_id=self.user_id)
    self.repeating_panel_4.items=app_tables.loan_details.search(loan_updated_status=q.like('underprocess%'),coustmer_id=self.user_id)
    self.repeating_panel_5.items=app_tables.loan_details.search(loan_updated_status=q.like('foreclosure%'),coustmer_id=self.user_id)
    self.label_5.text = str(len(self.repeating_panel_1.items))
    self.label_6.text=str(len(self.repeating_panel_2.items))
    self.label_7.text=str(len(self.repeating_panel_3.items))
    self.label_8.text=str(len(self.repeating_panel_4.items))
    self.label_9.text=str(len(self.repeating_panel_5.items))
    # Any code you write here will run before the form opens.

  def home_borrower_registration_form_copy_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_dashboard')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_1.visible=True
    self.label_2.visible=False
    self.label_3.visible=False
    self.label_4.visible=False
    self.label_10.visible=False
    self.data_grid_1.visible=True
    self.data_grid_2.visible=False
    self.data_grid_3.visible=False
    self.data_grid_4.visible=False
    self.data_grid_5.visible=False
    
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_1.visible=False
    self.label_2.visible=True
    self.label_3.visible=False
    self.label_4.visible=False
    self.label_10.visible=False
    self.data_grid_1.visible=False
    self.data_grid_2.visible=True
    self.data_grid_3.visible=False
    self.data_grid_4.visible=False
    self.data_grid_5.visible=False

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_1.visible=False
    self.label_2.visible=False
    self.label_3.visible=True
    self.label_4.visible=False
    self.label_10.visible=False
    self.data_grid_1.visible=False
    self.data_grid_2.visible=False
    self.data_grid_3.visible=True
    self.data_grid_4.visible=False
    self.data_grid_5.visible=False

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_1.visible=False
    self.label_2.visible=False
    self.label_3.visible=False
    self.label_4.visible=True
    self.label_10.visible=False
    self.data_grid_1.visible=False
    self.data_grid_2.visible=False
    self.data_grid_3.visible=False
    self.data_grid_4.visible=True
    self.data_grid_5.visible=False

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_1.visible=False
    self.label_2.visible=False
    self.label_3.visible=False
    self.label_4.visible=False
    self.label_10.visible=True
    self.data_grid_1.visible=False
    self.data_grid_2.visible=False
    self.data_grid_3.visible=False
    self.data_grid_4.visible=False
    self.data_grid_5.visible=True
