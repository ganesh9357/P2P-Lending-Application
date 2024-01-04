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
      
      # self.userId = user_id

      # user_data=app_tables.loan_details.get(borrower_customer_id=self.userId)
      # if user_data:
      #   self.text_box_1.text=user_data['loan_amount']
      #   self.drop_down_1.text=user_data['tenure']
      #   user_data.update()
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
        one_time = self.check_box_1.checked
        monthly_emi = self.check_box_2.checked

        # Validate loan_amount
        if not loan_amount:
            self.label_22.text = "Please fill the loan amount"
            self.label_22.foreground = '#FF0000'
        elif not re.match("^[0-9]+$", loan_amount):
            self.label_22.text = "Please enter only numeric values should be in 0-9"
            self.label_22.foreground = '#FF0000'
        else:
            self.label_22.text = ""

        # Validate tenure
        if not tenure:
            self.label_23.text = "Please select tenure"
            self.label_23.foreground = '#FF0000'
        else:
            self.label_23.text = ""

        # Validate check_box_1 and check_box_2
        if not (one_time or monthly_emi):
            self.label_24.text = "Please select either One-time or Monthly EMI"
            self.label_24.foreground = '#FF0000'
        else:
            self.label_24.text = ""

        # Proceed to the next form only if all validations pass
        if loan_amount and tenure and (one_time or monthly_emi):
            open_form('bank_users.borrower_dashboard.new_loan_request.check_out_form', self.proctct_g, self.prodct_cate, self.loan_amount_tb.text, self.tenure_dd.selected_value, self.user_id)

    def fetch_product_data(self):
        return app_tables.product_details.search(
            product_group=self.proctct_g,
            product_categories=self.prodct_cate
        )

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

    def check_box_2_change(self, **event_args):
        if self.check_box_2:
            self.tenure_dd.visible = True
            self.label_3.visible = True
