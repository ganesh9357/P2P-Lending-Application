from ._anvil_designer import star_1_borrower_registration_form_begin_3fTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_begin_3f(star_1_borrower_registration_form_begin_3fTemplate):
  def __init__(self, user_id , **properties):
    self.userId = user_id
    user_data=app_tables.user_profile.get(coustmer_id=user_id)
    if user_data:
      self.text_box_1.text=user_data['annual_salary']
      self.text_box_2.text=user_data['designation']
      user_data.update()
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def button_2_click(self, **event_args):
    annual_salary = self.text_box_1.text
    designation = self.text_box_2.text
    emp_id_proof = self.file_loader_1.file
    last_six_month = self.file_loader_2.file
    user_id = self.userId
    anvil.server.call('add_lendor_individual_form_3',annual_salary, designation,emp_id_proof,last_six_month,user_id)
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin_4',user_id = user_id)


  def button_1_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3e',user_id=self.userId)

  def button_3_click(self, **event_args):
    open_form("bank_users.user_form")
