import json as js
import string as str

with open("ParseResult.json") as jsondata:
    data = js.load(jsondata)

temp = 1
search_name = ""
requestName = input(" Find by Name - [1]\n Find by Symbol - [2]\n Input:")

if requestName == "1":
    search_name = str.capwords(input("\nEnter search Name: "))
    for i in data:
        if i['coin']["NAME"] == search_name:
            print("NAME COIN - ", i['coin']["NAME"])
            print("SYMBOL COIN - ", i['coin']['SYMBOL'])
            print("COIN PRICE - ", i['coin']['PRICE'])
            print("MARKET CAP - ", i['coin']['MARKET_CAP'])

if requestName == "2":
    search_name = input("\nEnter search Symbol: ").upper()
    for i in data:
        if i['coin']['SYMBOL'] == search_name:
            print("NAME COIN - ", i['coin']["NAME"])
            print("SYMBOL COIN - ", i['coin']['SYMBOL'])
            print("COIN PRICE - ", i['coin']['PRICE'])
            print("MARKET CAP - ", i['coin']['MARKET_CAP'])
