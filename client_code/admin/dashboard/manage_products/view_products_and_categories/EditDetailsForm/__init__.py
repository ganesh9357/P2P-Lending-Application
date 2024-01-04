from ._anvil_designer import EditDetailsFormTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import alert

class EditDetailsForm(EditDetailsFormTemplate):
    def __init__(self, selected_row, **properties):
        self.init_components(**properties)

        # Set the initial values for the input components
        self.text_box_1.text = selected_row['name_group']
        self.text_box_2.text = selected_row['name_categories']
        
        # Store the selected row for later use
        self.selected_row = selected_row

    def button_1_click(self, **event_args):
        """Save changes button click event"""
        # Get the updated values from the input components
        updated_group = self.text_box_1.text
        updated_category = self.text_box_2.text

        # Update the existing row in the product_categories table
        if self.selected_row is not None:
            self.selected_row['name_group'] = updated_group
            self.selected_row['name_categories'] = updated_category

            # Save changes to the database
            self.selected_row.update()

            alert("Changes saved successfully!")
            open_form('admin.dashboard.manage_products.view_products_and_categories')
      
    def button_2_click(self, **event_args):
        """Cancel button click event"""
        # Close the form without saving changes
        open_form('admin.dashboard.manage_products.view_products_and_categories')
