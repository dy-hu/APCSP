#Daniel Hu - AP CSP - 3/8
import math
import random

def compare(num1,num2):
  if(num1<num2):
    print(str(num1) + " is less than " + str(num2))
  elif(num1>num2):
    print(str(num1) + " is greater than " + str(num2))
  else:
    print(str(num1) + " is equal to " + str(num2))

def eliminate(x):
  random.shuffle(names)
  for i in range (0,x):
    names.pop(i)
  return names

for i in range (0,3):
  number1 = int(input("Give me an integer: ")) 
  number2 = int(input("Give me a second integer: "))
  compare(number1,number2)

names=[]
for i in range (0,6):
  name = input("Give me a name: ")
  names.append(name)
n = int(input("How many people do you want to eliminate?"))
survivors=eliminate(n)
for i in range (0, len(survivors)):
  print(survivors[i])


