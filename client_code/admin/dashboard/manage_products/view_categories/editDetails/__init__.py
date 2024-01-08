from ._anvil_designer import editDetailsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class editDetails(editDetailsTemplate):
    def __init__(self, selected_row, **properties):
        self.init_components(**properties)

        # Set the initial values for the input components
        self.text_box_1.text = selected_row['name_group']
        self.text_box_1.enabled = False  # Make text_box_1 non-editable

        self.text_box_2.text = selected_row['name_categories']
        self.text_box_2.enabled = True  # Make text_box_2 editable
        
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
            open_form('admin.dashboard.manage_products.view_categories')
      
    def button_2_click(self, **event_args):
        """Cancel button click event"""
        # Close the form without saving changes
        open_form('admin.dashboard.manage_products.view_categories')


    def delete_click(self, **event_args):
        """This method is called when the Delete button is clicked"""
        # Check if the user confirms the deletion
        if confirm("Are you sure you want to delete this item?"):
            # Delete the row directly on the client side
            self.selected_row.delete()
            
            # Optionally, navigate to a different form or perform other actions
            open_form('admin.dashboard.manage_products.view_categories')

    def home_button(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('admin.dashboard')
