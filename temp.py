# name = input("What is your name?")
# print("Nice to meet you, " + name + "!")


start = int(input("What is the starting number?"))
Increment = int(input("What is the Increment?"))
stop = int(input("What is the ending number?"))
if stop > start:
    stop = stop + 1
else:
    stop = stop - 1

for i in range(start, Stop, Increment):
    print(i)