import sys
from os import system, name
from time import sleep
#Function to display Caculator Menu
def UserMenu():
    print("******CalulatorMenu******")
    print(" 1: Addition      ")
    print(" 2: Subtraction   ")
    print(" 3: Multiplication")
    print(" 4: Division      ")
    print(" 5: Exit the program     ")
    userInput = int(input("Enter your choice 1-5  "))
    return userInput
#Function to accept user input
def userInput():
    num1 = int(input(" Enter first number  "))
    num2 = int(input(" Enter second number  "))
    return num1,num2
#Function to Clear screen
def clearscrn():
    if(name== 'posix'):
        system('cls')
    else:
        system('Clear')
#Division Function
def DivideNumbers(num1, num2):
    if (num1 == 0):
        return 0
    elif (num2 == 0):
        print("cannot divide by 0")
    else:
        return(num1 / num2)

#Main Function to accept numbers    
def main():
    #opertaionList = ['+','-','*','/','%']
    #clearscrn()
    #operation = UserMenu()
   # try:
        while True:
            clearscrn()
            operation = UserMenu()
           # if num1.isdigit() and num2.isdigit():
           #     num1 = int(num1)
            #    num2 = int(num2)
           #     if operation in [1,2,3,4,5]:
            match(operation):
                case 1:
                    num1,num2 = userInput()
                    print("Sum of number ",num1 + num2)
                case 2:
                    num1,num2 = userInput()
                    print("Differnce of numbers",num1 - num2)
                case 3:
                    num1,num2 = userInput()
                    print("Product of the number",num1 * num2)
                case 4:
                    num1,num2 = userInput()
                    print("{} Divided by {} is {}".format(num1,num2,DivideNumbers(num1, num2)))
                case 5:
                    print("Exiting Calulator")
                    exit()
                case default:
                    print("Not a valid Operation") 
    
         #       else:
         #           print("Not a Valid operator")       
         #   else:
         #       print("Not Valid Integer")   
            sleep (2)   
    #except:
    #    print("Invalid input")              
            
if __name__ == '__main__':
    sys.exit(main()) 
