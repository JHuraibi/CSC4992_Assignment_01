# Author: Jamal Huraibi, fh1328
# Assignment: 1
# Question: 2


class QuadraticHelper:
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
        self.sqComponent = None
        self.bComponent = None
        self.most_recent_variable = None
        self.imaginary_flag = None

    def check_valid(self, value_entered):
        # [This comment after Submitted]: Like Assignment 02, why does strip() not work?
        value_entered = value_entered.replace('.', '')                          # isDigit() cannot handle decimal (.)
        value_entered = value_entered.replace('-', '')                          # isDigit() cannot handle neg sign (-)
    
        if self.most_recent_variable == 'a':
            return value_entered.isdigit() & (float(value_entered) != 0.0)      # Extra check for var 'a': cannot be 0.0
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
        
        self.bComponent = -b                                                    # Negative of 'b' value user entered
        self.sqComponent = math.sqrt(abs(under_sqrt)) / 2*a                     # Sqrt of abs (b^2 - 4ac) / 2*a
        self.imaginary_flag = under_sqrt < 0.0                                  # Is (b^2 - 4ac) negative?
        
    def print_formatted_answer(self):
        
        if self.imaginary_flag:                                                 # Append 'i' if flag was triggered
            output_modifier = "i"
        else:
            output_modifier = ""
            
        print("\nFor a = {}, b = {}, and c = {}:"
              .format(self.a, self.b, self.c))                                  # Print original numbers entered by user
        
        print("x = {} + {:.4f}{}".format(self.b, self.sqComponent, output_modifier))
        print("x = {} - {:.4f}{}".format(self.b, self.sqComponent, output_modifier))
        
    
if __name__ == '__main__':
    quadraticHelper = QuadraticHelper()
    
    quadraticHelper.get_input('a')                                              # Get inputs from user
    quadraticHelper.get_input('b')
    quadraticHelper.get_input('c')
    quadraticHelper.solve_quadratic()                                           # Initiate the quadratic calculations
    
    quadraticHelper.print_formatted_answer()                                    # Print final answer/message
