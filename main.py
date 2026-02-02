# # the user will choose a number
# # this program will guess the number
# # the user will say "yes" or "higher" or "lower"
# # the program will ask to play again or exit

# import random

# i = 0



# while True:
#     if i == 10:
#         break
#     i = i + 1

#     if i == 4:
#         print("Correct!")

#     else:
#         print("Wrong!")


# input("Is your number 3?")

guess = 2
response = input(f"Is your number {guess}?")
while True:
    if response == "yes":
        print("Yay!")
        break
    elif response == "no":
        response1  =  input(f"Is it higher or lower?")
        if response1 == "lower":
            guess -= 1
            input(f"Is your number {guess}?")
            
        elif response1 == "higher":
            guess += 1
            response = input(f"Is your number {guess}?")
    else:
        response = input(f"Say 'yes' or 'no'. Is your number {guess}?")



