#function that evaluates the number entered by user
def evaluateNum(number):
        
                        
        if number % 2 == 1 and number < 60:
                print('Odd')

        elif number % 2 == 0 and number >=2 and number < 25:
                print('Even and less than 25')

        elif number % 2 == 0 and number >= 26 and number <=60:
                print('Even')

        elif number % 2 == 0 and number >=60:
                print(number, ': Even')

        elif number % 2 == 1 and number > 60:
                print(number, ': Odd & over 60')

#function that takes the number that the user enters and checks 
#to make sure it is between 1 and 100
def getNumber(number):
    while number < 1 or number > 100:
            print(name + ", the number must be between 1 and 100")
            print()
            number = int(input("Please enter a number between 1 and 100: "))
    evaluateNum(number)

#Program greeting. Asks for the user's name and prints a greeting
name = input("Enter your name: ")
print()
print("Hello " + name + "!")
print()

#ask the user to enter a number
number = int(input("Please enter a number between 1 and 100: "))

#passes the number through the getNumber function
getNumber(number)


        
                    
