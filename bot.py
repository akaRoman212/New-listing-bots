import asyncio
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events

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
api_id = '12788011'
api_hash = 'f06ac3603456859eccfd831b62d8134a'
api_key = '6224bde70fd8a700019e8bc5'
api_secret = '327de38a-60ad-4606-898d-50f03d50c680'
api_passphrase = '85462500'

client = Client(api_key, api_secret, api_passphrase)
phone = '+917351699598'
  
# creating a telegram session and assigning
# it to a variable client
tclient = TelegramClient('bin-session', api_id, api_hash)
  
# connecting and building the session
tclient.connect()
if not tclient.is_user_authorized():

    tclient.send_code_request(phone)
    
    # signing in the client
    tclient.sign_in(phone, input('Enter the code: '))

tokens = psym.sym
# pprint.pprint(currencies)

# pprint.pprint(currencies[0]['currency'])

# # #Get all symbols and then compare in excel
# for x in currencies:
#     print(x['currency'])

# # #For new token search by user choice
# input = input("Which symbol you want to search???")

up_token = []
# # #Get all symbols and then compare in excel
while True:
    symbol = client.get_currencies()
    
    up_token.clear()
    for x in symbol:
        up_token.append(x['currency'])

    # print (len(up_token))
    # print (len(tokens))
    
    if (len(tokens) != len(up_token)):
        winsound.Beep(freq, duration)
        print("New pair found!!!")
        for y in range(len(up_token)):
            if up_token[y] not in tokens:
                print(up_token[y])
                webbrowser.open("https://www.kucoin.com/news/categories/listing")
                try:
                    

                    # sending message using telegram client
                    tclient.send_message('kinggamer212', up_token[y])
                except Exception as e:
                    
                    # there may be many error coming in while like peer
                    # error, wrong access_hash, flood_error, etc
                    print(e)

    
    print("Kucoin Searching..............")
    time.sleep(60)
