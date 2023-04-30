from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json


browser = webdriver.Chrome()
browser.get("https://coinmarketcap.com/")


for i in range(8):
    browser.execute_script("window.scrollBy(0, 1000);")
    time.sleep(1)


block = browser.find_element(By.TAG_NAME, 'tbody')
table_data_list = block.text.split("\n")


result_dict = []
useless_indeces = [4, 6, 7, 8]
banned_indeces = []


for ind in useless_indeces:
    banned_indeces += [i for i in range(ind, len(table_data_list), 9)]


no_format_result_list = [data for data in table_data_list if table_data_list.index(
    data) not in banned_indeces]
for i in range(0, len(no_format_result_list), 5):
    result_dict.append({})


for j, i in zip(range(100), range(0, len(no_format_result_list), 5)):
    result_dict[j]['id'] = no_format_result_list[i]
    result_dict[j]['coin'] = {}
    result_dict[j]['coin']['NAME'] = no_format_result_list[i+1]
    result_dict[j]['coin']['SYMBOL'] = no_format_result_list[i+2]
    result_dict[j]['coin']['PRICE'] = no_format_result_list[i+3]
    result_dict[j]['coin']['MARKET_CAP'] = no_format_result_list[i+4]


with open(".\ParseResult.json", "w", encoding="utf-8") as file:
    json.dump(result_dict, file, indent=4, ensure_ascii=False)
