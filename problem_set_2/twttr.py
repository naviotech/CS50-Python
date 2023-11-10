'''
When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting 
vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program 
that prompts the user for a str of text and then outputs that same text but with all vowels 
(A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
'''
def main():
    print("Output:", shorten(input("Input: ")))

def shorten(word):
    my_list = ["A","a","E","e","i","I","O","o","U","u"]
    my_other_list = []
    for letter in word:
        if letter not in my_list:
            my_other_list.append(letter)

    conc= "".join(my_other_list)
    return conc

if __name__ == "__main__":
    main()
