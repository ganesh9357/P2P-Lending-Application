import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

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
# try:
#         # Fetch user_email and wallet_id based on customer_id
#         lender_row = app_tables.lender.get(email_id=email)
        
#         if lender_row is not None:
#             wallet_amount = lender_row['investment']

@anvil.server.callable
def create_wallet_entry(email, customer_id, full_name, user_type):
    # Generate unique wallet_id and account_id
    wallet_id = generate_wallet_id()
    account_id = generate_account_id()
    
    existing_wallets = app_tables.wallet.search(user_email=email)
    print(existing_wallets)
    
    if len(existing_wallets) == 0:
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
    print(user_profiles)
    return user_profiles

def generate_wallet_id():
    existing_wallets = app_tables.wallet.search(tables.order_by("wallet_id", ascending=False))

    if existing_wallets and len(existing_wallets) > 0:
        new_wallet_id = existing_wallets[0]['wallet_id']
        counter = int(new_wallet_id[2:]) + 1
    else:
        counter = 1  # Start the counter from 1 if no existing wallets

    return f"WA{counter:04d}"  # Ensure counter is formatted to 4 digits

def generate_account_id():
    existing_accounts = app_tables.wallet.search(tables.order_by("account_id", ascending=False))

    if existing_accounts and len(existing_accounts) > 0:
        new_account_id = existing_accounts[0]['account_id']
        counter = int(new_account_id[1:]) + 1
    else:
        counter = 1  

    return f"A{counter:04d}" 


# code for wallet_transactions
def generate_transaction_id():
    latest_transaction = app_tables.wallet_transactions.search(
        tables.order_by("transaction_id", ascending=False)
    )

    if latest_transaction and len(latest_transaction) > 0:
        last_transaction_id = latest_transaction[0]['transaction_id']
        counter = int(last_transaction_id[2:]) + 1
    else:
        counter = 1

    return f"TA{counter:04d}"


@anvil.server.callable
def deposit_money(email, deposit_amount, customer_id):
    transaction_id = generate_transaction_id()
    
    try:
        # Fetch user_email and wallet_id based on customer_id
        wallet_row = app_tables.wallet.get(user_email=email)
        
        if wallet_row is not None:
            user_email = wallet_row['user_email']
            wallet_id = wallet_row['wallet_id']
            
            # Add a row to wallet_transactions table with transaction timestamp
            app_tables.wallet_transactions.add_row(
                user_email=str(user_email),
                wallet_id=str(wallet_id),
                customer_id=customer_id,
                transaction_id=transaction_id,
                amount=deposit_amount,
                transaction_type='deposit',
                transaction_time_stamp=datetime.now(),
                status='success' 
            )
            
            return True
        else:
            print("Customer not found in the wallet table.")
            return False
    except Exception as e:
        print(f"Deposit failed: {e}")
        app_tables.wallet_transactions.add_row(
            customer_id=customer_id,
            transaction_id=transaction_id,
            amount=deposit_amount,
            transaction_type='deposit',
            transaction_time_stamp=datetime.now(),  
            status='fail'
        )
        return False

@anvil.server.callable
def withdraw_money(email, withdraw_amount, customer_id):
    transaction_id = generate_transaction_id()
    
    try:
        # Fetch user_email and wallet_id based on customer_id
        wallet_row = app_tables.wallet.get(user_email=email)
        
        if wallet_row is not None:
            user_email = wallet_row['user_email']
            wallet_id = wallet_row['wallet_id']
            
            # Add a row to wallet_transactions table with transaction timestamp
            app_tables.wallet_transactions.add_row(
                user_email=str(user_email),
                wallet_id=str(wallet_id),
                customer_id=customer_id,
                transaction_id=transaction_id,
                amount=withdraw_amount,
                transaction_type='withdraw',
                transaction_time_stamp=datetime.now(),
                status='success' 
            )
            
            return True
        else:
            print("Customer not found in the wallet table.")
            return False
    except Exception as e:
        print(f"Withdrawal failed: {e}")
        app_tables.wallet_transactions.add_row(
            customer_id=customer_id,
            transaction_id=transaction_id,
            amount=withdraw_amount,
            transaction_type='withdraw',
            transaction_time_stamp=datetime.now(), 
            status='fail'
        )
        return False


    
# @anvil.server.callable
# def deposit_money(email, deposit_amount, customer_id):
#     transaction_id = generate_transaction_id()
    
#     try:
#         app_tables.wallet_transactions.add_row(
#             user_email=str(email),
#             customer_id=customer_id,
#             transaction_id=transaction_id,
#             amount=deposit_amount,
#             transaction_type='deposit'
#         )
#         return True
#     except Exception as e:
#         print(f"Deposit failed: {e}")
#         return False


@anvil.server.callable
def fetch_profile_data_and_insert(email, customer_id):
    try:
        # Fetch user profile based on customer_id
        profile = app_tables.user_profile.get(email_user=email)
        
        if profile is not None:
            # Fetch wallet data based on customer_id
            wallet_data = app_tables.wallet.get(user_email=email)
            
            if wallet_data is not None:
                wallet_id = wallet_data['wallet_id']
                account_id = wallet_data['account_id']
                
                # Check if account_number is a string before converting to number
                account_number_value = int(profile['account_number']) if isinstance(profile['account_number'], str) else profile['account_number']
                
                # Add a row to wallet_bank_account_table
                app_tables.wallet_bank_account_table.add_row(
                    user_email=profile['email_user'], 
                    account_name=profile['account_name'],
                    account_number=account_number_value,
                    bank_name=profile['select_bank'],  
                    branch_name=profile['account_bank_branch'],  
                    ifsc_code=profile['ifsc_code'],
                    account_type=profile['account_type'],
                    wallet_id=wallet_id,
                    account_id=account_id
                )
                
                return True
            else:
                print("Wallet data not found for the provided customer_id.")
                return False
        else:
            print("Profile not found for the provided customer_id.")
            return False
    except Exception as e:
        print(f"Error occurred: {e}")
        return False