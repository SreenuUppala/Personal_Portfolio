import random
print("Welcome To Guessing Game")
print("You Can Guess a number between 1 To 100")
secret_num=random.randint(1,100)
while True:
    try:
        user_guess = int(input("Guess a number: "))
        if user_guess <= 0 :
            raise ValueError(" Enter a invalid input")
        if user_guess>100:
            raise ValueError(" range should be between 1 To 100")
        if secret_num < user_guess:
            print("You guessed Too High")
        elif secret_num > user_guess:
            print("You guessed Too Low")
        else:
            print("You guessed right!")
            break
    except ValueError as e:
        print("ValueError",e)
