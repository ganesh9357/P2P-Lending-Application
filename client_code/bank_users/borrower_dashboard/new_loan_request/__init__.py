from ._anvil_designer import new_loan_requestTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import borrower_main_form_module as main_form_module

class new_loan_request(new_loan_requestTemplate):
    def __init__(self, **properties):
        self.user_id = main_form_module.userId
        self.init_components(**properties)

        options = app_tables.product_group.search()
        option_strings = [''] + [option['name'] for option in options]
        self.name.items = option_strings
        self.name.selected_value = None  # Set to None initially, as there is no default selection

        # Add a placeholder to drop_down_2
        self.drop_down_2.items = ['']  # Add your placeholder text here
        self.drop_down_2.selected_value = None

    def name_change(self, **event_args):
        self.selected_value = self.name.selected_value

        if self.selected_value:
            self.label_1.visible = True
            self.label_2.visible = True
            self.name.visible = True
            self.drop_down_2.visible = True
            self.label_4.visible = True

            # Fetch product categories based on the selected loan type
            product_categories = app_tables.product_categories.search(
                name_group=self.name.selected_value
            )

            if product_categories:
                # Display product categories in drop_down_2
                self.drop_down_2.items = [''] + [category['name_categories'] for category in product_categories]
                self.drop_down_2.selected_value = None

    def button_2_click(self, **event_args):
        open_form('bank_users.borrower_dashboard')

    def button_1_copy_click(self, **event_args):
        name = self.name.selected_value
        category = self.drop_down_2.selected_value

        if not name:
            self.label_3.text = "Please select a product group"
            self.label_3.foreground = '#FF0000'
        else:
            self.label_3.text = ""

        if not category or category == '':
            self.label_4.text = "Please select a category"
            self.label_4.foreground = '#FF0000'
        else:
            self.label_4.text = ""

        if name and (category and category != ''):
            open_form('bank_users.borrower_dashboard.new_loan_request.loan_type', name, category)

    def max_amount_lb_show(self, **event_args):
        data = app_tables.product_details.search()
        data1_strings = [data['max_amount'] for data in data]
        self.max_amount_lb.text = data1_strings[0] if data1_strings else None
