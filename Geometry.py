import random
import math

num1 = float(input("Give me a small decimal number: "))

num2 = float(input("Give me a large decimal number: "))

final=random.uniform(num1,num2)
print(str(final))

volume = 4/3 * math.pi * math.pow(final,3)

print("The volume of a sphere with radius, " + str(final) + ", is: " + str(volume)) 