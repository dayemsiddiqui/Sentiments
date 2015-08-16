##from nltk.classify import PositiveNaiveBayesClassifier
##
##sports_sentences = [ 'The team dominated the game',
##                   'They lost the ball',
##                   'The game was intense',
##                   'The goalkeeper catched the ball',
##                   'The other team controlled the ball' ]
##
##various_sentences = [ 'The President did not comment',
##                     'I lost the keys',
##                     'Sara has two kids',
##                     'The show is over' ]
##
##
##def posfeatures(sentence):
##    words = sentence.lower().split()
##    return dict((w, "positive") for w in words)
##
##def negfeatures(sentence):
##    words = sentence.lower().split()
##    return dict((w, "negative") for w in words)
##
##print features("Hello my name is Dayem")
##
##positive_featuresets = list(map(features, sports_sentences))
##    
