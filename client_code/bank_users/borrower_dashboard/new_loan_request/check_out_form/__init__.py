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
        self.label_2.text = f"₹ {self.loan_amount}"
        self.label_6.text = self.tenure
        self.label_4.text = f"{self.roi}%"
        p = float(self.loan_amount)
        t = float(self.tenure)
        r = float(self.roi/100)
        interest_amount =  p*r
        # interest_amount = float((((p/r)*t)/100)/12)
        self.label_8.text = f"₹ {int(interest_amount)}"
        self.label_10.text = f" {self.processing_fee}%"
        processing_fee_amount = float((self.processing_fee/100)*p)
        self.label_16.text = f"₹ {int(processing_fee_amount)}"
        self.Total_Repayment_Amount = float(p+interest_amount+processing_fee_amount)
        Monthly_EMI = float(self.Total_Repayment_Amount/t)
        self.label_14.text = f"₹ {int(Monthly_EMI)}"
        self.label_12.text = f"₹ {int(self.Total_Repayment_Amount)}"
        self.rich_text_1.content = f"Here is a summary of the details of the {self.prodct_cate}. "

  # choose lender
  def submit_click(self, **event_args):
      user_id = self.userId
      loan_amount = self.label_2.text
      tenure = self.label_6.text
      interest_rate = self.roi
      total_repayment_amount = self.Total_Repayment_Amount
      monthly_emi = self.label_14.text
      open_form('bank_users.borrower_dashboard.choose_lender',)

  def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('bank_users.borrower_dashboard.new_loan_request')

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


