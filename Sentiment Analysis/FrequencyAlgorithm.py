import csv


def dictReader(filename):
    f = open(filename, "r")
    r = csv.DictReader(f, delimiter='\n')
    mydict = {}
    for row in r:
        for k,v in row.iteritems():
            vals =  v.split(",")
            keys = k.split(",")
            i = 0
            while i < len(keys):
                mydict[i] = int(vals[i])
                i= i + 1            
    #print r.value
    #print mydict
    return mydict

pos = dictReader("positiveDynamicData.csv")
neg = dictReader("negativeDynamicData.csv")
posFreq = []
negFreq = []
for x in pos.values():
    posFreq.append(x)
for x in neg.values():
    negFreq.append(x)



print posFreq
print negFreq
