from ._anvil_designer import dashboardTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
from anvil.tables import app_tables
from anvil import open_form, server
#from anvil import get_current_user


class dashboard(dashboardTemplate):
  def __init__(self, **properties):
    
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    
    

    # Any code you write here will run before the form opens.

  

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.opbal")

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.avlbal")

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vblr")

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.ld")

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.td")

  def outlined_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vlo")

  def outlined_button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.lender_view_loans")

  def outlined_button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vler")

  def outlined_button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vlfr")

  def outlined_button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.rta")

  def outlined_button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vdp")

  def outlined_button_8_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vep")

  def outlined_button_9_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vsn")

  def outlined_button_10_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.cp")

  def login_signup_button_click(self, **event_args):
    """This method is called when the button is clicked"""

    alert("Logged out sucessfully")
    anvil.users.logout()
    open_form('bank_users.main_form')

  def home_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard")

  def about_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.dasboard_about")

  def contact_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.dasboard_contact")

  def button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_show(self, **event_args):
    """This method is called when the Button is shown on the screen"""
    pass

  def button_hide(self, **event_args):
    """This method is called when the Button is removed from the screen"""
    pass

  
  def toggleswitch_1_x_change(self, **event_args):
    
    if self.toggleswitch_1.checked:
      self.button_status.text = "ONLINE"
      self.button_status.background = '#0876e8'  # Green color
      self.button_status.foreground = '#FFFFFF'  # White text
      # Update 'make_visibility' column in the 'lender' table to True
      lender_row = app_tables.lender.search() # Assuming you have a row with id=1 for the lender
      lender_row[0]['make_visibility'] = True
      lender_row[0].update()
    else:
      self.button_status.text = "OFFLINE"
      self.button_status.background = '#FFFFFF'  # White color
      self.button_status.foreground = '#FF0000'  # Red text
      lender_row = app_tables.lender.search()# Assuming you have a row with id=1 for the lender
      lender_row[0]['make_visibility'] = False
      lender_row[0].update()

  def notification_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('lendor_registration_form.dashboard.notification')

  def wallet_dashboard_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    
    open_form('wallet.wallet')
    
    # Fetching data from user_profile table
    user_profiles = app_tables.user_profile.search()  # Fetch all records from user_profile table

    # Mapping and inserting data into the wallet table
    for profile in user_profiles:
        wallet_row = app_tables.wallet.add_row(
            lender_email=profile['email_user'],
            lender_customer_id=profile['customer_id'],
            lender_full_name=profile['full_name']
        )

    # Display a success message
    notification = anvil.Notification("Data copied to wallet successfully!", style="success")
    notification.show()


  # def generate_new_wallet_id(self):
  #   # Fetch the existing wallet IDs from the 'wallet' table
  #   existing_wallets = app_tables.wallet.search()
    
  #   if len(existing_wallets) == 0:
  #       # If no wallets exist, start with 'WA001'
  #       return 'WA001'
  #   else:
  #       # Get the last wallet ID, extract the numeric part, and increment it
  #       last_wallet_id = existing_wallets[-1]['wallet_id']
  #       numeric_part = int(last_wallet_id[2:]) + 1
  #       new_wallet_id = f'WA{numeric_part:03d}'  # Format the numeric part to have leading zeros if necessary
  #       return new_wallet_id
  
  # def wallet_dashboard_link_click(self, **event_args):
  #       new_wallet_id = self.generate_new_wallet_id()

  #       user_id = self.user_id

  #        # Store the new wallet ID in the 'wallet' table
  #       app_tables.wallet.add_row(wallet_id=new_wallet_id, lender_customer_id=user_id)
  #       anvil.server.call('add_wallet', user_id, new_wallet_id)
        
        
    
  #       # anvil.server.call('add_wallet',wallet_id)
  #       self.data = tables.app_tables.wallet.search()
    
  #       self.id = 'WA' + str(1000)  
       
  #       a = -1
  #       self.list_1 = []

  #       for i in self.data:
  #           a += 1
  #           self.list_1.append(i['wallet_id']) 
  #       if a == -1:
  #           self.id = 'WA' + str(1000)
  #           user_id = self.user_id
  #           wallet_id = self.id
  #           anvil.server.call('add_wallet',wallet_id)
  #           # self.wallet_dashboard_link.text = self.id
  #       else:
  #           last_wallet_id = self.list_1[-1]
  #           numeric_part = last_wallet_id[2:] 
  #           self.id = 'WA' + str(int(numeric_part) + 1)
  #           user_id = self.user_id
  #           wallet_id = self.id
  #           anvil.server.call('add_wallet',wallet_id)
  #           # self.wallet_dashboard_link.text = self.id
      

    
  #   Fetch user details from user_profile database
  #   user_details = server.call('get_user_details', email_user)

    
  #   if user_details:
  #       # Extract required details
  #       email_user = user_details['user_email']
  #       customer_id = user_details['customer_id']
  #       full_name = user_details['full_name']

  #       # Open wallet form
  #       open_form('wallet.wallet')

  #       # Pass user details to server for wallet creation
  #       server.call('create_wallet', user_email, customer_id, full_name)

  # def wallet_dashboard_link_click(self, **event_args):
  #   # Fetch user details from user_profile database
  #   user_details = server.call('get_user_details')  
    
  #   if user_details:
  #       # Extract required details
  #       email_user = user_details['user_email']
  #       customer_id = user_details['customer_id']
  #       full_name = user_details['full_name']

  #       # Open wallet form
  #       open_form('wallet.wallet')
        
  #       # Pass user details to server for wallet creation
  #       server.call('create_wallet', user_email, customer_id, full_name)

 






    

  


  