from ._anvil_designer import Lender_reg_form_1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime

class Lender_reg_form_1(Lender_reg_form_1Template):
    def __init__(self, user_id, **properties):
        self.userId = user_id
        user_data = anvil.server.call('get_user_data', user_id)
        
        if user_data:
            self.full_name = user_data.get('full_name', '')
            self.gender = user_data.get('gender', '')
            self.date_of_birth = user_data.get('date_of_birth', datetime.now())
        else:
            self.full_name = ''
            self.gender = ''
            self.date_of_birth = datetime.now()

        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Restore previously entered data if available
        if self.full_name:
            self.text_box_1.text = self.full_name
        if self.gender:
            self.drop_down_1_copy_1.selected_value = self.gender
            self.date_picker_1.date = self.date_of_birth

    # next page form 2
    def button_2_click(self, **event_args):
        full_name = self.text_box_1.text
        gender = self.drop_down_1_copy_1.selected_value
        date_of_birth = self.date_picker_1.date
        user_id = self.userId

        if not full_name or not gender or not date_of_birth:
            Notification("Please fill all required fields").show()
        else:
            # Calculate age based on the selected date of birth
            today = datetime.now()
            age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

            if age >= 18:
                anvil.server.call('add_lendor_frist_form', full_name, gender, date_of_birth, user_id)
                open_form('lendor_registration_form.Lender_reg_form_2', user_id=user_id)
            else:
                Notification("You are not eligible. Age must be 18 or above").show()
                return

