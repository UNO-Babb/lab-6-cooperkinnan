#DiceRoll.py
#Name:Cooper Kinnan
#Date:3/2/2025
#Assignment:Lab 6
import random

def main():
  #Create an empty list with possible roll values
 
  rolls = [0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for i in range(10000):
    dice1= random.randint(1,6)
    dice2= random.randint(1,6)
    total = dice1+dice2
    rolls[total-2] = rolls[total-2] +1
  #find the sum total of the two dice
 
  #print statictics for dice rolls
  print(rolls)
  value = 2
  for r in rolls:
    avg = r /100
    print("You rolled a", str(value) +",", r, "times.  %", avg)
    value = value +1

if __name__ == '__main__':
  main()