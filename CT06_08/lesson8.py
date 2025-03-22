import random
ans = int(random.randint(1, 10))
guess = int(input("Guess a number between 1 and 10."))
if guess == ans:
    print("Congratulations! your answer is correct :)")
else:
    print("Your answer was incorrect, the correct answer was " + str(ans) + ", you will now die. ( ͡° ͜ʖ ͡°) ▄︻デ══━一💥")






NOofQuestions = int(input("How many questions do you want?"))
for i in range(NOofQuestions):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    userguess = int(input("What is " + (num1) + " x " + str(num2) + "?"))
    if userguess == num1 * num2 :
        print("Correct!")
    else:
        print