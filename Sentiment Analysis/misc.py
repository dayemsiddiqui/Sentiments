#==========================================================
#                       LIBRARY IMPORTS
#==========================================================
import requests
import json
import time
import urllib
from bs4 import BeautifulSoup

#===========================================================

fileData = open("negativeDictionary.csv", "r")

data = fileData.read()
fileData.close()

words = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
         "R","S","T","U","V","W","X","Y","Z"]
for w in words:
    data = data.replace(w, "")

data = data.replace("\n"," ")
data = data.replace(" ",",")
data = data.replace(",,,",",")
data = data.replace(",,",",")
print data

fileData = open("negativeDictionary.csv", "w")

fileData.write(data)

fileData.close()
