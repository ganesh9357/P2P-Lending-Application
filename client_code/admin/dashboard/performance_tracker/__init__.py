from ._anvil_designer import performance_trackerTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class performance_tracker(performance_trackerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data = tables.app_tables.loan_details.search()

    self.name_list = []
    
    a = 0
    for i in self.data:
      self.name_list.append(i['loan_updated_status'])
      
      a += 1
    self.label_4.text = a
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    for i in self.name_list:
      if i == 'approved':
        b += 1
      elif i == 'rejected':
        c += 1
      elif i == 'opened':
        d += 1
      elif i == 'closed':
        e += 1 
      elif i == 'under process':
        f += 1
    self.label_8.text = b
    self.label_6.text = c
    self.label_14.text = d
    self.label_12.text = e
    self.label_13.text = f

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard')

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.loan_management.approved_loans')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.loan_management.rejected_loans')

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.loan_management.open_loans')

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.loan_management.closed_loans')

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.loan_management.under_process')

