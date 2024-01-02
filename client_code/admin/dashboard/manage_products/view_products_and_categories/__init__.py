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
    self.refresh_data_button_click()

    # Any code you write here will run before the form opens.
  def refresh_data_button_click(self, **event_args):
        # Fetch data directly from the database
        categories = app_tables.product_categories.search()
        
        # Clear existing items in the repeating panel
        self.repeating_panel_1.items = []
        
        # Populate the repeating panel with fetched data
        for category in categories:
            self.repeating_panel_1.add_component(ui.Label(text=category['name_group']), 
                                                ui.Label(text=category['name_categories']))