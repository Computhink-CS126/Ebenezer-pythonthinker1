import random
num1 = random.randint(1, 6)
num2 = random.randint(1, 6)
num3 = random.randint(1, 6)
num1 = ( num1 % 2 ) == 0
num2 = ( num2 % 2 ) == 0
num3 = ( num2 % 2 ) == 0
boolen = num1 == num2 == num3
print("All numbers are even/odd: " + boolen)