#==============================================================
#                       LIBRARY IMPORT
#==============================================================
import numpy as np
import nltk
#==============================================================


#==============================================================
#                       FUNCTION DEFINITIONS
#==============================================================


def readDictionary(x,y):
    fileData = open(x,"r")
    positive = fileData.read().split(",")
    fileData.close()
    positive = np.array(positive)
    fileData = open(y,"r")
    negative = fileData.read().split(",")
    negative = np.array(negative)
    fileData.close()
    return (positive, negative)


def scoreAssigner(x, textTokens):
    score = 0
    for word in textTokens:
        for keyword in x:
            if word == keyword:
                #print keyword
                score = score + 1
                break

    return score

#==============================================================




positiveCharge = np.array([])
positiveCharge, negativeCharge = readDictionary("positiveDictionary.csv","negativeDictionary.csv")
p, n = readDictionary("positiveDynamic.csv","negativeDynamic.csv")

temp = []

text = raw_input("Write Your Text To Be Analysed: ")

for word in negativeCharge:
    temp.append(word.upper())

negativeCharge = temp
##print positiveCharge

tokens =  nltk.word_tokenize(text.upper())
print tokens
positiveScore = 0;
negativeScore = 0;



positiveScore = scoreAssigner(positiveCharge, tokens) + scoreAssigner(p, tokens)/2
negativeScore = scoreAssigner(negativeCharge, tokens) + scoreAssigner(n, tokens)/2

##print "========================================="
##print "                 REPORT                  "
##print "========================================="
##print '''
##      POSITIVE SCORE:  
##      ''' + str(positiveScore)
##print '''
##      NEGATIVE SCORE:  
##      ''' + str(negativeScore)
##print "========================================="
##print "========================================="
##print "========================================="
if(positiveScore > negativeScore):
    print "This is a postive sentence"
if(positiveScore < negativeScore):
    print "This is a negative sentence"
if(positiveScore == negativeScore):
    print "This is a neutral sentence"
