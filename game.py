# game.py

# 1) Import all Modules Necessary for this app
import os
import random

from dotenv
import load_dotenv
# 2) Make the desired application

print("-----------------------------")
print("Rock, Paper, Scissors, Shoot!")
print("-----------------------------")

user_input = input("Welcome, please input a User Name: ")
print("-----------------------------")

user_choice = input("Please select either 'rock', 'paper', or 'scissors':")
if user_choice == "rock":
    print(f"{user_input}'s Choice: Rock")
elif user_choice == "paper":
    print(f"{user_input}'s Choice: Paper")
elif user_choice == "scissors":
    print(f"{user_input}'s Choice: Scissors")
else:
    print("Sorry, that input is invalid. Please try again!")
    exit()


rps = ['rock', 'paper', 'scissors']

comp_choice = random.choice(rps)

if comp_choice == "rock":
    print("Computer's Choice: Rock")
elif comp_choice == "paper":
    print("Computer's Choice: Paper")
else:
    print("Computer's Choice: Scissors")

print("-----------------------------")

if comp_choice == "rock" and user_choice ==  "paper" or comp_choice == "scissors" and user_choice == "rock" or comp_choice == "paper" and user_choice == "scissors":
    print(f"You won, {user_input}! Why not go for 2 in a row?!")
elif user_choice == comp_choice:
    print("It's a Tie, could've been worse I guess!")
else:
    print("The computer won, better luck next time!")

print("-----------------------------")

print("Thanks for playing! Please try again!")

print("-----------------------------")
