'''
In The Sound of Music, there’s a song sung largely in English, So Long, Farewell, with these lyrics, 
wherein “adieu” means “goodbye” in French:

Adieu, adieu, to yieu and yieu and yieu

Of course, the line isn’t grammatically correct, since it would typically be written (with an Oxford 
comma) as:

Adieu, adieu, to yieu, yieu, and yieu

To be fair, “yieu” isn’t even a word; it just rhymes with “you”!

In a file called adieu.py, implement a program that prompts the user for names, one per line, until 
the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those 
names, separating two names with one and, three names with two commas and one and, and 
 names with 
 commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
'''
list=[]
try:
    while True:

        nouns = input()
        list.append(nouns)
except EOFError:
    if len(list) == 1:
        print(f"Adieu, adieu, to {list[0]}")
    elif len(list) == 2:
        print(f"Adieu, adieu, to {list[0]} and {list[1]}")
    else:
        more_nouns = ", ".join(list[1:-1])
        print(f"Adieu, adieu, to {list[0]}, {more_nouns}, and {list[-1]}")
