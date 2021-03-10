import math
import random

codes=[]
gameOver = False
numGuesses=1

for i in range(4):
  codes.append(int(random.uniform(1,10)))

for i in range(4):
  print(codes[i])

while(gameOver == False):
  guess=[]
  numCorrect=0

  print("Try to guess the 4-Digit Secret Code!")
  for i in range(4):
    newDigit=int(input("Enter a digit: "))
    guess.append(newDigit)
  for i in range(4):
    if(guess[i] == codes[i]):
      numCorrect = numCorrect+1
  if(numCorrect < 4):
    print("Sorry, that was incorrect. You got " + str(numCorrect) + " digits of the code correct.")
    numGuesses=numGuesses+1
  else:
    print("Congratulations! You guessed the secret code. It only took you " + str(numGuesses) + " tries.")
    gameOver=True
  





