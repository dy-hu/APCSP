for i in range (1,101):
  print(str(i))

for i in range (50,66):
  print(str(i))

x=100
while x <= 147:
  if x%2==1:
    print(str(x))
  x = x+1

for i in range (0,52,3): 
  print(str(i))

for i in range (10,1001,10):
  print(str(i))

num = int(input("Pick a number from 1 to 100: "))

if not (num < 1 or num > 100):
  print("Thank you for your input!")
else:
  while (num < 1 or num > 100):
    print("Invalid number! Try again.")
    num = int(input("Pick a number from 1 to 100: "))

numGuesses=1
favColor = "Orange"
color=input("What's my favorite color? ")
while not(color==favColor):
  print("Incorrect! Try again")
  color=input("What's my favorite color?")
  numGuesses = numGuesses + 1
if(color==favColor):
  print("Correct! It took you " + str(numGuesses) + " tries to find my favorite color")

  total=0
  counter=int(input("How many numbers do you wish to add? "))

  for i in range (0, counter):
    num=int(input("Input a number to add: "))
    total = total + num

  print("Your total sum is " + str(total))



