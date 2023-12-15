from ._anvil_designer import view_productTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class view_product(view_productTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data = tables.app_tables.product_details.search()

    a = -1
    self.list_1 = []
    self.list_2 = []
    self.list_3 = []
    self.list_4 = []
    self.list_5 = []
    self.list_6 = []

    for i in self.data:
      a+=1
      self.list_1.append(i['product_id'])
      self.list_2.append(i['product_name'])
      self.list_3.append(i['product_categories'])
      self.list_4.append(i['processing_fee'])
      self.list_5.append(i['extension_fee'])
      self.list_6.append(i['product_group'])

    print(a)

    self.result = []
    if a == -1:
      alert("No Data Available Here!")
    else:
      for i in range(a+1):
        print(self.list_2[i])
        self.result.append({'product_id' : self.list_1[i], 'product_name' : self.list_2[i], 'product_categories' : self.list_3[i], 'processing_fee' : self.list_4[i], 'extension_fee' : self.list_5[i], 'product_group' : self.list_6[i]})

      self.repeating_panel_1.items = self.result

      print(self.list_1, self.list_2, self.list_3)
      print(self.result)
      print(a)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.manage_products')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_products.edit_form')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_products.update_form')
