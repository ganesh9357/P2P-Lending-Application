from ._anvil_designer import edit_formTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class edit_form(edit_formTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        self.data = tables.app_tables.product_details.search()

        # Fetch data from product_group table and populate the name dropdown
        product_group_options = app_tables.product_group.search()
        self.name.items = [option['name'] for option in product_group_options]

        # Fetch data from product_group table and populate the name dropdown
        product_group_options = app_tables.product_categories.search()
        self.product_category.items = [option['name_categories'] for option in product_group_options]

        self.id_list = []
        self.name_list = []
        self.product_categorys = []
        self.discri_list = []
        self.profee_list = []
        self.extfee_list = []
        self.foreclosure_type_list = []
        self.extension_allowed_list = []
        self.type_list = []
        self.intr_type = []
        self.roi_list = []
        self.min_amount_list = []
        self.max_amount_list = []
        self.min_tenure_list = []
        self.max_tenure_list = []
        self.emi_payment_list = []
        self.disc_coupans_list = []

        a = -1
        for i in self.data:
            a += 1
            self.id_list.append(i['product_id'])
            self.name_list.append(i['product_name'])
            self.discri_list.append(i['product_discription'])
            self.product_categorys.append(i['product_categories'])
            self.profee_list.append(i['processing_fee'])
            self.extfee_list.append(i['extension_fee'])
            self.foreclosure_type_list.append(i['foreclose_type'])
            self.extension_allowed_list.append(i['extension_allowed'])
            self.type_list.append(i['membership_type'])
            self.intr_type.append(i['interest_type'])
            self.roi_list.append(i['roi'])
            self.max_amount_list.append(i['max_amount'])
            self.min_amount_list.append(i['min_amount'])
            self.min_tenure_list.append(i['min_tenure'])
            self.max_tenure_list.append(i['max_tenure'])
            self.emi_payment_list.append(i['emi_payment'])
            self.disc_coupans_list.append(i['discount_coupons'])

        if a == -1:
            alert("No Data Available Here!!")
        else:
            if self.id_list:
                self.label_1.text = str(self.id_list[-1])

            if self.name_list:
                self.name.selected_value = self.name_list[-1]

            if self.discri_list:
                self.discri_list = str(self.name_list[-1])

            if self.product_categorys:
                self.product_category.selected_value = self.product_categorys[-1]

            if self.profee_list:
                self.text_box_3.text = str(self.profee_list[-1])

            if self.extfee_list:
                self.text_box_4.text = str(self.extfee_list[-1])

            if self.foreclosure_type_list:
                self.foreclose_type.text = self.foreclosure_type_list[-1]

            if self.extension_allowed_list:
                self.extension_allowed.text = str(self.extension_allowed_list[-1])  # or .selected_value?

            if self.type_list:
                self.drop_down_2.selected_value = self.type_list[-1]

            if self.intr_type:
                selected_interest_type = str(self.intr_type[-1])
                if selected_interest_type == "Fixed":
                    self.radio_button_1.selected = True
                    self.radio_button_2.selected = False
                    self.min_amount.enabled = False
                    self.max_amount.enabled = False
                    self.min_tenure.enabled = False
                    self.max_tenure.enabled = False
                    self.roi.enabled = False
                    self.foreclose_type.enabled = False
                    self.extension_allowed.enabled = False
                    self.emi_payment.enabled = False
                else:
                    self.radio_button_1.selected = False
                    self.radio_button_2.selected = True
            else:
                self.radio_button_1.selected = False
                self.radio_button_2.selected = False

            if self.roi_list:
                self.roi.text = str(self.roi_list[-1])

            if self.min_amount_list:
                self.min_amount.text = str(self.min_amount_list[-1])

            if self.max_amount_list:
                self.max_amount.text = str(self.max_amount_list[-1])

            if self.min_tenure_list:
                self.min_tenure.text = str(self.min_tenure_list[-1])

            if self.max_tenure_list:
                self.max_tenure.text = str(self.max_tenure_list[-1])

            if self.emi_payment_list:
                self.emi_payment.text = str(self.emi_payment_list[-1])

            if self.disc_coupans_list:
                if self.disc_coupans_list[-1] == "Yes":
                    self.radio_button_3.text = "Yes"
                    self.radio_button_4.text = "No"
                else:
                    self.radio_button_3.text = "No"
                    self.radio_button_4.text = "Yes"

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('admin.dashboard.manage_products.view_product')

        if (
            self.name.selected_value is None
            or self.product_category.selected_value is None
            or self.drop_down_2.selected_value == ""
            or self.text_box_3.text == ""
            or self.text_box_4.text == ""
            or self.intr_type is None
            or self.max_amount.text == ""
            or self.min_amount.text == ""
            or self.min_tenure.text == ""
            or self.max_tenure.text == ""
            or self.roi.text == ""
            or self.emi_payment.text == ""
            or self.radio_button_3.text == ""
        ):
            Notification("Fill All Required Details").show()
        else:
            data = tables.app_tables.product_details.search()
            a = -1
            for row in data:
                a += 1

            if a == -1:
                alert("No Data Available Here")
            else:
                if self.intr_type[-1] == "Fixed":
                    self.name.enabled = False
                    self.product_category.enabled = False
                    self.min_amount.enabled = False
                    self.max_amount.enabled = False
                    self.min_tenure.enabled = False
                    self.max_tenure.enabled = False
                    self.roi.enabled = False
                    self.foreclose_type.enabled = False
                    self.extension_allowed.enabled = False
                    self.emi_payment.enabled = False
                    self.text_box_3.enabled = False
                    self.text_box_4.enabled = False
                    self.radio_button_3.enabled = False
                else:
                    data[a]['product_name'] = self.name.selected_value
                    data[a]['product_discription'] = self.text_area_1.text
                    data[a]['product_categories'] = self.product_category.selected_value
                    data[a]['processing_fee'] = int(self.text_box_3.text)
                    data[a]['extension_fee'] = int(self.text_box_4.text)
                    data[a]['membership_type'] = self.drop_down_2.selected_value
                    data[a]['interest_type'] = self.radio_button_1.text
                    data[a]['min_amount'] = int(self.min_amount.text)
                    data[a]['max_amount'] = int(self.max_amount.text)
                    data[a]['min_tenure'] = int(self.min_tenure.text)
                    data[a]['max_tenure'] = int(self.max_tenure.text)
                    data[a]['roi'] = int(self.roi.text)
                    data[a]['foreclose_type'] = self.foreclose_type.selected_value
                    extension_allowed_mapping = {'Yes': True, 'No': False}
                    data[a]['extension_allowed'] = extension_allowed_mapping.get(self.extension_allowed.text, False)
                    data[a]['emi_payment'] = self.emi_payment.selected_value
                    data[a]['discount_coupons'] = self.radio_button_3.text

                    Notification("Product details updated successfully").show()

    def link_1_copy_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form('admin.dashboard.manage_products.view_product')
