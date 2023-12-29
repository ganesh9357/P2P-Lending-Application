from ._anvil_designer import walletTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import open_form, server
from ...lendor_registration_form.dashboard import lendor_main_form_module as main_form_module


class wallet(walletTemplate):
  def __init__(self, **properties):
    
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.deposit_placeholder = "5000"
    self.withdraw_placeholder = "0.00"
    
  
    self.user_id = main_form_module.userId
    user_id = self.user_id
    
    ### Fetch user details from user_profile database
    user_profiles = app_tables.user_profile.search()  

    # Mapping and inserting data into the wallet table
    for profile in user_profiles:
      print(f"Adding row for customer ID: {profile['customer_id']}")
    # Add similar print statements for other column values

    wallet_row = app_tables.wallet.add_row(
        customer_id=profile['customer_id'],
        user_name=profile['full_name'],
        user_email=profile['email_user'],
        account_name=profile['account_name'],
        account_number=profile['account_number'],
        bank_name=profile['select_bank'],
        branch_name=profile['account_bank_branch'],
        ifsc_code=profile['ifsc_code']
    )
    print("Row added successfully")

    # # Display a success message
    # notification = anvil.Notification("Fetched Data successfully!", style="success")
    # notification.show()

    # save the amount to e_wallet column 

    # e_wallet = None

    # user_data = app_tables.wallet.search(customer_id=customer_id)

    # if user_data and len(user_data) > 0:
    #   e_wallet = user_data[0]['e_wallet']

    # if e_wallet:
    #   self.amount_text_box.text = e_wallet
    # Fetch the user's profile
    user_profile = app_tables.user_profile.get(customer_id=customer_id)

    if user_profile is not None:
      customer_id = user_profile['customer_id']

      e_wallet = None
      user_data = app_tables.wallet.search(customer_id=customer_id)

      if user_data and len(user_data) > 0:
        e_wallet = user_data[0]['e_wallet']

      if e_wallet:
        self.amount_text_box.text = str(e_wallet)
      else:
        # Handle if user profile doesn't exist
        notification = anvil.Notification("User profile not found!", style="warning")
        notification.show()


  def home_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard")

  def about_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.dasboard_about")

  def contact_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.dasboard_contact")

  def notification_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('lendor_registration_form.dashboard.notification')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def deposit_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_9.visible = False
    self.text_box_5.visible = False
    self.icon1.visible = False
    self.amount_text_box.placeholder = self.deposit_placeholder
    self.deposit_money_btn.visible = True
    self.withdraw_money_btn.visible = False


  def withdraw_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_9.visible = True
    self.text_box_5.visible = True
    self.icon1.visible = True
    self.amount_text_box.placeholder = self.withdraw_placeholder
    self.deposit_money_btn.visible = False
    self.withdraw_money_btn.visible = True
    self.deposit_btn.visible = True

  def wallet_dashboard_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def deposit_money_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    # selected_row = self.selected_row
    # customer_id = selected_row['customer_id']
    # e_wallet = selected_row['e_wallet']

    e_wallet = self.amount_text_box.text
   
    if e_wallet:
      user_data = app_tables.wallet.search(customer_id=customer_id)

    if user_data and len(user_data) > 0:
      user_row = user_data[0]
      user_row['e_wallet'] = e_wallet
    
    else:
      # If the row doesn't exist, add a new row
      app_tables.wallet.add_row(customer_id=customer_id, e_wallet=e_wallet)
    
    # customer_id = main_form_module.userId  

    # e_wallet = self.amount_text_box.text
    
    # # Check if the entered amount is valid
    # if e_wallet:
    #     try:
    #         e_wallet_amount = int(e_wallet)  
    #     except ValueError:
    #         # Handle if the entered amount is not a valid integer
    #         notification = anvil.Notification("Please enter a valid amount!", style="warning")
    #         notification.show()
    #         return

    #     # Fetch the user's data from the wallet table
    #     user_data = app_tables.wallet.search(customer_id=customer_id)

    #     if user_data and len(user_data) > 0:
    #         # If the row exists, update the e_wallet value
    #         user_row = user_data[0]
    #         user_row['e_wallet'] = e_wallet_amount
    #         print("Updating existing row...")
    #     else:
    #         # If the row doesn't exist, add a new row
    #         app_tables.wallet.add_row(customer_id=customer_id, e_wallet=e_wallet_amount)
    #         print("Adding new row...")
            
    #     # Display a success message after updating or adding the e_wallet value
    #     notification = anvil.Notification("Money Deposited successfully!", style="success")
    #     notification.show()
    # else:
    #     # Notify if no amount is entered
    #     notification = anvil.Notification("Please enter an amount!", style="warning")
    #     notification.show()


  
  # def deposit_money_btn_click(self, **event_args):
  #   """This method is called when the button is clicked"""
  #   customer_id = main_form_module.userId  

  #   e_wallet = self.amount_text_box.text
  #   if e_wallet:
  #       user_data = app_tables.wallet.search(customer_id=customer_id)

  #       if user_data and len(user_data) > 0:
  #           # If the row exists, update the e_wallet value
  #           user_row = user_data[0]
  #           user_row['e_wallet'] = int(e_wallet)  
  #       else:
  #           # If the row doesn't exist, add a new row
  #           app_tables.wallet.add_row(customer_id=customer_id, e_wallet=int(e_wallet))
            
  #       # Display a success message after updating or adding the e_wallet value
  #       notification = anvil.Notification("Money Deposited successfully!", style="success")
  #       notification.show()
  #   else:
  #       # Notify if no amount is entered
  #       notification = anvil.Notification("Please enter an amount!", style="warning")
  #       notification.show()

