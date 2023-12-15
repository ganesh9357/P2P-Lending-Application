from ._anvil_designer import default_loansTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime

class default_loans(default_loansTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.loan = tables.app_tables.loan_details.search()
    self.fourcloser = tables.app_tables.foreclosure.search()
    self.today = datetime.now().date()
    print(self.today)

    self.due_list = []
    self.loan_amont = []
    self.paid_amount = []
    self.intrest = []
    self.loan_due_amount = []

    self.id = []
    self.c_id = []
    self.full_name = []
    self.status = []
    for i in self.loan:
      self.due_list.append(i['due_date'].date())
      self.loan_amont.append(i['loan_amount'])
      self.id.append(i['loan_id'])
      self.intrest.append(i['interest_rate'])
      self.loan_due_amount.append(i['total_repayment_amount'])
      self.c_id.append(i['coustmer_id'])
      self.full_name.append(i['full_name'])
      self.status.append(i['loan_updated_status'])

    self.id_1 = []
    for i in self.fourcloser:
      self.paid_amount.append(i['paid_amount'])
      self.id_1.append(i['loan_id'])


    self.index = []  
    for i in self.id:
      if i in self.id_1:
        b = self.id_1.index(i)
        if (self.loan_amont[b] != 0) and (self.status[b] != "closed"):
          self.index.append(self.id_1[b])

    self.result = []
    self.days = {}
    for i in self.index:
      c = self.index.index(i)
      d = d = ((self.today - self.due_list[c]).days > 3) and ((self.today - self.due_list[c]).days < 90)
      if (self.due_list[c] < self.today) and (d):
        annual_interest_rate = self.intrest[c]
        days_in_year = 365
        daily_interest_rate = (annual_interest_rate / 100) / days_in_year
        print(daily_interest_rate)
        self.result.append(self.id[c])
        interest_per_day = self.loan_due_amount[c] * daily_interest_rate
        days_late = (self.today - self.due_list[c]).days
        penalty = interest_per_day * days_late
        total_due = self.loan_due_amount[c] + penalty
        self.days[self.id[c]] = total_due
    
    print(self.result)
    print(self.days)
    self.index1 = []
    self.final = []
    self.total = []
    for id, total in self.days.items():
      self.index1.append(self.id.index(id))
      self.total.append(total)

    a = -1
    for i in self.index1:
      a += 1
      self.final.append({'loan_id' : self.id[i], 'coustmer_id' : self.c_id[i], 'full_name' : self.full_name[i], 'amount': int(self.total[a])})

    self.repeating_panel_1.items = self.final

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.loan_management')
