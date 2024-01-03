from ._anvil_designer import check_out_formTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import borrower_main_form_module as main_form_module
from anvil import app as anvil_app
class check_out_form(check_out_formTemplate):
  def __init__(self, product_group, product_cat,loan_amount, tenure,user_id, **properties):
        self.proctct_g = product_group
        self.prodct_cate = product_cat
        self.userId = user_id
        self.loan_amount = loan_amount
        self.tenure = tenure
        # self.loan_id = loan_id
        self.Total_Repayment_Amount = 0 
        
    
    
        self.init_components(**properties)
        # loan_details = anvil_app.tables.loan_details.search(borrower_customer_id=user_id)
        # if loan_details:
        #   self.label_2.text = f"['loan_amount']"
        #   self.label_6.text = f"['tenure']"
        # else:
        #   self.label_2.text = f"None"
        #   self.label_6.text = f"None"
        user_request = app_tables.product_details.get(product_categories=self.prodct_cate)
        if user_request:
            self.roi = user_request['roi']
            self.processing_fee = user_request['processing_fee']
            self.membership_type = user_request['membership_type']
        self.label_2.text = f"₹ {self.loan_amount}"
        self.label_6.text = self.tenure
        self.label_4.text = f"{self.roi}%"
        p = float(self.loan_amount)
        t = self.tenure
        r = float(self.roi/100)
        interest_amount =  p*r
        # interest_amount = float((((p/r)*t)/100)/12)
        self.label_8.text = f"₹ {int(interest_amount)}"
        self.label_10.text = f" {self.processing_fee}%"
        processing_fee_amount = float((self.processing_fee/100)*p)
        self.label_16.text = f"₹ {int(processing_fee_amount)}"
        self.Total_Repayment_Amount = float(p+interest_amount+processing_fee_amount)
        Monthly_EMI = int(self.Total_Repayment_Amount/float(t))
        self.label_14.text = f"₹ {int(Monthly_EMI)}"
        self.label_12.text = f"₹ {int(self.Total_Repayment_Amount)}"
        self.rich_text_1.content = f"Here is a summary of the details of the {self.prodct_cate}. "

  # choose lender

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_dashboard.new_loan_request')


  def submit_click(self, **event_args):
    user_id = self.userId
    loan_amount = self.loan_amount
    tenure = self.tenure
    interest_rate = self.roi
    total_repayment_amount = self.Total_Repayment_Amount
    monthly_emi = self.label_14.text
    membership_type = self.membership_type
    processing_fee = self.processing_fee
    processing_fee_amount = self.label_16.text

    anvil.server.call('add_loan_details',loan_amount,tenure,user_id,interest_rate,total_repayment_amount)

    # self.id = 'LA' + str(1000)  
    # self.label_18.text = self.id
    # self.data = tables.app_tables.loan_details.search()

    # a = -1
    # self.list_1 = []

    # for i in self.data:
    #         a += 1
    #         self.list_1.append(i['loan_id']) 
    # if a == -1:
    #         self.id = 'LA' + str(1000)
    #         self.label_18.text = self.id
    # else:
    #         last_loan_id = self.list_1[-1]
    #         numeric_part = last_loan_id[2:]
    #         self.id = 'LA' + str(int(numeric_part) + 1)
    #         self.label_18.text = self.id


    # loan_id=self.id
    # app_tables.loan_details.add_row(loan_id = loan_id)

    # borrower_customer_id=user_id
    # loan_amount=loan_amount
    # tenure=tenure
    # interest_rate=interest_rate
    # total_repayment_amount=total_repayment_amount
    # monthly_emi=monthly_emi
    # membership_type=membership_type
    # processing_fee=processing_fee
    # processing_fee_amount=processing_fee_amount
    alert("Request Submited")
    open_form('bank_users.borrower_dashboard')

  # def submit_click(self, **event_args):
  #     user_id = self.userId
  #     loan_amount = self.label_2.text
  #     tenure = self.label_6.text
  #     interest_rate = self.roi
  #     total_repayment_amount = self.Total_Repayment_Amount
  #     monthly_emi = self.label_14.text
  #     membership_type = self.membership_type
  #     processing_fee = self.processing_fee
  #     processing_fee_amount = self.label_16.text
  #     self.id = 'LA' + str(1000)  
  #     self.loan_id = self.id
  #     self.data = tables.app_tables.loan_details.search()

  #     a = -1
  #     self.list_1 = []

  #     for i in self.data:
  #           a += 1
  #           self.list_1.append(i['loan_id']) 
  #     if a == -1:
  #           self.id = 'LA' + str(1000)
  #           self.loan_id = self.id
  #     else:
  #           last_loan_id = self.list_1[-1]
  #           numeric_part = last_loan_id[2:]
  #           self.id = 'LA' + str(int(numeric_part) + 1)
  #           self.loan_id = self.id
  #     loan_id = self.loan_id
  #     open_form('bank_users.borrower_dashboard.choose_lender',self.userId,self.label_2.text,self.label_6.text,self.roi,self.Total_Repayment_Amount,self.label_14.text,self.membership_type,self.processing_fee,self.label_16.text)


  def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('bank_users.borrower_dashboard')

  
  def fetch_product_data(self):
        return app_tables.product_details.search(
            product_name=self.proctct_g,
            product_categories=self.prodct_cate
        )

  def display_label_text(self, label, column_name):
        product_data = self.fetch_product_data()
        if product_data:
            label_text = [str(data[column_name]) for data in product_data]
            label.text = label_text[0] if label_text else None

  # def label_4_show(self, **event_args):
  #   self.display_label_text(self.label_4, 'roi')


# def label_2_show(self, **event_args):
#     borrower_customer_id = self.borrower_customer_id
#     loan_amount = anvil.server.call('add_loan_details', borrower_customer_id)
#     if loan_amount is not None:
#         self.label_2.text = f"Loan Amount: {loan_amount}"
#     else:
#         self.label_2.text = "Loan Amount not available"

  # def label_2_show(self, **event_args):
  #   self.display_label_text(self.label_2,self.loan_amount)

  # def label_6_show(self, **event_args):
  #   self.display_label_text(self.label_6,self.tenure)


