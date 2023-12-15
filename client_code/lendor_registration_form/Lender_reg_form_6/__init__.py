from ._anvil_designer import Lender_reg_form_6Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_form_6(Lender_reg_form_6Template):
    def __init__(self, user_id, **properties):
        self.userId = user_id
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Initialize variables
        lending_type = None
        investment = None
        lending_period = None

        # Search for user_data in the lender table
        user_data = app_tables.lender.search(coustmer_id=user_id)

        if user_data and len(user_data) > 0:
            lending_type = user_data[0]['lending_type']
            investment = user_data[0]['investment']
            lending_period = user_data[0]['lending_period']

        # Set selected values for dropdowns
        if lending_type:
            self.lending_type_dropdown.selected_value = lending_type
        if investment:
            self.text_box_1.text = investment  # No need to convert to string
        if lending_period:
            self.drop_down_2.selected_value = lending_period

        # Any code you write here will run before the form opens.

    def button_1_click(self, **event_args):
        open_form('lendor_registration_form.Lender_reg_form_5', user_id=self.userId)

    def button_2_click(self, **event_args):
        lending_type = self.lending_type_dropdown.selected_value
        investment = self.text_box_1.text
        lending_period = self.drop_down_2.selected_value
        user_id = self.userId

        # Check if user_data is not empty before accessing its elements
        if lending_type and investment and lending_period:
            # Search for existing user data in the lender table
            user_data = app_tables.lender.search(coustmer_id=user_id)

            if user_data and len(user_data) > 0:
                # If the row exists, update the existing row
                user_row = user_data[0]
                user_row['lending_type'] = lending_type
                user_row['investment'] = str(investment)
                user_row['lending_period'] = lending_period
                user_row['membership'] = self.calculate_membership(float(investment))
                user_row.update()
            else:
                # If the row doesn't exist, add a new row
                app_tables.lender.add_row(coustmer_id=user_id, lending_type=lending_type, investment=str(investment), lending_period=lending_period, membership=self.calculate_membership(float(investment)))

            if lending_type == 'Individual':
                open_form('lendor_registration_form.Lender_reg_individual_form_1', user_id=user_id)
            elif lending_type == 'Institutional':
                open_form('lendor_registration_form.Lender_reg_Institutional_form_1', user_id=user_id)

    def button_3_click(self, **event_args):
        open_form("bank_users.user_form")

    # Function to calculate membership based on investment
    def calculate_membership(self, investment):
        if investment <= 500000:
            return 'Silver'
        elif investment <= 1000000:
            return 'Gold'
        else:
            return 'Platinum'
