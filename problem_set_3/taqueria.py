'''
In a file called taqueria.py, implement a program that enables a user to place an order, 
prompting them for items, one per line, until the user inputs control-d (which is a common way 
of ending one’s input to a program). After each inputted item, display the total cost of all items 
inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. 
Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume 
that every item on the menu will be titlecased.
'''
my_dict = {
    "Baja Taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}
price = 0
while True:
    try:
        item = input("Item: ")
        for i in my_dict:
            if item == i:
                value = my_dict[i]
                price += value
                print(f"Total: ${price:.2f}")

    except EOFError:
        break
    else:
        continue