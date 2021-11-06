#Number 2: Reccursive Power Method . assume that the exponent is a nonnegative interger
def main(): #defining the function
    x = int(input("Enter number to be raise:"))#input to get user's number to be raised
    y = int(input("Enter the exponent:"))#ask user to enter . Note to assume exponent is a nonnegative integer
    result = raised(x,y)
    print(result)

def raised(x,y):    
    if y == 0: #The base call
        return 1
    else:# The recursive call that is greater than 0
       return x ** y
main() #calling the function


    
    
    
    
    
