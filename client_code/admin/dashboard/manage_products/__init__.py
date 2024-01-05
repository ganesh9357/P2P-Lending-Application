from ._anvil_designer import manage_productsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class manage_products(manage_productsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.manage_products.manage_producs1')

  def button_1_copy_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.manage_products.view_product')

  def button_1_copy_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.manage_products.add_group')

  def button_1_copy_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard')

  def button_1_copy_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.manage_products.view_products_and_categories')

  def button_1_copy_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.manage_products.view_categories')






 
 

