import numpy
import nltk

fileData = open("positiveDictionary.csv","r")
positiveCharge = fileData.read().split(",")
fileData.close()

fileData = open("negativeDictionary.csv","r")
negativeCharge = fileData.read().split(",")
fileData.close()
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


def scoreAssigner(x, textTokens):
    score = 0
    for word in textTokens:
        for keyword in x:
            if word == keyword:
                print keyword
                score = score + 1
                break

    return score

positiveScore = scoreAssigner(positiveCharge, tokens)
negativeScore = scoreAssigner(negativeCharge, tokens)

print "========================================="
print "                 REPORT                  "
print "========================================="
print '''
      POSITIVE SCORE:  
      ''' + str(positiveScore)
print '''
      NEGATIVE SCORE:  
      ''' + str(negativeScore)
print "========================================="
print "========================================="
print "========================================="
if(positiveScore > negativeScore):
    print "This is a postive sentence"
if(positiveScore < negativeScore):
    print "This is a negative sentence"
if(positiveScore == negativeScore):
    print "This is a neutral sentence"
