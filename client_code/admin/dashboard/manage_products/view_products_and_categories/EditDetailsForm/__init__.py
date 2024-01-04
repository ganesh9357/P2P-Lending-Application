from ._anvil_designer import EditDetailsFormTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class EditDetailsForm(EditDetailsFormTemplate):
    def __init__(self, selected_group, selected_category, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Set the initial values for the input components
        self.text_box_1.text = selected_group
        self.text_box_2.text = selected_category

    def button_1_click(self, **event_args):
        """Save changes button click event"""
        # Get the updated values from the input components
        updated_group = self.text_box_group.text
        updated_category = self.text_box_category.text

        # Perform any validation or data processing as needed

        # Update the existing row in the product_categories table
        selected_item = self.item  # Assuming you passed the selected item to this form
        if selected_item is not None:
            selected_item['name_group'] = updated_group
            selected_item['name_categories'] = updated_category

        # Optionally, show a confirmation message
        alert("Changes saved successfully!")

        # Close the form after saving changes
        self.close()

    def button_2_click(self, **event_args):
        """Cancel button click event"""
        # Close the form without saving changes
        self.close()

  
