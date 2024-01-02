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
def deposit_money(email, deposit_amount):
    # Fetch customer_id using email from user_profile table
    user_profile = app_tables.user_profile.get(user_email=email)
    if user_profile is not None:
        customer_id = user_profile['customer_id']
    else:
        print(f"No user profile found for email: {email}")
        return False  # Unable to find user profile
    
    transaction_id = str(uuid.uuid4())  # Generate unique transaction_id
    
    app_tables.wallet_transactions.add_row(
        user_email=email,
        customer_id=customer_id,
        transaction_id=transaction_id,
        amount=deposit_amount,
        transaction_type='Success'  # Assuming successful deposit
    )
    return True  # Deposit successful

@anvil.server.callable
def withdraw_money(email, withdraw_amount):
    # Fetch customer_id using email from user_profile table
    user_profile = app_tables.user_profile.get(user_email=email)
    if user_profile is not None:
        customer_id = user_profile['customer_id']
    else:
        print(f"No user profile found for email: {email}")
        return False  # Unable to find user profile
    
    transaction_id = str(uuid.uuid4())  # Generate unique transaction_id
    
    transactions_rows = app_tables.wallet_transactions.search(
        user_email=email, customer_id=customer_id
    )
    
    if len(transactions_rows) > 0:
        transactions_row = transactions_rows[0]
        
        if transactions_row['amount'] >= withdraw_amount:
            transactions_row['amount'] -= withdraw_amount
            transactions_row['transaction_id'] = transaction_id
            transactions_row['transaction_type'] = 'Success'
            transactions_row.update()
            return True  # Withdrawal successful
        else:
            print("Insufficient balance for withdrawal")
            app_tables.wallet_transactions.add_row(
                user_email=email,
                customer_id=customer_id,
                transaction_id=transaction_id,
                amount=withdraw_amount,
                transaction_type='Fail'  # Insufficient balance
            )
            return False  # Insufficient balance for withdrawal
    else:
        print(f"No rows found for email: {email} and customer_id: {customer_id}")
        return False  # Withdrawal unsuccessful