#Number Guessing Game:

from random import randint
#Choosing a number between 1 to 100
print(logo)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5    #Constants
turns=0

def check_answer(guess,answer, turns):
  """Checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too High")
    return turns - 1
  elif guess < answer:
    print("Too Low")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

def set_levels():
  level=input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level=="easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1,100) #includes both 1 and 100
  
  turns = set_levels()
  print(f"You have {turns} attempts remaining to guess the number.")
  
  guess = 0
  while guess != answer:
    guess = int(input("Make a guess: "))
    turns = check_answer(guess,answer,turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return 
    elif guess!= answer:
      print("Guess Again!")
      
