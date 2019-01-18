# Create a function with two variables.
# One should equal “My name is: “ and the other should equal your actual name.
# Print the two variables in one print message.

def main():
#     problem1()
#     problem2()
#     problem3()
    problem4()
#     main()
#     name = "My name is "
#     myName = "Chelsea"
#     print(name + myName)

# problem2

# Create a function to ask the user to enter the extra credit they earned.
# If they entered less than 5 print “That’s not enough extra credit.”
# If they entered more than 20 print “That’s too much extra credit”.

# main ()
# def problem2():
#     userInput = int(input("Enter your extra credit points:"))
#     if(userInput<5):
#         print("That's not enough extra credit")
#     elif(userInput>20):
#         print("That's too much extra credit")
#     else:
#         print("No points for you!!!")
#
#
# main()

# Create a function to ask a user to enter a password.
# Enter a password. Ask user to reenter password.
# Check to see if they are correct.

# def problem3():
#
#     userPassword = (input("Enter your password"))
#     userPassword2 = (input("Please reenter your password"))
#     if(userPassword == userPassword2):
#         print("Password has been made")
#     else:
#         print("Password does not work")
#
# if __name__ == '__main__':
#     main()

# Create a function to ask for two card numbers.
# If it equals 21 print BLACKJACK!,
# if it’s greater than 21 print BUST!,
# if it’s less than 21 print “The total is [THE TOTAL]”

def problem4():

    userCard = int(input("Give a card number:"))
    userCard2 = int(input("Give another card number:"))
    if(userCard + userCard2 == 21):
        print("BLACKJACK!!!")
    elif(userCard + userCard2 > 21):
        print("BUST!!")
    elif(userCard + userCard2 < 21):
        print("The total is " + str(userCard + userCard2))

main()


