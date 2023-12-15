import anvil
from ._anvil_designer import Borr_loan_requestTemplate
from anvil import *
import anvil.tables as tables
from anvil.tables import app_tables
from anvil import open_form

# In Borr_loan_request class

class Borr_loan_request(Borr_loan_requestTemplate):
    def __init__(self, selected_row, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Populate labels with the selected row details
        self.label_user_id.text = f"{selected_row['coustmer_id']}"
        self.label_name.text = f"{selected_row['full_name']}"
        self.label_loan_amount_applied.text = f"{selected_row['loan_amount']}"
        self.label_loan_acc_number.text = f"{selected_row['loan_id']}"
        self.label_beseem_score.text = f"{selected_row['beseem_score']}"
        self.label_loan_tenure.text = f"{selected_row['tenure']}"
        self.label_credit_limit.text = f"{selected_row['credit_limit']}"

        # Fetch additional details from the 'borrower' table
        try:
            user_request = app_tables.borrower.get(coustmer_id=str(selected_row['coustmer_id']))
            if user_request is not None:
                # Assuming 'bank_acc_details' is a valid column name in the 'borrower' table
                bank_acc_details = user_request['bank_acc_details']
                borrower_approve_date_time = user_request['borrower_approve_date_time']
                self.label_member_since.text = f"{borrower_approve_date_time}"
                self.label_bank_acc_details.text = f"{bank_acc_details}"
                
                # Fetch additional details from the 'loan_details' table
                try:
                    #loan_details = app_tables.loan_details.get(loan_id=int(selected_row['loan_id']))
                    loan_details = app_tables.loan_details.get(loan_id=str(selected_row['loan_id']))
                    if loan_details is not None:
                        # Assuming 'interest_rate' and 'min_amount' are valid column names in the 'loan_details' table
                        interest_rate = loan_details['interest_rate']
                        min_amount_text = loan_details['loan_amount']
                        
                        # Calculate and display ROM in amount format
                        rom_amount = self.calculate_rom(interest_rate,min_amount_text)
                        self.label_member_rom.text = f"{rom_amount:.2f}"
                    else:
                        self.label_member_rom.text = "No data for loan_id in loan_details"
                except anvil.tables.TableError as e:
                    self.label_member_rom.text = f"Error fetching loan details: {e}"
            else:
                self.label_bank_acc_details.text = "No data for bank_acc_details in user_request"
        except anvil.tables.TableError as e:
            self.label_bank_acc_details.text = f"Error fetching user details: {e}"

    def calculate_rom(self, interest_rate, min_amount_text):
        # Calculate ROM based on your business logic
        try:
            # Convert min_amount_text to a numeric value (assuming it's a string representing a number)
            min_amount = float(min_amount_text)

            earnings = interest_rate * min_amount

            return earnings
        except ValueError as e:
            print(f"Error converting min_amount_text to numeric: {e}")
            return 0

    def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('lendor_registration_form.dashboard.vblr')

    def button_1_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('lendor_registration_form.dashboard.vblr')




