import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
 
def word_feats(words):
    return dict([(word, True) for word in words])
 
negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')

print 'Getting Ready...'
 
negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'negative') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'positive') for f in posids]

#print posfeats[5]

negcutoff = len(negfeats)*3/4
poscutoff = len(posfeats)*3/4
 
trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
#classifier.show_most_informative_features()

print 'Almost Ready Please Wait...' 
 
classifier = NaiveBayesClassifier.train(trainfeats)

while True:
    text = raw_input("Type the text you want to check: ")
    print classifier.classify(word_feats(text))


