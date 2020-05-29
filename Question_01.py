# Author: Jamal Huraibi, fh1328
# Assignment []
# Question []

if __name__ == '__main__':
    
    for num in range(1, 101):
        isDivisibleByThree = num % 3 == 0
        isNotDivisibleByTwo = num % 2 != 0
        
        if isDivisibleByThree & isNotDivisibleByTwo:
            # print(num, end=',')
            # sys.stdout.write(str(num))
            print(num, end=', ')
    
print('\b\b')      # Delete the trailing "end" arg ", "
