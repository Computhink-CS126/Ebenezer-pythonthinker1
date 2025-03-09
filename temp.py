# name = input("What is your name?")
# print("Nice to meet you, " + name + "!")


# start = int(input("What is the starting number? "))
# stop = int(input("What is the ending number? "))
# if stop > start:
#     stop = stop + 1
# else:
#     stop = stop - 1

# Increment = int(input("What is the Increment? "))

# for i in range(start, stop, Increment):
#     print(i)





























total_score = 0

Ans_1 = input("What is the capital of Spain? (Blond edition): ")
if Ans_1 == "S":
    print("Correct!")
    total_score = total_score + 1
elif Ans_1 == "s":
    print("Correct!")
    total_score = total_score + 1
else:
    print("WRONG!!!!!!")

Ans_2 = input("How does a blonde brain cell die?")
if Ans_2 == "Alone":
    print("Correct!")
    total_score = total_score + 1
elif Ans_2 == "alone":
    print("Correct!")
    total_score = total_score + 1
else:
    print("WRONG!!!!!")

print("You got " + str(total_score) + "correct.")
