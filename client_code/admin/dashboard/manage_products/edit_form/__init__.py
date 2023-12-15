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
    self.profee_list = []
    self.extfee_list = []
    self.type_list = []
    self.min_list = []
    self.max_list = []
    self.roi_list = []
    a = -1
    for i in self.data:
      a+=1
      self.id_list.append(i['product_id'])
      self.name_list.append(i['product_name'])
      self.profee_list.append(i['processing_fee'])
      self.extfee_list.append(i['extension_fee'])
      self.type_list.append(i['membership_type'])
      self.max_list.append(i['max_days'])
      self.min_list.append(i['min_days'])
      self.roi_list.append(i['roi'])

    if a == -1:
      alert("No Data Available Here!!")
    else:

      self.label_1.text = self.id_list[-1]
      self.text_box_2.text = self.name_list[-1]
      self.text_box_3.text = self.profee_list[-1]
      self.text_box_4.text = self.extfee_list[-1]
      self.drop_down_2.selected_value = self.type_list[-1]
      self.drop_down_3.text = self.max_list[-1]
      self.drop_down_4.text = self.min_list[-1]

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_products.view_product')

    
    if  self.text_box_2.text == ""  or self.text_box_3.text == "" or self.text_box_4.text  == "" or  self.drop_down_2.selected_value == "" or   self.drop_down_3.selected_value == "" or self.drop_down_4.selected_value == "" or self.text_box_5.text == "":
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
       data[a]['processing_fee'] = int(self.text_box_3.text)
       data[a]['extension_fee'] = int(self.text_box_4.text)
       data[a]['membership_type'] = self.drop_down_2.selected_value
       data[a]['max_days'] = int(self.drop_down_3.text)
       data[a]['min_days'] = int(self.drop_down_4.text)
       data[a]['roi'] = int(self.text_box_5.text)

  def link_1_copy_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.manage_products.view_product')