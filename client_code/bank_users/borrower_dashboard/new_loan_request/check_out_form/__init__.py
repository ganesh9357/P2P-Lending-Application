from ._anvil_designer import check_out_formTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import borrower_main_form_module as main_form_module
class check_out_form(check_out_formTemplate):
  def __init__(self, **properties):
        # Initialize self.names as an instance variable
        self.names = 'k-12 education loan'

        # Initialize self.interest_rate as an instance variable
        self.interest_rate = None

        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        user_request = app_tables.product_borrower.get(name=self.names)

        if user_request:
            self.interest_rate = user_request['interest_rate']
            self.int_rate.text = f"Interest rate : {self.interest_rate} %"
        else:
            self.int_rate.text = "Interest rate not found."
            return  # Exit the __init__ method if interest_rate is not available

        all_requests = app_tables.loan_details.search()

        if all_requests:
            most_recent_request = None

            for request in all_requests:
                if most_recent_request is None or request['timestamp'] > most_recent_request['timestamp']:
                    most_recent_request = request

            self.customer_id = most_recent_request['coustmer_id']
            loan_amount = most_recent_request['loan_amount']
            tenure = most_recent_request['tenure']
            credit_limit = most_recent_request['credit_limit']

            # Check if values are non-empty strings before converting
            if loan_amount and tenure and credit_limit:
                loan_amount = int(loan_amount)
                tenure = int(tenure)
                credit_limit = int(credit_limit)

                

                P = int(loan_amount)
                r = int(self.interest_rate) / 12 / 100
                n = int(tenure)

                emi = P * r * (1 + r)**n / ((1 + r)**n - 1)
                emi = int(emi)
                self.emi_details.text = f"EMI Details: {emi}"
                processing_fee_percentage = 1
                processing_fee = loan_amount * (processing_fee_percentage / 100)
                processing_fee = int (processing_fee)
                self.pro_fee.text = f"Processing fee : {processing_fee}"
                total_repayment_amount = (emi * tenure) + processing_fee
                total_repayment_amount = int(total_repayment_amount)
                self.trp_amount.text = f"Total Repayment Amount : {total_repayment_amount}"
                emi = emi
                interest_rate = self.interest_rate
                total_repayment_amount = total_repayment_amount 
                
            else:
                self.trp_amount.text = "Invalid loan details."
        else:
            self.trp_amount.text = "No user profile data available."
         
  def submit_click(self, **event_args):
      
      
      
      alert('your request is submitted')
      open_form('bank_users.borrower_dashboard')

  def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('bank_users.borrower_dashboard.new_loan_request.k12_loan')

  def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('bank_users.borrower_dashboard')

