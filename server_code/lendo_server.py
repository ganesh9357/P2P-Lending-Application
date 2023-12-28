import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_lendor_frist_form(name,gender,date_of_birth,user_id):
  row = app_tables.user_profile.search(customer_id = user_id)
  if row:
    row[0]['full_name'] = name
    row[0]['gender'] = gender
    row[0]['date_of_birth'] = date_of_birth
    row[0]['form_count'] = 0

@anvil.server.callable
def add_lendor_second_form(mobile,email,photo,user_id):
  row = app_tables.user_profile.search(customer_id = user_id)
  if row:
    #row[0]['investment'] = investment
    row[0]['mobile'] = mobile
    row[0]['another_email'] = email
    row[0]['user_photo'] = photo
    row[0]['form_count'] = 1

@anvil.server.callable
def add_lendor_education_form(qualification,certificate,user_id):
  row = app_tables.user_profile.search(customer_id = user_id)
  if row:
    
    row[0]['qualification'] = qualification
    row[0]['education_certificate'] = certificate
    

@anvil.server.callable
def add_lendor_third_form(aadhaar_photo, pan_card, pan_id,aadhaar_card,user_id):
  row = app_tables.user_profile.search(customer_id = user_id)
  if row:
    row[0]['pan_photo'] = pan_id
    row[0]['pan_number'] = pan_card
    row[0]['aadhaar_no'] = aadhaar_card
    row[0]['aadhaar_photo'] = aadhaar_photo



@anvil.server.callable
def add_lendor_four_form(street_adress_1,street_address_2,city,user_id):
  row = app_tables.user_profile.search(customer_id = user_id)
  if row:
    row[0]['street_adress_1'] = street_adress_1
    row[0]['street_address_2'] = street_address_2
    row[0]['city'] = city


                          
@anvil.server.callable
def add_lendor_five_form(pincode,state,country,user_id):
  row = app_tables.user_profile.search(customer_id = user_id)
  if row:
    row[0]['state'] = state
    row[0]['country'] = country
    row[0]['pincode'] = pincode



@anvil.server.callable
def add_lendor_six_form(lending_type, investment,lending_period, user_id):
  row = app_tables.lender.add_row(investment=investment, lending_type=lending_type,lending_period=lending_period,customer_id = user_id)
    
    
@anvil.server.callable
def add_lendor_individual_form_1(company_name,org_type,emp_type,user_id):
  row = app_tables.user_profile.search(customer_id = user_id)
  if row:
    row[0]['company_name']=company_name
    row[0]['organization_type']=org_type
    row[0]['employment_type']=emp_type

    

@anvil.server.callable
def add_lendor_individual_form_2(business_phone_number, landmark,comp_address,user_id):
  row = app_tables.user_profile.search(customer_id = user_id)
  if row:
    row[0]['business_no']=business_phone_number
    row[0]['company_landmark']=landmark
    row[0]['company_address']=comp_address      


@anvil.server.callable
def add_lendor_individual_form_3(annual_salary, designation,emp_id_proof,last_six_month,user_id):
  row = app_tables.user_profile.search(customer_id = user_id)
  if row:
    row [0]['annual_salary']=annual_salary
    row[0]['designation'] = designation
    row[0]['emp_id_proof']=emp_id_proof
    row[0]['last_six_month_bank_proof']=last_six_month

@anvil.server.callable
def add_lendor_institutional_form_1(business_name,business_location,business_add,branch_name,user_id):
  row = app_tables.user_profile.search(customer_id = user_id)
  if row:
    row[0]['business_name'] = branch_name
    row[0]['business_location'] = business_location
    row[0]['business_add'] = business_add
    row[0]['branch_name'] = branch_name

@anvil.server.callable
def add_lendor_institutional_form_2(nearest_loc,business_type,empolyees_working,year_estd,user_id):
  row = app_tables.user_profile.search(customer_id = user_id)
  if row:
    row[0]['nearest_location'] = nearest_loc
    row[0]['business_type'] = business_type
    row[0]['employees_working'] = empolyees_working
    row[0]['year_estd'] = year_estd

@anvil.server.callable
def add_lendor_institutional_form_3(industry_type,six_monthturnover,last_six_statments,user_id):
  row = app_tables.user_profile.search(customer_id = user_id)
  if row:
    row[0]['industry_type'] = industry_type
    row[0]['six_month_turnover'] = six_monthturnover
    row[0]['last_six_month_bank_proof'] = last_six_statments

@anvil.server.callable
def add_lendor_institutional_form_4(director_name,director_no,din,cin,user_id):
  row = app_tables.user_profile.search(customer_id = user_id)
  if row:
    row[0]['director_name'] = director_name
    row[0]['director_no'] = director_no
    row[0]['din'] = din
    row[0]['cin'] = cin

@anvil.server.callable
def add_lendor_institutional_form_5(reg_office_add,off_add_proof,proof_verification,user_id):
  row = app_tables.user_profile.search(customer_id = user_id)
  if row:
    row[0]['registered_off_add'] = reg_office_add
    row[0]['off_add_proof'] = off_add_proof
    row[0]['proof_verification'] = proof_verification

@anvil.server.callable
def add_lendor_bank_details_form_1(account_name, account_type,account_number,bank_name, user_id):
  row = app_tables.user_profile.search(customer_id = user_id)
  if row:
    row[0]['account_name'] = account_name
    row[0]['account_type'] = account_type
    row[0]['account_number'] = account_number
    row[0]['select_bank'] = bank_name


