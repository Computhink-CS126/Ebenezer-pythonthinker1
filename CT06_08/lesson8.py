import random
ans = int(random.randint(1, 10))
guess = int(input("Guess a number between 1 and 10."))
if guess == ans:
    print("Congratulations! your answer is correct :)")
else:
    print("Your answer was incorrect, the correct answer was " + str(ans) + " you will now die. ")