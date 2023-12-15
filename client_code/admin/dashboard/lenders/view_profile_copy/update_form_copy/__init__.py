from ._anvil_designer import update_form_copyTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

class update_form_copy(update_form_copyTemplate):
  def __init__(self, get_customer_id_value, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.get = get_customer_id_value

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_2.text == "" or  self.text_box_3.text == "" or self.text_box_4.text == "" or self.text_box_5.text == ""  or self.text_box_7.text == "" or self.text_box_8.text == "" or self.text_box_9.text == "" or self.text_box_10.text == "" or self.text_box_12.text == "" or self.text_box_13.text == "" or self.text_box_14.text == "" or self.text_box_15.text == "" or self.text_box_17.text == "" or self.text_box_18.text == "" or self.text_box_19.text == "" or self.text_box_20.text == "" or self.text_box_21.text == "" or self.text_box_22.text == "" or self.text_box_23.text == "" or self.text_box_24.text == "" or self.text_box_25.text == "" or self.text_box_26.text == "" or self.text_box_27.text == "" or self.text_box_28.text == "" or self.text_box_29.text == "" or self.text_box_30.text == "" or self.text_box_32.text == "" or self.text_box_33.text == "" or self.text_box_34.text == "" or self.text_box_35.text == "" :
      Notification("Fill All Required Details").show()
    else:
      data = tables.app_tables.user_profile.search()
      id_list = []
      for i in data:
        id_list.append(i['coustmer_id'])

      if self.get in id_list:
        a = id_list.index(self.get)
        data[a]['full_name'] = self.text_box_2.text
        data[a]['profile_status'] = bool(self.text_box_3.text)
        data[a]['gender'] = self.text_box_4.text
        data[a]['user_age'] = int(self.text_box_5.text)
        data[a]['date_of_birth'] = self.date_picker_1.date
        data[a]['mobile'] = self.text_box_7.text
        data[a]['aadhaar_no'] = self.text_box_8.text
        data[a]['pan_number'] = self.text_box_9.text
        data[a]['city'] = self.text_box_10.text
        data[a]['last_confirm'] = bool(self.text_box_12.text)
        data[a]['mobile_check'] = bool(self.text_box_13.text)
        data[a]['mouther_tounge'] = self.text_box_14.text
        data[a]['marital_status'] = self.text_box_15.text
        data[a]['Date_mariage'] = self.date_picker_2.date
        data[a]['spouse_name'] = self.text_box_17.text
        data[a]['spouse_mobile'] = self.text_box_18.text
        data[a]['spouse_company_name'] = self.text_box_19.text
        data[a]['spouse_company_address'] = self.text_box_20.text
        data[a]['spouse_profficen'] = self.text_box_21.text
        data[a]['usertype'] = self.text_box_22.text
        data[a]['registration_approve'] = bool(self.text_box_23.text)
        data[a]['about'] = self.text_box_24.text
        data[a]['address_type'] = self.text_box_25.text
        data[a]['alerts'] = bool(self.text_box_26.text)
        data[a]['building_name'] = self.text_box_27.text
        data[a]['house_landmark'] = self.text_box_28.text
        data[a]['house_no'] = self.text_box_29.text
        data[a]['pincode'] = self.text_box_30.text
        data[a]['business_no'] = self.text_box_31.text
        data[a]['qualification'] = self.text_box_32.text
        data[a]['state'] = self.text_box_33.text
        data[a]['street'] = self.text_box_34.text
        data[a]['terms'] = bool(self.text_box_35.text)
        data[a]['another_email'] = self.text_box_1.text
        data[a]['company_name'] = self.text_box_6.text
        data[a]['organization_type'] = self.text_box_11.text
        data[a]['employment_type'] = self.text_box_16.text
        data[a]['company_landmark'] = self.text_box_36.text
        data[a]['company_address'] = self.text_box_37.text
        data[a]['annual_salary'] = self.text_box_38.text
        data[a]['designation'] = self.text_box_39.text
        data[a]['account_name'] = self.text_box_40.text
        data[a]['account_type'] = self.text_box_41.text
        data[a]['account_number'] = self.text_box_42.text
        data[a]['account_bank_branch'] = self.text_box_43.text
        data[a]['ifsc_code'] = self.text_box_44.text
        data[a]['salary_type'] = self.text_box_45.text
        data[a]['select_bank'] = self.text_box_46.text
        data[a]['net_bank'] = self.text_box_47.text
        data[a]['father_name'] = self.text_box_48.text
        data[a]['father_age'] = self.text_box_49.text
        data[a]['mother_name'] = self.text_box_50.text
        data[a]['mother_age'] = self.text_box_51.text
        data[a]['college_name'] = self.text_box_52.text
        data[a]['college_id'] = self.text_box_53.text
        data[a]['college_address'] = self.text_box_54.text
        data[a]['running_Home_Loan'] = self.text_box_55.text
        print(a)
        open_form('admin.dashboard.lenders.view_profile_copy', self.get)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.lenders.view_profile_copy', self.get)
