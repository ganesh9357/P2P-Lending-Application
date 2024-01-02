from ._anvil_designer import view_products_and_categoriesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class view_products_and_categories(view_products_and_categoriesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = app_tables.product_categories.search()

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.manage_products')

  