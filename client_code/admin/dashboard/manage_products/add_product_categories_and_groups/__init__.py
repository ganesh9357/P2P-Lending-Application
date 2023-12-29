from ._anvil_designer import add_product_categories_and_groupsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class add_product_categories_and_groups(add_product_categories_and_groupsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    options = app_tables.product_group.search()
    option_strings = [option['name'] for option in options]
    self.drop_down_1.items = option_strings
    self.drop_down_1.selected_value = option_strings[0] if option_strings else None   


  def name_change(self, **event_args):
        self.selected_value = self.drop_down_1.selected_value

        if self.selected_value:
          self.label_1.visible = True
          self.label_2.visible = True
          self.drop_down_1.visible = True
          self.drop_down_2.visible = True

            # Fetch product categories based on the selected loan type
          product_categories = app_tables.product_categories.search(
          name_group=self.selected_value
          )

          if product_categories:
            # Display product categories in drop_down_2
            self.drop_down_2.items = [category['name_categories'] for category in product_categories]
            self.drop_down_2.selected_value = product_categories[0]['name_categories'] if product_categories else None

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_products')
    
  def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        # Get selected values
        selected_group = self.drop_down_1.selected_value
        selected_category = self.drop_down_2.selected_value

        # Check if both values are selected
        if selected_group and selected_category:
            # Create a new row in the product_details table and set the values
            app_tables.product_details.add_row(
                product_name=selected_group,
                product_categories=selected_category
            )

            # Optionally, you can show a confirmation message
            alert("Product details saved successfully!")

            # Navigate to the manage_products form
            open_form('admin.dashboard.manage_products')
        else:
            # Show an error message if one or both values are not selected
            alert("Please select both product group and product category before saving.")