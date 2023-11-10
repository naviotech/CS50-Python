'''
Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, 
until the user inputs control-d (which is a common way of ending one’s input to a program). 
Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing 
each line with the number of times the user inputted that item. No need to pluralize the items. 
Treat the user’s input case-insensitively.
'''
import sys

# Crear un diccionario para almacenar la cantidad de veces que se ingresó cada artículo
shopping_list = {}

# Solicitar elementos al usuario
try:
    while True:
        item = input().upper()  # Convertir el artículo a minúsculas para evitar distinción entre mayúsculas y minúsculas
        if item in shopping_list:
            shopping_list[item] += 1
        else:
            shopping_list[item] = 1
except EOFError:
    pass  # El usuario ha ingresado control-d para finalizar la entrada

# Generar la lista de compras en mayúsculas, ordenada alfabéticamente por artículo
for item in sorted(shopping_list):
    count = shopping_list[item]
    print(f"{count} {item}")