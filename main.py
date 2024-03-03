# Starter file for Project 2

# Name: Chris Oesterling
# Date: 10/23/22
# Class: ISIT333
# Assignment: Project 2 Rock Paper Scissors

import random

def get_name():
  name = input("What is your name? ")
  print("\nHello " + name, "Would you like to see the rules before you start y/n? ")
  answer = input()
  if answer.lower() == 'y':
    rules()
  else:
    SystemExit
  return name

def rules():
  print("\nYou are to choose between Earth, Wind and Fire,")
  print("Fire > Earth, Earth > Water, Water > Fire")
  print("Good luck!\n")


def game(wins, losses, opponent):
  #oppent options and opponent name
  option = ["Earth", "Water", "Fire"]
  print("Your opponent is " + opponent + "\n")

  #Start game
  item = input("Choose Earth, Water, or Fire?\n")
  rand_opt = random.choice(option)
  if item.lower() == "fire" and rand_opt == "Earth":
    wins += 1
    print("Oppenent chose: " + rand_opt, "You won!\n")
    return wins, losses
  elif item.lower() == "earth" and rand_opt == "Water":
    wins += 1
    print("Oppenent chose: " + rand_opt, "You won!\n")
    return wins, losses
  elif item.lower() == "water" and rand_opt == "Fire":
    wins += 1
    print("Oppenent chose: " + rand_opt, "You won!\n")
    return wins, losses
  elif item.lower() == rand_opt.lower():
    print("Oppenent chose: " + rand_opt)
    print("There's a tie, nobody scores\n")
    return wins, losses
  else:
    losses += 1
    print("Oppenent chose: " + rand_opt, "You lost\n")
    return wins, losses

def rand_opp():
  first_name = ["Walter", "Tom", "John", "Ted", "Jamie"]
  last_name = ["White", "Jerry", "Henry", "Lasso", "Tart"]
  opponent = random.choice(first_name) + " " + random.choice(last_name)
  return opponent
  
def main():
  print("Welcome to the Earth, Fire and Water game!\n")

  #variables
  wins = 0
  losses = 0
  count = 0
  #Get opponent name
  opponent = rand_opp()
  
  #ask for name and rules
  name = get_name()
  answer = input("Press y to start game or n to quit: ")
  while answer.lower() == 'y':
      wins, losses = game(wins, losses, opponent)
      count += 1

      #scores
      print("Wins - " + str(wins), "Losses - " + str(losses) + "\n\n")

      #play again?
      answer = input("would you like to play again y/n? ")

  print("Games played: " + str(count) + "\nFinal score, " + str(wins) + " - " + str(losses))
  print("Bye, " + name + "!")

if __name__ == "__main__":
  main()