@anvil.server.callable
def add_lendor_bank_details_form_2(ifsc,salary_type,branch_name, user_id):
  row = app_tables.user_profile.search(customer_id = user_id)
  if row:
    row[0]['ifsc_code'] = ifsc
    row[0]['salary_type'] = salary_type
    row[0]['branch_name'] = branch_name
    row[0]['usertype'] = 'lender'
    row[0]['last_confirm'] = True



#--- lender reg was completed ---#



# this one for dashboard start 

# code for rta 
@anvil.server.callable
def add_rtr_form(final_rta, available_balance):
  #row = app_tables.lender.search()
  row = app_tables.lender.search(tables.order_by("lender_accepted_timestamp", ascending=False))
  if row:
    row[0]['final_rta'] = final_rta
    row[0]['available_balance'] = available_balance

@anvil.server.callable
def add_top_up_amount(top_up):
  row= app_tables.top_up.search()
  if row:
    top_up = int(top_up)
    row[0]['top_up_amount'] = top_up



#code for foreclose request

@anvil.server.callable
def search_user(query):
  result=app_tables.foreclose.search()
  if query:
    result=[
    x for x in result
    if query in x["customer_id"]
    ]
  return result

  
# In your Anvil server module (e.g., server_module.py)

import anvil.server
from anvil.tables import app_tables

@anvil.server.callable
def get_user_data(user_id):
    user = app_tables.user_profile.get(customer_id = user_id)
    if user:
        return {
            'full_name': user['full_name'],
            'gender': user['gender'],
            'date_of_birth': user['date_of_birth'],
            'mobile': user['mobile'],
            'another_email': user['another_email'],
            'aadhaar_no': user['aadhaar_no'],
            'pan_number' : user['pan_number'],
            'qualification': user['qualification'],
            'street_adress_1': user['street_adress_1'],
            'street_address_2': user['street_address_2'],
            'city': user['city'],
            'pincode': user['pincode'],
            'state': user['state'],
            'country': user['country'],
            #'lending_type': user['lending_type'],
            #'investment': user['investment'],
            #'lending_period': user['lending_period'],
            'employment_type': user['employment_type'],
            'organization_type': user['organization_type'],
            'company_name': user['company_name'],
            'business_no': user['business_no'],
            'company_landmark': user['company_landmark'],
            'company_address': user['company_address'],
            'business_name': user['business_name'],
            'business_add': user['business_add'],
            'business_location': user['business_location'],
            'branch_name': user['branch_name'],
            'nearest_location': user['nearest_location'],
            'business_type': user['business_type'],
            'employees_working': user['employees_working'],
            'year_estd': user['year_estd'],
            'industry_type': user['industry_type'],
            'six_month_turnover': user['six_month_turnover'],
            'director_name': user['director_name'],
            'director_no': user['director_no'],
            'din': user['din'],
            'cin': user['cin'],
            'registered_off_add': user['registered_off_add'],
            'off_add_proof': user['off_add_proof'],
            'account_name': user['account_name'],
            'account_type': user['account_type'],
            'account_number': user['account_number'],
            'select_bank': user['select_bank'],
            'ifsc_code': user['ifsc_code'],
            'salary_type': user['salary_type'],
            'branch_name': user['branch_name'],
            'net_bank': user['net_bank']
          
            
        }
    else:
        return None


# code for wallet
import anvil.server
from anvil import tables, app

# @anvil.server.callable
# def get_user_details(email_user):
#     # user = tables.user_profile.search(email_user=app.user['email_user'])  
#     user = app_tables.user_profile.get(email_user = email_user)
#     if user:
#         return {
#             'user_email': user['email_user'],
#             'customer_id': user['customer_id'],
#             'full_name': user['full_name']
#         }
#     return None

# @anvil.server.callable
# def create_wallet(user_email, customer_id, full_name):
#     wallet_id = generate_wallet_id()
#     try:
#         wallet_row = tables.wallet.add_row(
#             wallet_id=wallet_id,
#             lender_email=user_email,
#             lender_customer_id=customer_id,
#             lender_full_name=full_name
#         )
#         tables.wallet._save_changes()
#         anvil.server.log("Wallet created successfully.")
#     except Exception as e:
#         anvil.server.log(f"Error creating wallet: {str(e)}")

# def generate_wallet_id():
#     latest_wallet = tables.wallet.search(limit=1, order_by=tables.wallet['wallet_id'], ascending=False)
#     if latest_wallet:
#         latest_id = latest_wallet[0]['wallet_id']
#         numeric_part = int(latest_id[2:]) + 1
#         wallet_id = 'WA' + str(numeric_part).zfill(3)
#     else:
#         wallet_id = 'WA001'
#     return wallet_id

# @anvil.server.callable
# def add_wallet(wallet_id, user_id):
#   app_tables.wallet.add_row(
#     wallet_id = wallet_id,
#     lender_customer_id = user_id
#   )

# code for wallet deposit money
import anvil.server
@anvil.server.callable
def deposit_money_to_wallet(amount):
    # Accessing the current user's wallet record (assuming it's associated with the user)
    user = anvil.users.get_user()
    if user:
        wallet = app_tables.wallet.get(customer_id = user_id)

        # Update the 'lender_wallet_amount' in the user's wallet
        if wallet:
            wallet['lender_wallet_amount'] += amount
            wallet.save()
            return True  # Return True if the deposit was successful
        else:
          return False  # Return False if wallet record not found for the user

    else:
      return False # Return False if user is not logged in