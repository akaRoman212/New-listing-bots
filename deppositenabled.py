import asyncio
from locale import currency
import sys

from kucoin.client import Client
import pprint 
import psym
import webbrowser
import winsound
import time      
duration = 1000  # milliseconds
freq = 440  # Hz
# api_key = '6224b58e37a6090001981aa2'
# api_secret = '1b104eeb-4d9e-40c5-9dc7-51967902b0e5'
# api_passphrase = '00000000'
# client = Client(api_key, api_secret, api_passphrase, sandbox=True)

api_key = '6224bde70fd8a700019e8bc5'
api_secret = '327de38a-60ad-4606-898d-50f03d50c680'
api_passphrase = '85462500'

client = Client(api_key, api_secret, api_passphrase)


tokens = psym.sym
# pprint.pprint(currencies)

# pprint.pprint(currencies[0]['currency'])

# # #Get all symbols and then compare in excel
# for x in currencies:
#     print(x['currency'])

# # #For new token search by user choice
# input = input("Which symbol you want to search???")
input = input("Which symbol you want to search???")
symbol = client.get_currencies()
    
found = False  

for x in symbol:
    if x['currency'] == input:
        pprint.pprint(x)
        found = True
        break
print('Token found ????   ::  ' + str(found))
# # #Get all symbols and then compare in excel
while True:
    symbol = client.get_currencies()
    
    

    for x in symbol:
        if x['currency'] == input:
             
            if x['isDepositEnabled'] == True :
                print("Deposit is now enabled")

                
                webbrowser.open("https://www.https://www.kucoin.com/news/categories/listing")
                sys.exit()
    
    print("Deposit is CLOSED CLOSED CLOSED for now!!")
    time.sleep(60)
