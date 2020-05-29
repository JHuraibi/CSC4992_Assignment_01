# Author: Jamal Huraibi, fh1328
# Assignment 1
# Question 3


class SaleHelper:
    def __init__(self):
        self.bill_subtotal = None
        self.sales_tax_rate = None
        self.tip_rate = None
        self.tax_amount = None
        self.tip_amount = None
        self.bill_total = None

    @staticmethod
    def check_valid(value_entered):
        import re
        tokens = re.split("[.]", value_entered)
        
        if len(tokens) > 2:
            return False
        
        for token in tokens:
            if not str(token).isdigit():
                return False
        
        return True

    def get_inputs(self):
        self.__get_input_bill()                                                 # Get bill subtotal
        self.__get_input_sales_tax_rate()                                       # Get sales tax rate (as %)
        self.__get_input_tip_rate()                                             # Get tip rate (as %)
    
    def __get_input_bill(self):
        print("Please Enter the Bill Amount: $", end="")                        # Prompt user for bill subtotal
        value = input()
    
        while not self.check_valid(value):                                      # Ensure bill subtotal valid
            print("\nThe value entered was invalid.", end='\n')                 # Reattempt if provided invalid input
            print("Please Enter the Bill Amount: $", end="")
            value = input()
        
        self.bill_subtotal = float(value)
        
    def __get_input_sales_tax_rate(self):
        print("Please Enter the Sales Tax Rate: ", end="")                      # Prompt user for sales tax rate (%)
        value = input()
    
        while not self.check_valid(value):                                      # Ensure tax rate valid
            print("\nThe value entered was invalid.", end='\n')                 # Reattempt if provided invalid input
            print("Please Enter the Sales Tax: ", end="")
            value = input()
        
        self.sales_tax_rate = float(value)
        
    def __get_input_tip_rate(self):
        print("Please Enter the Tip Rate: ", end="")                            # Prompt user for tip rate (%)
        value = input()
    
        while not self.check_valid(value):                                      # Ensure tip rate valid
            print("\nThe value entered was invalid.", end='\n')                 # Reattempt if provided invalid input
            print("Please Enter the Tip Rate: ", end="")
            value = input()
        
        self.tip_rate = float(value)
    
    def calculate_total_bill(self):
        bill_subtotal = self.bill_subtotal
        sales_tax_rate = self.sales_tax_rate
        tip_rate = self.tip_rate
        
        self.tax_amount = bill_subtotal * (sales_tax_rate / 100)                # Subtotal times tax rate in %
        self.tip_amount = bill_subtotal * (tip_rate / 100)                      # Subtotal times tip rate in %
        
        self.bill_total = bill_subtotal + self.tax_amount + self.tip_amount     # Add bill subtotal, tax, and tip

    def print_bill(self):
        print("Dear User,")
        print("Your bill amount is: $", self.bill_subtotal)                    # Print bill subtotal
        print("Your tax amount is: $", self.tax_amount)                        # Print tax amount
        print("Your tip amount is: $", self.tip_amount)                        # Print tip amount
        print("****************************************")
                                                                                # Total bill amount, to 2 decimal places
        print("Your Total Bill, including sales tax and tip is ${:.2f}".format(self.bill_total))
    
    
if __name__ == '__main__':
    sale = SaleHelper()
    
    sale.get_inputs()
    sale.calculate_total_bill()
    sale.print_bill()