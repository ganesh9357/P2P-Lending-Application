from ._anvil_designer import manage_producs1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class manage_producs1(manage_producs1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Fetch data from product_group table and populate the name dropdown
        product_group_options = app_tables.product_group.search()
        self.name.items = [option['name'] for option in product_group_options]

        # Fetch data from product_group table and populate the name dropdown
        product_group_options = app_tables.product_categories.search()
        self.product_category.items = [option['namw'] for option in product_group_options]

        # Any code you write here will run before the form opens.
        self.id = 'PD' + str(1000)  
        self.label_1.text = self.id
        self.data = tables.app_tables.product_details.search()

        a = -1
        self.list_1 = []

        for i in self.data:
            a += 1
            self.list_1.append(i['product_id']) 
        if a == -1:
            self.id = 'PD' + str(1000)
            self.label_1.text = self.id
        else:
            last_product_id = self.list_1[-1]
            numeric_part = last_product_id[2:]  # Assuming the prefix is always two characters ('PD')
            self.id = 'PD' + str(int(numeric_part) + 1)
            self.label_1.text = self.id

    def link_1_copy_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form('admin.dashboard.manage_products')

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""

        

        product_name = self.name.selected_value
        product_discription = self.text_area_1.text
        product_categories = self.product_category.selected_value
        processing_fee = int(self.text_box_3.text)
        extension_fee = int(self.text_box_4.text)
        membership_type = self.drop_down_2.selected_value
        print(membership_type)
        interest_type = self.radio_button_1.text
        if interest_type:
            print(self.radio_button_1.text)
        else:
            print(self.radio_button_2.text)
        min_amount = int(self.min_amount.text)
        print(min_amount)
        max_amount = int(self.max_amount.text)
        print(max_amount)
        min_tenure = int(self.min_tenure.text)
        max_tenure = int(self.max_tenure.text)
        roi = int(self.text_box_5.text)
        print(roi)
        foreclose_type = self.foreclose_type.selected_value
        extension_allowed_mapping = {
    'Yes': True,
    'No': False,
}
        extension_allowed = extension_allowed_mapping.get(self.extension_allowed.selected_value, False)
        emi_payment = self.drop_down_1.selected_value
        print(emi_payment)
        discount_coupons = self.radio_button_3.text
        if discount_coupons:
          print(self.radio_button_3.text)
        else:
          print(self.radio_button_4.text)

        if product_name == "" or product_categories== "" or membership_type == "" or processing_fee == "" or extension_fee == "" or interest_type == "" or max_amount == "" or min_amount == "" or min_tenure == "" or max_tenure == "" or roi == "" or emi_payment == "" or discount_coupons == "":
            Notification("Fill All Required Details").show()
        else:
            anvil.server.call('product_details', self.id, product_name, product_categories, processing_fee, extension_fee, membership_type, interest_type, max_amount, min_amount, min_tenure, max_tenure, roi, foreclose_type, extension_allowed, emi_payment, discount_coupons)
            product_id = self.label_1.text
            # open_form('admin.dashboard.manage_products.add_group',product_id )

  