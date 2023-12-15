import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime


@anvil.server.callable
def add_borrower_step1(full_name,gender,dob,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['full_name'] = full_name
    row[0]['gender'] = gender
    row[0]['date_of_birth'] = dob
    row[0]['form_count']=0

@anvil.server.callable
def add_borrower_3a1_form(street_adress_1,street_address_2,city,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['street_adress_1'] = street_adress_1
    row[0]['street_address_2'] = street_address_2
    row[0]['city'] = city    
    row[0]['form_count']=3
@anvil.server.callable
def add_borrower_step2(mobile_no,user_photo,alternate_email,user_id):
  row=app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['mobile']=mobile_no
    row[0]['user_photo']=user_photo
    row[0]['another_email']= alternate_email
    row[0]['form_count']=1



@anvil.server.callable
def add_borrower_step3(aadhar,aadhar_card,pan,pan_card,user_id):
  row=app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['aadhaar_no']=aadhar
    row[0]['aadhaar_photo']=aadhar_card
    row[0]['pan_number']=pan
    row[0]['pan_photo']=pan_card
    row[0]['form_count']=2


@anvil.server.callable
def add_borrower_step3a(father_name,father_age,mother_name,mother_age,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['father_name'] = father_name
    row[0]['father_age'] = father_age
    row[0]['mother_name'] = mother_name
    row[0]['mother_age'] = mother_age
    row[0]['form_count']=4

@anvil.server.callable
def add_borrower_step3c(status_of_user,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['profficen'] = status_of_user
    row[0]['form_count']=5


@anvil.server.callable
def add_borrower_step4(marital_status,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['marital_status']=marital_status
    row[0]['form_count']=6

@anvil.server.callable
def add_borrower_student(college_name,college_id,college_proof,college_address,user_id):
  row=app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['college_name']=college_name
    row[0]['college_id']=college_id
    row[0]['college_address']=college_address
    row[0]['college_proof']=college_proof
    
    
@anvil.server.callable
def add_borrower_step4a(spouse_name,marrege_date,spouse_mobile_no,user_id):
  row=app_tables.user_profile.search(coustmer_id=user_id)
  if row:
   row[0]['spouse_name']=spouse_name
   row[0]['Date_mariage']=marrege_date
   row[0]['spouse_mobile']=spouse_mobile_no

@anvil.server.callable
def add_borrower_step5(spouse_company_name,spouse_company_address,spouse_profficen,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['spouse_company_name']=spouse_company_name
    row[0]['spouse_company_address']=spouse_company_address
    row[0]['spouse_designation']=spouse_profficen

@anvil.server.callable
def add_borrower_spouse(annual_ctc,office_number,user_id):
  row=app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['spouse_annual_ctc']=annual_ctc
    row[0]['spouse_office_number']=office_number

@anvil.server.callable
def add_borrower_step7(home_loan,other_loan,live_loan,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['running_Home_Loan'] = home_loan
    row[0]['running_or_live loans']= live_loan
    row[0]['other_loan']=other_loan
    row[0]['form_count']=7
@anvil.server.callable
def add_borrower_step8(account_name, account_type,account_number,bank_name, user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['account_name'] = account_name
    row[0]['account_type'] = account_type
    row[0]['account_number'] = account_number
    row[0]['select_bank'] = bank_name  
    row[0]['form_count']=8

@anvil.server.callable
def add_borrower_step9(ifsc,salary_type,select_bank,net_bank, user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['ifsc_code'] = ifsc
    row[0]['salary_type'] = salary_type
    row[0]['select_bank'] = select_bank
    row[0]['net_bank'] = net_bank
    row[0]['usertype'] = 'borrower'
    row[0]['last_confirm'] = True
    row[0]['form_count']=9

# the borrower registration form end hear do not change any code ---#






@anvil.server.callable
def add_loan_details(loan_amount, credit_limit, tenure, user_id):
    # Generate a unique loan ID and get the updated counter
    loan_id = generate_loan_id()

    # Search for the user profile
    user_profiles = app_tables.user_profile.search(coustmer_id=user_id)
    
    if user_profiles and len(user_profiles) > 0:
        # If there is a user profile, get the first one
        user_profile = user_profiles[0]

        # Extract the full name from the user profile
        full_name = user_profile['full_name']
        email_id = user_profile['email_user']
        # Add the loan details to the data table
        app_tables.loan_details.add_row(
            loan_id=loan_id,
            loan_amount=loan_amount,
            credit_limit=credit_limit,
            tenure=tenure,
            coustmer_id=user_id,
            full_name=full_name,
            email_id=email_id,                 
            timestamp=datetime.now()
        )

        # Return the generated loan ID to the client
        return loan_id
    else:
        # Handle the case where no user profile is found
        return "User profile not found"

def generate_loan_id():
    # Query the latest loan ID from the data table
    latest_loan = app_tables.loan_details.search(tables.order_by("loan_id", ascending=False))

    if latest_loan and len(latest_loan) > 0:
        # If there are existing loans, increment the last loan ID
        last_loan_id = latest_loan[0]['loan_id']
        counter = int(last_loan_id[2:]) + 1
    else:
        # If there are no existing loans, start the counter at 100001
        counter = 100001

    # Return the new loan ID
    return f"LA{counter}"







@anvil.server.callable
def update_loan_details(loan_id, emi, total_repayment_amount, interest_rate):
    rows = app_tables.loan_details.search(loan_id=loan_id)

    if rows:
        row = rows[0]
        row['emi'] = emi
        row['total_repayment_amount'] = total_repayment_amount
        row['interest_rate'] = interest_rate
        row.update()
    else:
        raise ValueError(f"Row not found for loan_id {loan_id}")

