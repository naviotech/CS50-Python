'''
I’m thinking of a number between 1 and 100…

What is it?
It’s 50! But what if it were more random?

In a file called game.py, implement a program that:

Prompts the user for a level, 
. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and 
, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should 
prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the 
user again.
If the guess is larger than that integer, the program should output Too large! and prompt the 
user again.
If the guess is the same as that integer, the program should output Just right! and exit.
'''
import random

while True:
    number= input("Level: ")
    if number.isdigit() and int(number) > 0:
        number = int(number)
        number_random = random.randint(1,number)
        correct_guess = False
        while not correct_guess:
            answer= input("Guess: ")
            if answer.isdigit() and int(answer)> 0:
                answer = int(answer)
                if answer == number_random:
                    print("Just right!")
                    correct_guess= True
                elif answer != number_random and answer < number_random:
                    print("Too small!")
                    continue
                elif answer != number_random and answer > number_random:
                    print("Too Large!")
                    continue
                else:
                    continue
            else:
                continue
        break
    else:
        continue