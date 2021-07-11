# Problem 1
# Handle the exception thrown by the code below by using try and except blocks.

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Some error")


# Problem 2
# Handle the exception thrown by the code below by using try and except blocks.
# Then use a finally block to print 'All Done.'

try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print ("Can not divide by error")
finally:
    print("I will always run!")

# Problem 3
# Write a function that asks for an integer and prints the square of it.
# Use a while loop with a try, except, else block to account for incorrect inputs.


def ask():
    while True:
        try:
            number = int(input("Please enter a number you want a square"))
        except TypeError:
            print("An error occurred! Please try again!")
            continue
        except ValueError:
            print("An error occurred! Please try again!")
            continue
        else:
            square = number ** 2
            print(f"Thank you, your number squared is: {square}")
            break


ask()
