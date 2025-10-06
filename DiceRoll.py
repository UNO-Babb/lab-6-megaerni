#DiceRoll.py
#Name: Meg Aerni
#Date: 9.29.2025
#Assignment: Lab 6, Part 1
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0]

  # Number of iterations:
  numIterations = 10000

  #Create two dice values ranging from 1 - 6 each
  for r in range(numIterations):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    diceRoll = dice1 + dice2
    rolls[diceRoll - 2] = rolls[diceRoll - 2] + 1

  #find the sum total of the two dice 
  dice = 2
  for count in rolls:
    percent = (count / numIterations) * 100
    print(f"{dice}: {count} rolls; {round(percent, 2)}%")
    dice = dice + 1
  #print statictics for dice rolls
  print(rolls)

if __name__ == '__main__':
  main()
