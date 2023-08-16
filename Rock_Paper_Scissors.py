import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
games_images = [rock, paper, scissors]
user_ans = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))
if user_ans >= 3 or user_ans < 0:
    print("You typed an invalid number, you lose")
else:
    print(games_images[user_ans])

computer_ans = int(random.randint(0, 2))
print("Computer chose: \n")
print(games_images[computer_ans])

if user_ans == 0 and computer_ans == 2:
    print("You Wins!")
elif computer_ans > user_ans:
    print("You Loses!")
elif computer_ans < user_ans:
    print("You Wins!")
elif computer_ans == user_ans:
    print("It's a draw")
elif computer_ans == 0 and user_ans == 2:
    print("You Lose")
