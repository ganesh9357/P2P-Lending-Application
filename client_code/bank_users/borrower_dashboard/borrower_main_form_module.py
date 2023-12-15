import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from .bank_users.borrower_rgistration_form import Module1
#
#    Module1.say_hello()
#

user_id=""

userId = 0

# this is from the borrower data enters

def borrower_table_data_entry():
  user_data=app_tables.user_profile.search(coustmer_id=user_id)
  if user_data:
    user_1=app_tables.u