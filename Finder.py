import json as js
import string as str

with open("ParseResult.json") as jsondata:
    data = js.load(jsondata)

SYMBOL = 'SYMBOL'
NAME = 'NAME'


def print_coin_data(_search_name, _type):
    print("===========")
    for i in data:
        if i['coin'][_type] == _search_name:
            print("NAME COIN - ", i['coin']["NAME"])
            print("SYMBOL COIN - ", i['coin']['SYMBOL'])
            print("COIN PRICE - ", i['coin']['PRICE'])
            print("MARKET CAP - ", i['coin']['MARKET_CAP'])


def print_all_element():
    for i in data:
        print("===========")
        print("NAME COIN - ", i['coin']["NAME"])
        print("SYMBOL COIN - ", i['coin']['SYMBOL'])
        print("COIN PRICE - ", i['coin']['PRICE'])
        print("MARKET CAP - ", i['coin']['MARKET_CAP'])


def print_developers():
    print("https://vk.com/huharev1")
    print("https://vk.com/lvzvrv")
    print("https://vk.com/pmakhonin")


requestName = input("Find by Name - [1]\nFind by Symbol - [2]\nAll elements - [3]\nDevelopers - [4]\nInput: ")
while requestName != "":
    if requestName == "1":
        _type = NAME
        search_name = str.capwords(input("Enter search Name: "))
        print_coin_data(search_name, _type)
    if requestName == "2":
        _type = SYMBOL
        search_name = input("\nEnter search Symbol: ").upper()
        print_coin_data(search_name, _type)
    if requestName == "3":
        print_all_element()
    if requestName == "4":
        print_developers()
    print("===========")
    requestName = input("Find by Name - [1]\nFind by Symbol - [2]\nAll elements - [3]\nDevelopers - [4]\nInput: ")
