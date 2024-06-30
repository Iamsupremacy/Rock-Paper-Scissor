import random
user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissor"]

while True:
    user_guess = input("Pick from ROCK PAPER SCISSOR or Q for Quit: \n").lower()
    if user_guess == "q":
        break
    if user_guess not in options:
        continue

    random_number = random.randint(0, 2)
    computer_guess = options[random_number]
    print("Computer picked", computer_guess + ".")

    if user_guess == "rock" and computer_guess == "scissor":
        print("You won!!")
        user_wins += 1
    elif user_guess == "paper" and computer_guess == "rock":
        print("You won!!")
        user_wins += 1
    elif user_guess == "scissor" and computer_guess == "paper":
        print("You won!!")
        user_wins += 1
    else:
        if user_guess == computer_guess:
         print("Match tie")
        else:
            print("You lost!!")
            computer_wins += 1




print("Goodbye!!")

