
from pattern.text.en import positive
import sys
import glob
import os


def sentiment_analysis(file):
    fl = open(file,"r")
    i=0.0
    j=0.0
    for line in fl.readlines():
        if positive(line, 0.1):
            i+=1
        else:
            j+=1
    fl.close()
    positive_score = i/(i+j)
    negative_score = j/(i+j)
    # print "positive Score: ",positive_score
    return positive_score


def cal_s_score():
    path = os.path.dirname(sys.modules['__main__'].__file__)+'/Movies_tweets/*.txt'
    files = glob.glob(path)
    for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
        print name
        print sentiment_analysis(name)
        import pandas as pd
        df = pd.read_excel('2014 and 2015 CSM dataset 2.xlsx')  # Read Excel file as a DataFrame
        df['Sentiment Score'] = sentiment_analysis(name)
        df.to_excel('2014 and 2015 CSM dataset 2.xlsx')  # Write DateFrame back as Excel file


#cal_s_score()