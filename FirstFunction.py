######################################
#            FirstFunction           #
#                                    #
#             UTeach CSP             #
#             Brian Ford             #
#                                    #
#              11/12/19              #
#                                    #
######################################

import random
import math

def BMI():
  name = input("Please type your name: ")
  height = float(input("How many inches tall are you: "))
  nheight = height / 39.37
  weight = float(input("How much do you weigh (in pounds): "))
  nweight = weight / 2.205
  bmi = nweight / (nheight * nheight)
  print(name + ", your BMI is " + str(bmi))

def numberGame():
  count = 1
  randnum = random.randint(1, 100)
  print("I am thinking of a number between 1 and 100.")
  guess = int(input("What number am I thinking of? "))
  while guess != randnum:
    if guess < randnum:
      guess = int(input("Too low, guess again: "))
    else:
      guess = int(input("Too high, guess again: "))
    count = count + 1
  print("You guessed correctly, it took you " + str(count) + " tries.")

choice = int(input("""Which of the following would you like to do? Type the number corresponding to the choice.
1) Calculate BMI
2) Play a Game
3) Final Exam - What do I need if...
4) Basic Calculator
"""))

if choice == 1:
  BMI()
elif choice == 2:
  numberGame()
elif choice == 3:
  mp1 = int(input("What was your grade for marking period 1? "))
  mp2 = int(input("What was your grade for marking period 2? "))
  grade = int(input("What grade would you like to have for your overall semester grade? "))
  score = (grade - mp1 * 0.4 - mp2 * 0.4) / 0.2
  print("You will need to score a " + str(score) + " on the final exam.")
elif choice == 4:
  num1 = float(input("Enter your first number: "))
  num2 = float(input("Enter your second number: "))
  operator = input("Which operation do you want to perform?\nAdd \nSubtract \nMultiply \nDivide\n")
  if operator == "Add":
    solution = num1 + num2
    print("You answer is: " + str(solution))
  elif operator == "Subtract":
    solution = num1 - num2
    print("You answer is: " + str(solution))
  elif operator == "Multiply":
    solution = num1 * num2
    print("You answer is: " + str(solution))
  elif operator == "Divide":
    solution = num1 / num2
    print("You answer is: " + str(solution))
  else:
    print("Incorrect math operation. Oof.")
else:
  print("That is an incorrect option.")