'''
Bitcoin is a form of digitial currency, otherwise known as cryptocurrency. Rather than rely on a 
central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a 
blockchain, to record transactions.

Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as 
by exchanging one currency (e.g., USD) for Bitcoin.

In a file called bitcoin.py, implement a program that:

Expects the user to specify as a command-line argument the number of Bitcoins, 
, that they would like to buy. If that argument cannot be converted to a float, the program should exit 
via sys.exit with an error message.
Queries the API for the CoinDesk Bitcoin Price Index at 
https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, 
among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, 
as with code like:
'''
import requests
import sys


try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    date = response.json()
    amount = date['bpi']['USD']['rate_float']
except requests.RequestException:
    sys.exit()

try:
    n = float(sys.argv[1])
    
except ValueError:
    sys.exit("Missing command-line argument")
except IndexError:
    sys.exit("Command-line argument is not a number")

print(f"${n * amount:,.4f}")
