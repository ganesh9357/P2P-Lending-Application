from ._anvil_designer import user_buganalysisTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class user_buganalysis(user_buganalysisTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data = tables.app_tables.user_issues_bugreports.search()

    a = -1
    self.list_1 = []
    self.list_2 = []
    self.list_3 = []
    self.list_4 = []
    self.list_5 = []

    for i in self.data:
      a+=1
      self.list_1.append(i['user_issues'])
      self.list_2.append(i['specific_issue'])
      self.list_3.append(i['user_discription'])
      self.list_4.append(i['feedback_form'])

    print(a)

    self.result = []
    if a == -1:
      alert("No Data Available Here!")
    else:
      for i in range(a+1):
        print(self.list_2[i])
        self.result.append({'user_issues' : self.list_1[i], 'specific_issue' : self.list_2[i], 'user_discription' : self.list_3[i], 'feedback_form' : self.list_4[i]})

      self.repeating_panel_1.items = self.result

      print(self.list_1, self.list_2, self.list_3)
      print(self.result)
      print(a)
