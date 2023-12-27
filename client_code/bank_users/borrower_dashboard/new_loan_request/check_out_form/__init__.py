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
  def __init__(self, product_group, product_cat, **properties):
        self.proctct_g = product_group
        self.prodct_cate = product_cat
        self.init_components(**properties)

         
  def submit_click(self, **event_args):
      alert('your request is submitted')
      open_form('bank_users.borrower_dashboard')

  def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('bank_users.borrower_dashboard.new_loan_request.k12_loan')

  def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('bank_users.borrower_dashboard')

  
  def fetch_product_data(self):
        return app_tables.product_details.search(
            product_name=self.proctct_g,
            product_categories=self.prodct_cate
        )

  def display_label_text(self, label, column_name):
        product_data = self.fetch_product_data()
        if product_data:
            label_text = [str(data[column_name]) for data in product_data]
            label.text = label_text[0] if label_text else None

  def label_4_show(self, **event_args):
    self.display_label_text(self.label_4, 'roi')

