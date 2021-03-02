import random
import math

answer = input("The sky blue? True or False: ")

if answer == "True" or answer == "true" or answer == "T" or answer == "t":
  print("That is correct!")
elif answer == "False" or answer == "false" or answer == "F" or answer == "f":
  print('That is incorrect!')
else:
  print("You entered an invalid answer.")

