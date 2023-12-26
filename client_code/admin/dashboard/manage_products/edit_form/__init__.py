# 

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

        self.id_list = []
        self.name_list = []
        self.product_categorys = []
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
            self.label_1.text = self.id_list[-1]
            self.text_box_2.text = self.name_list[-1]
            self.product_category.text = self.product_categorys[-1]
            self.text_box_3.text = str(self.profee_list[-1])
            self.text_box_4.text = str(self.extfee_list[-1])
            self.foreclose_type.text = self.foreclosure_type_list[-1]
            self.extension_allowed.text = str(self.extension_allowed_list[-1])
            self.drop_down_2.selected_value = self.type_list[-1]
            if self.intr_type:
                self.radio_button_1.text = self.intr_type[-1]
            else:
                self.radio_button_2.text = self.intr_type[-1]

            self.roi.text = str(self.roi_list[-1])
            self.min_amount.text = str(self.min_amount_list[-1])
            self.max_amount.text = str(self.max_amount_list[-1])
            self.min_tenure.text = str(self.min_tenure_list[-1])
            self.max_tenure.text = str(self.max_tenure_list[-1])
            self.emi_payment.text = str(self.emi_payment_list[-1])
            if self.disc_coupans_list:
                self.radio_button_3.text = self.disc_coupans_list[-1]
            else:
                self.radio_button_4.text = self.disc_coupans_list[-1]

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('admin.dashboard.manage_products.view_product')

        if (
            self.text_box_2.text == ""
            or self.product_category.text == ""
            or self.drop_down_2.selected_value == ""
            or self.text_box_3.text == ""
            or self.text_box_4.text == ""
            or self.intr_type == ""
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
                data[a]['product_name'] = self.text_box_2.text
                data[a]['product_categories'] = self.product_category.text
                data[a]['processing_fee'] = int(self.text_box_3.text)
                data[a]['extension_fee'] = int(self.text_box_4.text)
                data[a]['membership_type'] = self.drop_down_2.selected_value
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

    def link_1_copy_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form('admin.dashboard.manage_products.view_product')
