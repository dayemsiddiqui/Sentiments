#==========================================================
#                       LIBRARY IMPORTS
#==========================================================
import requests
import json
import time
import urllib
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import csv
#===========================================================
#                       Methods
#===========================================================

def filterIt(text):

    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)

    filteredSentence = []

    for w in words:
        if w not in stop_words:
            filteredSentence.append(w)


    tagged = nltk.pos_tag(filteredSentence)
    #print "Tagged: "
    #print tagged

    shit = []


    for word in tagged:
##        if word[1] == "JJR":
##            shit.append(word[0].upper())
##        if word[1] == "JJS":
##            shit.append(word[0].upper())
##        if word[1] == "RB":
##            shit.append(word[0].upper())
##        if word[1] == "RBR":
##            shit.append(word[0].upper())
##        if word[1] == "RBS":
##            shit.append(word[0].upper())
##        if word[1] == "UH":
##            shit.append(word[0].upper())
##        else:
        shit.append(word[0].upper())
    return shit


#***************************************************

def dictReader(filename):
    f = open(filename, "r")
    r = csv.DictReader(f, delimiter='\n')
    mydict = {}
    for row in r:
        for k,v in row.iteritems():
            #print k, v
            mydict[k] = v
            
    #print r.value
    #print mydict
    return mydict

    

#***************************************************
def sortIt(diction, element):
    count = []
    for x in diction.keys():
        count.append(diction[x][0])
    count.sort()
    return count.index(element)
#****************************************************

def putIn(final,dictionary):
    for word in final:
        if word in dictionary.keys():
          dictionary[word] = int(dictionary[word])+1 
        else:
          dictionary[word] =  1
#*****************************************************
def eliminate(a,b):
    for x in a.keys():
        for y in b.keys():
            if x == y:
                del a[x]
                del b[y]
    return (a,b)

#=============================================================================
#                   Variable Declaration
#=============================================================================
positiveDictionary = dictReader("positiveDynamicData.csv")

negativeDictionary = dictReader("negativeDynamicData.csv")

random = raw_input("Type the file name you want to read: ")

print "Opening Reviews"
f = open(random)
print "Reading Reviews"
random = f.read()
random = random.decode('utf-8')
print "Tokenizing Reviews"
some = sent_tokenize(random)

annotedSentencePositive = []
annotedSentenceNegative = []

for x in some:
    print x
    y = raw_input("1 for + / 2 for - :")
    if y == "1":
        annotedSentencePositive.append(x)
        finalWords = filterIt(x)
        putIn(finalWords, positiveDictionary)
        print ""
        print "====================="
    if y == "2":
        annotedSentenceNegative.append(x)
        finalWords = filterIt(x)
        putIn(finalWords, negativeDictionary)
        print ""
        print "====================="
    if y == "3":
        break;





eliminate(positiveDictionary, negativeDictionary)

#print positiveDictionary
#print negativeDictionary

for x in annotedSentencePositive:
    
    f = open("positiveSentence.csv", 'a')
    f.write("\n")
    f.write(x)
    f.close()

for x in annotedSentenceNegative:
    
    f = open("negativeSentence.csv", 'a')
    f.write("\n")
    f.write(x)
    f.close()


with open('negativeDynamic.csv', 'a') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, negativeDictionary.keys())
    w.writeheader()
with open('negativeDynamicData.csv', 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, negativeDictionary.keys())
    w.writeheader()
    w.writerow(negativeDictionary)
with open('positiveDynamicData.csv', 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, positiveDictionary.keys())
    w.writeheader()
    w.writerow(positiveDictionary)
with open('positiveDynamic.csv', 'a') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, positiveDictionary.keys())
    w.writeheader()
