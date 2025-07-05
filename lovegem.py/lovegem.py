import random

def love_gem():
    user_first_input = input("Enter First Name ")
    user_Second_input = input("Enter second Name ")

    percentage = random.randint(0 , 100 )

    print("love compatibiThelity between " , {user_first_input} , "and" , {user_Second_input} , "is" , percentage)

love_gem()

while True:
    love_gem()
    again = input("Try again? (yes/no): ").lower()
    if again != "yes":
        break
#I will add more features soon.#
#𓅆 Squaaawk!#
