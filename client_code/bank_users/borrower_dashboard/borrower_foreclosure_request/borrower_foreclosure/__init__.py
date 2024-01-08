from ._anvil_designer import borrower_foreclosureTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime

class borrower_foreclosure(borrower_foreclosureTemplate):
    def __init__(self, selected_row, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.label_loan_id.text = f"{selected_row['loan_id']}"
        self.label_name.text = f"{selected_row['borrower_full_name']}"
        self.label_loan_amount.text = f"{selected_row['loan_amount']}"
        self.label_loan_tenure.text = f"{selected_row['tenure']} Months"
        self.label_interest_rate.text = f"{selected_row['interest_rate']} % pa"
        self.label_credit_limit.text = f"{selected_row['credit_limit']}"
        self.label_3.text = "Foreclosure Request Under Process......"  
        self.label_5.text = "Foreclosure Request Rejected"

        # Check foreclosure status for the selected loan ID
        loan_id = selected_row['loan_id']
        foreclosure_rows = app_tables.foreclosure.search(loan_id=loan_id)

        approved_status = False
        rejected_status = False

        for row in foreclosure_rows:
            if row['status'] == 'approved':
                approved_status = True
                break
            elif row['status'] == 'reject':
                rejected_status = True
                break

        if approved_status:
            # If there is an approved status, make "Pay" button visible
            self.button_foreclose.visible = False
            self.button_2.visible = False
            self.button_3.visible = True
            self.button_4.visible = True
        elif rejected_status:
            # If there is a reject status, show an alert
            alert('Your request has been rejected.')
            self.button_foreclose.visible = False
            self.button_2.visible = False
            self.button_3.visible = False
            self.label_5.visible = True
            self.button_5.visible = True
        else:
            # If there is no approved or reject status, check if the loan ID is in foreclosure table
            existing_requests = app_tables.foreclosure.search(loan_id=loan_id)
            if len(existing_requests) == 0:
                # If the loan ID is not in the foreclosure table, make "Foreclose" button and button2 visible
                self.button_foreclose.visible = True
                self.button_2.visible = True
                self.button_3.visible = False
                self.button_4.visible = False
                
            else:
                # If the loan ID is in the foreclosure table, make other buttons visible
                self.button_foreclose.visible = False
                self.button_2.visible = False 
                self.button_4.visible = False
                self.button_3.visible = False
                self.label_3.visible = True
                self.button_5.visible = True

        # Save selected_row as an instance variable for later use
        self.selected_row = selected_row

        # Calculate months_difference
        loan_details_row = app_tables.loan_details.get(loan_id=loan_id)
        borrower_last_payment_done = selected_row['borrower_last_payment_done']
        borrower_first_payment_done = loan_details_row['borrower_first_payment_done']
        product_id = selected_row['product_id']
        product_details_row = app_tables.product_details.get(product_id=product_id)
        self.min_months = product_details_row['min_months']
        self.min_months = int(self.min_months)

        # Calculate the difference in months between first and last payments
        self.months_difference = self.calculate_month_difference(borrower_first_payment_done, borrower_last_payment_done)
        self.months_difference = int(self.months_difference)

        # Set the label text
        self.label_tpm.text = f"{self.months_difference} months"

        # Check if a row with the given loan_id exists
        rows = app_tables.loan_details.search(loan_id=loan_id)

        if rows:
            # If the row exists, get the first one (assuming loan_id is unique)
            loan_details_row = rows[0]
        else:
            # If the row does not exist, create a new one
            loan_details_row = app_tables.loan_details.add_row(loan_id=loan_id)
        
        # Add months_difference to the loan_details table
        loan_details_row['total_payments_made'] = self.months_difference
        
        # Update the row
        loan_details_row.update()


    def button_foreclose_click(self, **event_args):
        selected_row = self.selected_row
        loan_id = selected_row['loan_id']

        if  self.months_difference >= self.min_months:
              open_form('bank_users.borrower_dashboard.borrower_foreclosure_request.borrower_foreclosure.foreclose', selected_row=selected_row)
        else:
              alert('You are not eligible for foreclosure! You have to pay at least 12 months.')
              open_form('bank_users.borrower_dashboard.borrower_foreclosure_request')

        # Rest of the button_foreclose_click code...

    @staticmethod
    def calculate_month_difference(start_date, end_date):
        months_difference = (end_date.year - start_date.year) * 12 + end_date.month - start_date.month
        return months_difference

    def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('bank_users.borrower_dashboard.borrower_foreclosure_request')

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('bank_users.borrower_dashboard')

    def button_4_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('bank_users.borrower_dashboard.borrower_foreclosure_request')

    def button_5_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('bank_users.borrower_dashboard.borrower_foreclosure_request')

