# name = input("What is your name?")
# print("Nice to meet you, " + name + "!")


start = int(input("What is the starting number? "))
stop = int(input("What is the ending number? "))
if stop > start:
    stop = stop + 1
else:
    stop = stop - 1

Increment = int(input("What is the Increment? "))

for i in range(start, stop, Increment):
    print(i)


print(5 + "John")