#function that evaluates the number entered by user
def evaluateNum(n):
        n = number
                        
        if number % 2 == 1 and number < 60:
                print('Odd')

        elif number % 2 == 0 and number >=2 and number < 25:
                print('Even and less than 25')

        elif number % 2 == 0 and number >= 26 and number <=60:
                print('Even')

        elif number % 2 == 0 and number >=60:
                print(number, 'Even')

        elif number % 2 == 1 and number > 60:
                print(number, 'Odd & over 60')

#Asks user to enter name
name = input("Enter your name: ")
#All print() functions print blank lines for program spacing
print()

#prints a hello message with user name(custom)
print("Hello " + name + "!")

print()

#Asks user to input a number between 1 and 100
number = int(input("Please enter a number between 1 and 100: "))
#while loops that checks if number entered by user is between 1 and 100
while number < 1 or number > 100:
        #prints a message if number is not between 1 and 100
        print(name + ", the number must be between 1 and 100")
        print()
        #program loops and asks user to enter another number if first value
        #was not between 1 and 100
        number = int(input("Please enter a number between 1 and 100: "))
        #Calls the evaluateNum function if number meets requirements
evaluateNum(number)
        
                    
