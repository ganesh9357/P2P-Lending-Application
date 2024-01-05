from ._anvil_designer import loan_typeTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import borrower_main_form_module as main_form_module
import re

class loan_type(loan_typeTemplate):
    def __init__(self, product_group, product_cat, **properties):
        self.user_id = main_form_module.userId
        self.proctct_g = product_group
        self.prodct_cate = product_cat
        self.init_components(**properties)

    def button_1_click(self, **event_args):
        open_form('bank_users.borrower_dashboard')

    def button_2_click(self, **event_args):
        open_form('bank_users.borrower_dashboard.new_loan_request')

    def button_3_click(self, **event_args):
        loan_amount = self.loan_amount_tb.text
        tenure = self.tenure_dd.selected_value
        one_time = self.radio_button_1.selected
        monthly_emi = self.radio_button_2.selected
    
        # Validate loan_amount
        if not loan_amount:
            self.label_22.text = "Please fill the loan amount"
            self.label_22.foreground = '#FF0000'
        elif not loan_amount.isdigit():
            self.label_22.text = "Please enter only numeric values (0-9) for loan amount"
            self.label_22.foreground = '#FF0000'
        else:
            min_amount, max_amount = self.get_min_max_amount()
            loan_amount = int(loan_amount)
    
            if min_amount <= loan_amount <= max_amount:
                self.label_22.text = ""
            else:
                self.label_22.text = f"Loan amount should be between {min_amount} and {max_amount}"
                self.label_22.foreground = '#FF0000'
    
        # Validate tenure
        if not tenure:
            self.label_23.text = "Please select tenure"
            self.label_23.foreground = '#FF0000'
        else:
            self.label_23.text = ""
    
        # Validate radio_button_1 and radio_button_2
        if not (one_time or monthly_emi):
            self.label_24.text = "Please select either One-time or Monthly EMI"
            self.label_24.foreground = '#FF0000'
        else:
            self.label_24.text = ""
    
        # Proceed to the next form only if all validations pass
        if not any([self.label_22.text, self.label_23.text, self.label_24.text]):
            open_form('bank_users.borrower_dashboard.new_loan_request.check_out_form', self.proctct_g, self.prodct_cate, str(loan_amount), tenure, self.user_id)

    def fetch_product_data(self):
        return app_tables.product_details.search(
            product_group=self.proctct_g,
            product_categories=self.prodct_cate
        )

    def get_min_max_amount(self):
        product_data = self.fetch_product_data()
        if product_data:
            min_amount = product_data[0]['min_amount']
            max_amount = product_data[0]['max_amount']
            return min_amount, max_amount
        return 0, 0

    def display_label_text(self, label, column_name):
        product_data = self.fetch_product_data()
        if product_data:
            label_text = [str(data[column_name]) for data in product_data]
            label.text = label_text[0] if label_text else None

    def label_11_show(self, **event_args):
        self.display_label_text(self.label_11, 'max_amount')

    def label_5_show(self, **event_args):
        self.display_label_text(self.label_5, 'min_amount')

    def label_13_show(self, **event_args):
        self.display_label_text(self.label_13, 'min_tenure')

    def label_15_show(self, **event_args):
        self.display_label_text(self.label_15, 'max_tenure')

    def label_21_show(self, **event_args):
        self.display_label_text(self.label_21, 'processing_fee')

    def label_7_show(self, **event_args):
        self.display_label_text(self.label_7, 'roi')

    def label_9_show(self, **event_args):
        self.display_label_text(self.label_9, 'foreclose_type')

    def label_18_show(self, **event_args):
        self.display_label_text(self.label_18, 'membership_type')
