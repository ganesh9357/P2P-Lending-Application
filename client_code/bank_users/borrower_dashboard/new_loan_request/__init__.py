from ._anvil_designer import new_loan_requestTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import borrower_main_form_module as main_form_module

class new_loan_request(new_loan_requestTemplate):
    def __init__(self, **properties):
        self.user_id = main_form_module.userId
        self.init_components(**properties)
        self.max_amount_lb.text = f"200000"
        self.drop_down_1= app_tables.product_group.search()


    def button_1_click(self, **event_args):
        open_form('bank_users.borrower_dashboard')
