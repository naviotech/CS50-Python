'''
In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, 
the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or 
forty two. Otherwise output No.
'''
answer = input("What is de answer to great question of life, the universe, and everything? ").title()

if answer.strip() == "42" or answer.strip() == "Forty Two" or answer.replace("-"," ") == "Forty Two":
    print("Yes")
else:
    print("No")
