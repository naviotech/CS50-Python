'''
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in 
these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a 
time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, 
output how many cents in change the user is owed. Assume that the user will only input integers, and 
ignore any integer that isn’t an accepted denomination.
'''
price = 50
while price > 0:
    print(f"Amount Due: {price}")
    pay = int(input("Insert Coin: "))
    if pay == 25 or pay == 10 or pay == 5:
        price = price - pay
        if price < 0:
            print(f"Change Owed: {abs(price)}")
        elif price == 0 :
            print("Change Owed: 0")
    else:
        continue