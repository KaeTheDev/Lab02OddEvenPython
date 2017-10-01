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


name = input("Enter your name: ")
print()

print("Hello " + name + "!")

print()

number = int(input("Please enter a number between 1 and 100: "))
while number < 1 or number > 100:
        print(name + ", the number must be between 1 and 100")
        print()
        number = int(input("Please enter a number between 1 and 100: "))
evaluateNum(number)
        
                    
