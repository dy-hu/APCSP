import random
import math

names = ["Peter", "Bruce", "Steve", "Tony", "Natasha", "Clint", "Wanda", "Hope", "Danny", "Carol"]

numbers = [100,50,10,1,2,7,11,17,53,-8,-4,-9,-72,-64,-80]

count=1
for i in range(len(names)):
  if(not(count%2==0)):
    print(names[i])
  count=count+1

for i in range(len(numbers)):
  if(numbers[i] > 0):
    print(numbers[i])

count=int(random.uniform(1,3))
sum=0
if(count==1):
  for i in range(len(numbers)):
    sum=sum+numbers[i]
  print(sum)
else :
  for i in range(len(numbers)):
    sum=sum+numbers[i]
  avg = sum/len(numbers)
  print(avg)

for i in range(len(numbers)):
  if(not(numbers[i]%2==0)):
    print(numbers[i])

for i in range(len(names)):
  if(not(min(names[i], "Thor") == "Thor")):
    print(min(names[i], "Thor"))

max=0
min=0

for i in range(len(numbers)):
  if(numbers[i] > max):
    max=numbers[i]
  if(numbers[i] < min):
    min=numbers[i]
print("Max: " + str(max))
print("Min: " + str(min))