#DiceRoll.py
#Name: Meg Aerni
#Date: 9.29.2025
#Assignment: Lab 6, Part 1
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for r in range(100):
    dice1 = random.randint(1, 6)
    rolls[dice1 - 1] = rolls[dice1 - 1] + 1
  dice2 = random.randint(1, 6)
  #find the sum total of the two dice 
  dice = 1
  for count in rolls:
    print(dice, ":", count)
    dice = dice + 1
  #print statictics for dice rolls
  print(rolls)

if __name__ == '__main__':
  main()
