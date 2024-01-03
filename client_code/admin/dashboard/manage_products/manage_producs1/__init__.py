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

        options = app_tables.product_group.search()
        option_strings = [option['name'] for option in options]
        self.name.items = option_strings
        self.name.selected_value = option_strings[0] if option_strings else None  
          
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
          
    def name_change(self, **event_args):
      self.label_3_copy.visible = True
      self.label_5.visible = True
      self.name.visible = True
      self.product_category.visible = True
      self.selected_value = self.name.selected_value
      print(f"Selected Value: {self.selected_value}")
        
      if self.selected_value:
            # Fetch product categories based on the selected loan type
        product_categories = app_tables.product_categories.search(
        name_group = self.selected_value
        )
        print(f"Product Categories: {product_categories}")

        if product_categories:
            # Display product categories in drop_down_2
          category_names = [category['name_categories'] for category in product_categories]
          print(f"Category Names: {category_names}")
          self.product_category.items = category_names
          self.product_category.selected_value = category_names[0] if category_names else None
   
            

    def link_1_copy_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form('admin.dashboard.manage_products')

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""      
        product_name = self.product_name.text
        product_group = self.name.selected_value
        product_discription = self.text_area_1.text
        product_categories = self.product_category.selected_value
        processing_fee = float(self.text_box_3.text)
        extension_fee = float(self.text_box_4.text)
        membership_type = self.drop_down_2.selected_value
        if self.radio_button_1.selected:
            interest_type = self.radio_button_1.text
        else:
            interest_type = self.radio_button_2.text
        min_amount = int(self.min_amount.text)
        max_amount = int(self.max_amount.text)
        min_tenure = int(self.min_tenure.text)
        max_tenure = int(self.max_tenure.text)
        roi = int(self.text_box_5.text)
        foreclose_type = self.foreclose_type.selected_value
        foreclosure_fee = int(self.foreclosure_fee.text)      
        extension_allowed = self.extension_allowed.selected_value
        emi_payment = self.drop_down_1.selected_value
        if self.radio_button_3.selected:
            # Code to execute when radio_button_3 is selected
            discount_coupons = self.radio_button_3.text
        elif self.radio_button_4.selected:
            # Code to execute when radio_button_4 is selected
            discount_coupons = self.radio_button_4.text
        else:
            # Code to execute when neither radio_button_3 nor radio_button_4 is selected
            discount_coupons = None  # or any default value

        if product_group == ""  or product_name == "" or product_categories== "" or membership_type == "" or processing_fee == "" or extension_fee == "" or interest_type == "" or max_amount == "" or min_amount == "" or min_tenure == "" or max_tenure == "" or roi == "" or emi_payment == "" or discount_coupons == "":
            Notification("Fill All Required Details").show()
        else:
            anvil.server.call('product_details', self.id, product_group, product_name, product_discription, product_categories, processing_fee, extension_fee, membership_type, interest_type, max_amount, min_amount, min_tenure, max_tenure, roi, foreclose_type, foreclosure_fee, extension_allowed, emi_payment, discount_coupons)
            product_id = self.label_1.text
            # open_form('admin.dashboard.manage_products.add_group',product_id )

            Notification("Products added successfully").show()
            open_form('admin.dashboard.manage_products')

  