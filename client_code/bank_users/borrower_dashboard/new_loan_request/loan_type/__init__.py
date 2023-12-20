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

class loan_type(loan_typeTemplate):
    def __init__(self, **properties):
        self.user_id = main_form_module.userId
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    #     # Manually fetch loan data and populate the dropdowns
    #     self.populate_loan_types()
    #     self.populate_product_categories()

    #     Any code you write here will run before the form opens.

    # def populate_loan_types(self):
    #     # Manually fetch loan types from the 'product_group' table
    #     loan_types = app_tables.product_group.search()

    #     # # Populate the dropdown with fetched loan types
    #     if loan_types:
    #         self.drop_down_1.items = [loan['name'] for loan in loan_types]
    #         self.drop_down_1.selected_value = loan_types[0]['name']  # Set the default selection


    # def populate_product_categories(self):
    #     # Manually fetch product categories from the 'product_category' table
    #     categories = app_tables.product_categories.search()

    #     # Populate the product categories dropdown with fetched categories
    #     if categories:
    #         self.drop_down_2.items = [category['name_group'] for category in categories]
    #         self.drop_down_2.selected_value = categories[0]['name_group']  # Set the default selection

    #     # Automatically select the first item in drop_down_1 to trigger the change event
    #     self.drop_down_1.include_placeholder=self.get_components()
        

    # def drop_down_1_change(self, **event_args):
    #     selected_value = self.drop_down_1.selected_value

    #     if selected_value:
    #         self.label_1.visible = False
    #         self.label_3.visible = True
    #         self.drop_down_1.visible = True
    #         self.drop_down_2.visible = True

    #         # Fetch product categories based on the selected loan type
    #         product_categories = app_tables.product_categories.search(
    #             name_group=selected_value
    #         )

    #         if product_categories:
    #             # Display product categories in drop_down_2
    #             self.drop_down_2.items = [category['name_categories'] for category in product_categories]
    #             self.drop_down_2.selected_value = product_categories[0]['name_categories'] if product_categories else None

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('bank_users.borrower_dashboard')

    def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('bank_users.borrower_dashboard.new_loan_request')

    def button_3_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('bank_users.borrower_dashboard.new_loan_request.check_out_form')

    def label_11_show(self, **event_args):
      """This method is called when the Label is shown on the screen"""
      data =app_tables.product_details.search()
      data1_strings = [data['max_amount'] for data in data]
      self.label_11.text = data1_strings
      self.label_11.text = data1_strings if data1_strings else None

    def label_5_show(self, **event_args):
      """This method is called when the Label is shown on the screen"""
      min_amt =app_tables.product_details.search()
      min_amount = [min_amt['min_amount'] for min_amt in min_amt]
      self.label_5.text = min_amount
      self.label_5.text = min_amount if min_amount else None

    def label_13_show(self, **event_args):
      min_ten = app_tables.product_details.search()
      min_tenure = [min_ten['min_tenure'] for min_ten in min_ten]
      self.label_13.text = min_tenure
      self.label_13.text = min_tenure if min_tenure else None

    def label_15_show(self, **event_args):
      max_ten = app_tables.product_details.search()
      max_tenure = [max_ten['max_tenure'] for max_ten in max_ten]
      self.label_15.text = max_tenure
      self.label_15.text = max_tenure if max_tenure else None

    def label_21_show(self, **event_args):
      process_fee = app_tables.product_details.search()
      processing_fee = [process_fee['processing_fee'] for process_fee in process_fee]
      self.label_21.text = processing_fee
      self.label_21.text = processing_fee if processing_fee else None

    def label_7_show(self, **event_args):
      int_rate = app_tables.product_details.search()
      interest_rate = [int_rate['roi'] for int_rate in int_rate]
      self.label_7.text = interest_rate
      self.label_7.text = interest_rate if interest_rate else None

    def label_9_show(self, **event_args):
      forclos_eligibility = app_tables.product_details.search()
      forclosure_eligibility = [forclos_eligibility['foreclose_type'] for forclos_eligibility in forclos_eligibility]
      self.label_9.text = forclosure_eligibility
      self.label_9.text = forclosure_eligibility if forclosure_eligibility else None
      
      


      
      
      
      
