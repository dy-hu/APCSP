import random
import math

result=True

name=input("What's your name?")

num=int(input("Hello, " + name + ". Pick a random number!"))

num2=int(input("Hello, " + name + ". Pick another random number!"))

if num%num2 != 0:
  result=False
  print(result)
  print(str(num) + " is not divisible by " + str(num2))
else:
  result=True
  print(result)
  print(str(num) + " is divisible by " + str(num2))

  