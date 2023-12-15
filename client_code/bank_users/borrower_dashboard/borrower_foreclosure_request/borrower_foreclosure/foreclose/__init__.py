from ._anvil_designer import forecloseTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime

class foreclose(forecloseTemplate):
  def __init__(self, selected_row, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.selected_row = selected_row 
        # Any code you write here will run before the form opens.
    loan_amount = selected_row['loan_amount']
    loan_amount = int(loan_amount)
    payment_done = selected_row['payment_done']
    tenure = selected_row['tenure']  # Assuming tenure is given in months
    tenure = int(tenure)
    monthly_interest_rate = selected_row['interest_rate'] / (12 * 100)  # Assuming interest rate is in percentage
    factor = (1 + monthly_interest_rate) ** tenure  # Calculate (1 + r)^t without using pow
    emi = loan_amount * monthly_interest_rate * factor / (factor - 1)
    emi = int(emi)
    monthly_installment = loan_amount / tenure
    monthly_installment=int(monthly_installment)
    paid_amount = emi * payment_done
    paid_amount = int(paid_amount)
    monthly_interest_amount=emi-monthly_installment
    monthly_interest_amount=int( monthly_interest_amount)

    outstanding_amount= loan_amount - monthly_installment*payment_done
    outstanding_amount = int(outstanding_amount)
    oustanding_month=tenure-payment_done
    outstanding_amount_i_amount=monthly_interest_amount*oustanding_month
    outstanding_amount_i_amount=int(outstanding_amount_i_amount)
    total_outstanding_amount=outstanding_amount+outstanding_amount_i_amount
    

    penalty_rate = 0.03  # 3%
    penalty_amount = outstanding_amount * penalty_rate
    penalty_amount = int(penalty_amount)
    total_due_amount = outstanding_amount + penalty_amount
    total_due_amount = int(total_due_amount)

    self.ra_label.text = f"{outstanding_amount}"
    self.tda_label.text = f"{total_due_amount}"
    self.emi_label.text = f"{emi}"
    self.pa_label.text = f"{penalty_amount}"
    self.paid_label.text = f"{paid_amount}"
    self.mi_label.text = f"{monthly_installment}"
    self.fir_label.text = f"{monthly_interest_amount}"
    self.label_20.text = f"{monthly_installment}"
    self.label_8.text = f"{outstanding_amount_i_amount}"
    self.label_18.text = f"{total_outstanding_amount} "
    self.label_17.text = f"{outstanding_amount}"
    self.label_23.text = f"({payment_done} months)"
    self.label_24.text = f"({oustanding_month} months)"
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_dashboard')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_dashboard.borrower_foreclosure_request.borrower_foreclosure', selected_row= self.selected_row)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    alert('Submitting a foreclosure request implies acknowledgment and acceptance of financial and legal consequences, adhering to established timelines and communication protocols.')

  def button_3_click(self, **event_args):
    
    """This method is called when the button is clicked"""
    if self.f_checkbox.checked:
        # Get the reason entered by the user
        reason = self.reason_textbox.text.strip()

        if reason:
           
                app_tables.foreclosure.add_row(
                    loan_id=self.selected_row['loan_id'],
                    borrower_name=self.selected_row['full_name'],
                    loan_amount=self.selected_row['loan_amount'],
                    outstanding_amount=self.ra_label.text,
                    total_due_amount=self.tda_label.text,
                    emi_amount=self.emi_label.text,
                    paid_amount=self.paid_label.text,
                    penalty_amount=self.pa_label.text,
                    requested_on=datetime.now(),
                    reason=reason
                )
                
               
                #self.button_3.visible = True
                #self.button_4.visible = False

                    # Check if there is an approved foreclosure
                  #foreclosure_status = app_tables.foreclosure.get(status='approved')
                 # if foreclosure_status:
                 #self.button_4.text = foreclosure_status['status']
                 #self.button_4.visible = True
                alert("The Foreclosure Statement will be processed within 15 working days from the date of request. Please place this request to know the principal amount outstanding for closure of loan and applicable charges. If you have provided your mobile number or email, we will inform you about the closure of your request by SMS or email respectively. Providing the mobile number or email here will not result in an update of your mobile number or email as recorded with us. KOTAK Bank does not take any responsibility, and will also not be liable, for your claims if the details provided by you are incorrect/incomplete.")

                open_form('bank_users.borrower_dashboard.borrower_foreclosure_request')
        else:
            alert('Please enter a reason for foreclosure.')
    else:
        alert('Please accept the Terms and Conditions.')
