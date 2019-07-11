# Import the necessary methods from tweepy library
import datetime
import json
import os

import tweepy
from tweepy.streaming import StreamListener

# Variables that contains the user credentials to access Twitter API
access_token = "137269494-WOIhYGJ12wXWec0UEgeyjtDEgwmT0zoP7bBYiDy8"
access_token_secret = "YE3wyKpwAyH4Uyu75LfNT0k8e7YfdotK61Q1ID6wEZiAX"
consumer_key = "w87t3ZGvGsj4aWaZLLCm4Qjlw"
consumer_secret = "flm4z5AnaKKNq0gs5T6tWMNKhOpS5pEAlTT1pOFSEuVli9mYyn"

OAuth = tweepy.OAuthHandler('w87t3ZGvGsj4aWaZLLCm4Qjlw', 'flm4z5AnaKKNq0gs5T6tWMNKhOpS5pEAlTT1pOFSEuVli9mYyn')
OAuth.set_access_token('137269494-WOIhYGJ12wXWec0UEgeyjtDEgwmT0zoP7bBYiDy8',
                       'YE3wyKpwAyH4Uyu75LfNT0k8e7YfdotK61Q1ID6wEZiAX')


class StreamListener(tweepy.StreamListener):
    def on_data(self, raw_data):
        output_folder_date = 'data/{0}'.format(datetime.datetime.now().strftime('%Y_%m_%d'))
        if not os.path.exists(output_folder_date): os.makedirs(output_folder_date)
        output_file = output_folder_date + '/data.txt'
        try:
            jdata = json.loads(str(raw_data))
            print jdata['text']
            f = open(output_file, 'a+')
            f.write(json.dumps(jdata) + '\n')
            f.close()
        except:
            print 'Data Writting exception.'


def main():
    while True:
        sl = StreamListener()
        stream = tweepy.Stream(OAuth, sl)
        try:
            stream.filter(languages=["en"], track=['The Imitation Game', 'Fifty Shades of Grey'])
        except:
            print 'Exception occur!'


if __name__ == '__main__':
    main()
