#Guess the number
import random
computer_number = random.randint(1,10)
guess_number = 0
attempts = 0

while guess_number!=computer_number:
    guess_number = int(input("Guess a number: "))
    if guess_number < 1 or guess_number>10:
        print("please enter a number between 1 and 10")
        continue
    attempts +=1

    if guess_number<computer_number:
        print("The number is less than the computer number")

    elif guess_number>computer_number:
        print("The number is greater than the computer number")

else:
    print("you won the game")
    print("Number of attempts=",attempts)


#Screambled word


import random
words = ["python", "javascript", "java", "automation", "pytest"]

selected_word = random.choice(words)
letters = random.sample(selected_word, len(selected_word))
scrambled_word = "".join(letters)
print("Scrambled word:", scrambled_word)

attempts = 0

user_guess = ""

while user_guess != selected_word:
    user_guess = input("Guess the original word: ")

    attempts += 1

    if user_guess == selected_word:
        print("Correct! You won the game")
        print("Total attempts:", attempts)

    else:
        print("Wrong! Try again")
