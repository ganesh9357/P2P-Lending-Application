from ._anvil_designer import new_loan_requestTemplate
from anvil import *
import anvil.server
from .. import borrower_main_form_module as main_form_module

class new_loan_request(new_loan_requestTemplate):
    def __init__(self, **properties):
        self.user_id = main_form_module.userId
        self.init_components(**properties)

        self.max_amount_lb.text = f"200000"

    def button_1_copy_click(self, **event_args):
        loan_amount = self.min_amount_tb.text
        credit_limit = self.max_amount_lb.text
        tenure = self.tenure_dd.selected_value
        user_id = self.user_id
        
        # Check if the checkbox is checked
        if not loan_amount or not tenure:
            Notification('please fill all details')
        elif not self.check_box_1.checked:
            anvil.server.call('add_loan_details', loan_amount, credit_limit, tenure, user_id)
            Notification('Please select Terms and Conditions').show()
        else:
            open_form('bank_users.borrower_dashboard.new_loan_request.loan_type')
            
    def link_1_click(self, **event_args):
        """This method is called when the link is clicked"""
        alert('Agreements, Privacy Policy, and Applicant should accept the following: Please note that any information concealed (as what we ask for) would be construed as illegitimate action on your part and an intentional attempt to hide material information, which if found in the future, would attract necessary action(s) at your sole cost. Hence, request to be truthful to your best knowledge while sharing your details)')

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('bank_users.borrower_dashboard')
