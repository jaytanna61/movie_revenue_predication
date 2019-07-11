import json
from collections import Counter
import numpy
from sklearn.linear_model import LogisticRegression
from sklearn import svm
import pylab as pl
import numpy as np
from sklearn import cross_validation
from sklearn.grid_search import GridSearchCV

stopwords = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "just", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the","panther","black",'glover','"black','donald',"deadpool","jedi","(2017)","star",'wars',"wars:",'"donald','"jumanji','jumanji','welcome','"star',]


def my_svm():
    tweets = []
    for line in open('data.txt').readlines()[:500]:
        items = line.split(',')
        tweets.append([int(items[0]), items[1].lower().strip()])

    # Extract the vocabulary of keywords
    vocab = dict()
    for class_label, text in tweets:
        for term in text.split():
            term = term.lower()
            if len(term) > 2 and term not in stopwords:
                if vocab.has_key(term):
                    vocab[term] = vocab[term] + 1
                else:
                    vocab[term] = 1

    # Remove terms whose frequencies are less than a threshold (e.g., 10)
    vocab = {term: freq for term, freq in vocab.items() if freq > 10}
    # Generate an id (starting from 0) for each term in vocab
    vocab = {term: idx for idx, (term, freq) in enumerate(vocab.items())}
    print "******Features*******"
    print vocab

    # Generate X and y
    X = []
    y = []
    for class_label, text in tweets:
        x = [0] * len(vocab)
        terms = [term for term in text.split()]
        for term in terms:
            if vocab.has_key(term):
                x[vocab[term]] += 1
        y.append(class_label)
        X.append(x)


    print "The total number of training tweets: {} ({} positives, {}: negatives)".format(len(y), sum(y), len(y) - sum(y))


    # 10 folder cross validation to estimate the best w and b
    svc = svm.SVC(kernel='linear')
    Cs = range(1, 20)
    clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs), cv = 10)
    clf.fit(X, y)

    print "The estimated w: "
    print clf.best_estimator_.coef_

    print "The estimated b: "
    print clf.best_estimator_.intercept_

    print "The estimated C after the grid search for 10 fold cross validation: "
    print clf.best_params_

    print "Accuracy "
    print str(clf.best_score_)

    # predict the class labels of new tweets
    tweets = []
    for line in open('tJumanji.txt').readlines():
        tweets.append(line)

    # Generate X for testing tweets
    test_X = []
    for text in tweets:
        x = [0] * len(vocab)
        terms = [term for term in text.split() if len(term) > 2]
        for term in terms:
            if vocab.has_key(term):
                x[vocab[term]] += 1
        test_X.append(x)
    test_y = clf.predict(test_X)

    c = 0
    fl = open("p_Jumanji.txt","w")
    fl_n = open("n_Jumanji.txt","w")
    for text in tweets:
        if(test_y[c]==1):
            fl.write(text)
        else:
            fl_n.write(text)
        c+=1


    print "The total number of testing tweets: {} ({} are predicted as positives, {} are predicted as negatives)".format(len(test_y), sum(test_y), len(test_y) - sum(test_y))


my_svm()
