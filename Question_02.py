# Author: Jamal Huraibi, fh1328
# Assignment: 1
# Question: 2


class QuadraticHelper:
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
        self.pos_x = None
        self.neg_x = None
        self.most_recent_variable = None
        self.imaginary_flag = None

    def check_valid(self, value_entered):
        if self.most_recent_variable == 'a':
            return str(value_entered).isdigit() & (value_entered != 0.0)        # Extra check for 'a', cannot be 0
        else:
            return str(value_entered).isdigit()                                 # Was input a digit?
        
    def get_input(self, for_which_var):                                         # for_which_var indicates a, b, or c
        self.most_recent_variable = for_which_var                               # Record variable we're working for
        print("Please Enter the Value of '{}': ".format(for_which_var), end="")  # Prompt user for input
        value = input()
        
        while not self.check_valid(value):                                      # Ensure input was valid (i.e. a digit)
            print("\nThe value entered was invalid.", end='\n')                 # Reattempt if provided invalid input
            print("Please Enter the Value of '{}': ".format(for_which_var), end="")
            value = input()
            
        self.store_input_value(float(value))                                    # Store user-entered value

    def store_input_value(self, value):
        if self.most_recent_variable == 'a':                                    # Most-recent variable (i.e. a, b, or c)
            self.a = value
        elif self.most_recent_variable == 'b':
            self.b = value
        elif self.most_recent_variable == 'c':
            self.c = value
        else:
            print("Error with Variable Identification")
    
    def solve_quadratic(self):
        import math
        a = self.a
        b = self.b
        c = self.c

        # Intermediate variables
        under_sqrt = b**2 - (4*a*c)                                             # Proactive handling negative under root
        denominator = 2*a                                                       # Denominator
        
        pos_x_numerator = (-b) + math.sqrt(abs(under_sqrt))                     # Numerators (plural!)
        neg_x_numerator = (-b) - math.sqrt(abs(under_sqrt))
        
        self.pos_x = pos_x_numerator / denominator                              # Calculator the positive x value
        self.neg_x = neg_x_numerator / denominator                              # Calculator the negative x value
        self.imaginary_flag = under_sqrt < 0.0                                  # Was (b^2 - 4ac) negative?
        
    def print_formatted_answer(self):
        if self.imaginary_flag:                                                 # Append 'i' if flag was triggered
            output_modifier = "i"
        else:
            output_modifier = ""
            
        print("\nFor a = {}, b = {}, and c = {}:"
              .format(self.a, self.b, self.c))                                  # Print original numbers entered by user
        print("+x = {:e}{}".format(self.pos_x, output_modifier))                # Positive x (in scientific notation)
        print("-x = {:e}{}".format(self.neg_x, output_modifier))                # Negative x (in scientific notation)
        
    
if __name__ == '__main__':
    quadraticHelper = QuadraticHelper()
    
    quadraticHelper.get_input('a')                                              # Get inputs from user
    quadraticHelper.get_input('b')
    quadraticHelper.get_input('c')
    quadraticHelper.solve_quadratic()                                           # Initiate the quadratic calculations
    
    quadraticHelper.print_formatted_answer()                                    # Print final answer/message
