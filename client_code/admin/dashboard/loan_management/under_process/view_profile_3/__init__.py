from ._anvil_designer import view_profile_3Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class view_profile_3(view_profile_3Template):
  def __init__(self, value_to_display, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.user = tables.app_tables.user_profile.search()
    self.type = []
    self.id = []
    
    for i in self.user:
      self.type.append(i['usertype'])
      self.id.append(i['coustmer_id'])

    if value_to_display in self.id:
      a = self.id.index(value_to_display)
      self.label_34.text = self.type[a]
      
    self.data = tables.app_tables.loan_details.search()

    a = -1
    self.list_1 = []
    self.list_2 = []
    self.list_3 = []
    self.list_4 = []
    self.list_5 = []
    self.list_6 = []
    self.list_7 = []
    self.list_8 = []
    self.list_9 = []
    self.list_10 = []
    self.list_11 = []
    self.list_12 = []
    self.list_13 = []
    self.list_14 = []
    self.list_15 = []
    self.list_16 = []

    for i in self.data:
      a+=1
      self.list_1.append(i['loan_id'])
      self.list_2.append(i['coustmer_id'])
      self.list_3.append(i['full_name'])
      self.list_4.append(i['loan_status'])
      self.list_5.append(i['application_status'])
      self.list_6.append(i['min_amount'])
      self.list_7.append(i['max_amount'])
      self.list_8.append(i['interest_rate'])
      self.list_9.append(i['timestamp'])
      self.list_10.append(i['total_repayment_amount'])
      self.list_11.append(i['payment_done'])
      self.list_12.append(i['member_rom'])
      self.list_13.append(i['beseem_score'])
      self.list_14.append(i['email_id'])
      self.list_15.append(i['tenure'])
      self.list_16.append(i['loan_updated_status'])
    print(a)

    if value_to_display in self.list_2:
      b = self.list_2.index(value_to_display)
      self.label_2.text = self.list_1[b]
      self.label_4.text = self.list_2[b]
      self.label_6.text = self.list_3[b]
      self.label_8.text = self.list_4[b]
      self.label_10.text = self.list_5[b]
      self.label_12.text = self.list_6[b]
      self.label_14.text = self.list_7[b]
      self.label_16.text = self.list_8[b]
      self.label_18.text = self.list_9[b]
      self.label_20.text = self.list_10[b]
      self.label_22.text = self.list_11[b]
      self.label_24.text = self.list_12[b]
      self.label_26.text = self.list_13[b]
      self.label_28.text = self.list_14[b]
      self.label_30.text = self.list_15[b]
      self.label_32.text = self.list_16[b]

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.loan_management.under_process')
