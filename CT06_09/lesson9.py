import random
yos = False
while yos != True:
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    num3 = random.randint(1, 6)
    num11 = ( num1 % 2 ) == 0
    num22 = ( num2 % 2 ) == 0
    num33 = ( num2 % 2 ) == 0
    yos = num11 == num22 == num33  
    yos = str(yos)
    print("the first number is: " + str(num1))
    print("the second number is: " + str(num2))
    print("the third number is: " + str(num3))
    print("All numbers are even/odd: " + yos)



