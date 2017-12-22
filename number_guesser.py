import random
answer = random.randint(1,100)
user_guess = 0
print(answer)
game_status = True
count = 0

def answer_check():
    print(type(user_guess))
    print(type(answer))
    if user_guess == answer:
        print("Correct!")
        sys.exit()
    elif user_guess < answer:
        print("Your answer is lower")
    elif user_guess > answer:
        print("Your answer is higher")
    else:
        print("tf")


def answer_submit():
    try:
        user_guess = int(input("Enter your guess: "))
        if not (1 <= user_guess <= 100):
            raise ValueError()
    except ValueError:
        print ("Invalid Option, the number must be between 1 and 100.")
    answer_check()


while game_status == True:
    answer_submit()
