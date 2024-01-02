import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

import anvil.server
from anvil import tables

@anvil.server.callable
def create_wallet_entry(email, customer_id, full_name, user_type):
    existing_wallets = app_tables.wallet.search(user_email=email)
    
    if len(existing_wallets) == 0:
        wallet_id = generate_wallet_id(email)
        account_id = generate_account_id(email)
        
        app_tables.wallet.add_row(
            user_email=email,
            wallet_id=wallet_id,
            account_id=account_id,
            customer_id=customer_id,
            user_name=full_name,
            user_type=user_type
        )
        return f"Wallet entry created successfully for {email}"
    else:
        return f"Wallet entry already exists for {email}. Multiple entries found."

@anvil.server.callable
def fetch_user_profiles():
    user_profiles = app_tables.user_profile.search()
    return user_profiles

def generate_wallet_id(email):
    existing_wallets = app_tables.wallet.search(user_email=email)
    count = len(existing_wallets) + 1
    formatted_count = str(count).zfill(4)  # Zero-padding
    
    return f"WA{formatted_count}"

def generate_account_id(email):
    existing_wallets = app_tables.wallet.search(user_email=email)
    count = len(existing_wallets) + 1
    formatted_count = str(count).zfill(4)  # Zero-padding
    
    return f"A{formatted_count}"



@anvil.server.callable
def deposit_money(customer_id, deposit_amount):
    transactions_rows = app_tables.wallet_transactions.search(customer_id=customer_id)
    
    if len(transactions_rows) > 0:
        transactions_row = transactions_rows[0] 
        
        if transactions_row['amount'] is None:
            transactions_row['amount'] = 0  
        
        transactions_row['amount'] += deposit_amount  # Increase e_wallet balance
        transactions_row['transaction_type'] = 'Deposit'  # Set transaction_type to Deposit
        transactions_row.update()  # Update the row
        return True  # Deposit successful
    else:
        print(f"No rows found for customer_id: {customer_id}")
        return False  # Deposit unsuccessful

@anvil.server.callable
def withdraw_money(customer_id, withdraw_amount):
    transactions_rows = app_tables.wallet_transactions.search(customer_id=customer_id)
    
    if len(transactions_rows) > 0:
        transactions_row = transactions_rows[0]  # Update the first row found
        
        # Check if there's enough balance for withdrawal
        if transactions_row['amount'] >= withdraw_amount:
            transactions_row['amount'] -= withdraw_amount  # Decrease e_wallet balance
            transactions_row['transaction_type'] = 'Withdraw'  # Set transaction_type to Withdraw
            transactions_row.update()  # Update the row
            return True  # Withdrawal successful
        else:
            print("Insufficient balance for withdrawal")
            return False  # Insufficient balance for withdrawal
    else:
        print(f"No rows found for customer_id: {customer_id}")
        return False  # Withdrawal unsuccessful