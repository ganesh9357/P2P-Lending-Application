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

# from collections import defaultdict

# # A dictionary to store counts for each email
# email_counts = defaultdict(int)

# Your existing code remains unchanged here...
@anvil.server.callable
def create_wallet_entry(email, customer_id, full_name, user_type,user_id):
    # Generate a unique loan ID and get the updated counter
     wallet_id = generate_wallet_id
     account_id = generate_account_id

    # Search for the user profile
     user_profiles = app_tables.user_profile.search(customer_id=user_id)
    
     if user_profiles and len(user_profiles) > 0:
        # If there is a user profile, get the first one
        user_profile = user_profiles[0]

        # Extract the full name from the user profile
        user_name = user_profile['full_name']
        user_email = user_profile['email_user']
        user_type = user_profile['user_type']
        # Add the wallet details to the data table
        app_tables.wallet.add_row(
            wallet_id=wallet_id,
            account_id=account_id,
            customer_id=customer_id,
        )
        # Return the generated wallet ID to the client
        return wallet_id and account_id
       
     else:
        # Handle the case where no user profile is found
        return "User profile not found"
       
# @anvil.server.callable
# def create_wallet_entry(email, customer_id, full_name, user_type):
#     wallet_id = generate_wallet_id
#     existing_wallets = app_tables.wallet.search(user_email=email)
    
    
#     if len(existing_wallets) == 0:
#         wallet_id = generate_wallet_id
#         account_id = generate_account_id(email)
        
#         app_tables.wallet.add_row(
#             user_email=email,
#             wallet_id=wallet_id,
#             account_id=account_id,
#             customer_id=customer_id,
#             user_name=full_name,
#             user_type=user_type
#         )
#         return f"Wallet entry created successfully for {email}"
#     else:
#         return f"Wallet entry already exists for {email}. Multiple entries found."

# @anvil.server.callable
# def fetch_user_profiles():
#     user_profiles = app_tables.user_profile.search()
#     return user_profiles

def generate_wallet_id():
  
    existing_wallets = app_tables.wallet.search()['wallet_id']

    if existing_wallets:
        # Extract the numeric part, convert to integers, and find the maximum
        numeric_part = max(int(wallet_id[2:]) for wallet_id in existing_wallets)
        
        # Generate the new loan ID with the next numeric part
        new_wallet_id = f'WA{numeric_part + 1:04d}'
    else:
        # If no existing IDs, start with 'WA0001'
        new_wallet_id = 'WA0001'

    return new_wallet_id
    app_tables.wallet.add_row(wallet_id = wallet_id)


def generate_account_id():
  
    existing_account = app_tables.wallet.search()['account_id']

    if existing_account:
        # Extract the numeric part, convert to integers, and find the maximum
        numeric_part = max(int(account_id[2:]) for account_id in existing_account)
        
        # Generate the new loan ID with the next numeric part
        new_account_id = f'A{numeric_part + 1:04d}'
    else:
        # If no existing IDs, start with 'A0001'
        new_account_id = 'A0001'

    return new_account_id
    app_tables.wallet.add_row(account_id = account_id)


# def generate_account_id():
#     email_counts[email] += 1
#     count = email_counts[email]
#     formatted_count = str(count).zfill(4)  # Zero-padding
    
#     return f"A{formatted_count}"



@anvil.server.callable
def deposit_money(email, deposit_amount):
    if not isinstance(email, str):
        # Convert the email to a string if it's not already
        email = str(email)
    
    # Fetch customer_id using email from user_profile table
    user_profile = app_tables.user_profile.get(email_user=email)
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

# def generate_wallet_id():
#     # existing_wallets = app_tables.wallet.search(user_email=email)
#     # if len(existing_wallets) == 0:
#     #     return 'WA00001'  # If no wallets exist for the email, start with WA00001
    
#     # # Find the last wallet_id for the email
#     # last_wallet_id = max(existing_wallets, key=lambda x: int(x['wallet_id'][2:]))['wallet_id']
#     # numeric_part = int(last_wallet_id[2:]) + 1
#     # new_wallet_id = f'WA{numeric_part:05d}'  # Format to ensure 5 digits
    
#     # return new_wallet_id