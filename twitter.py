from __future__ import absolute_import, print_function
import json

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="HfX9vtQ37LoGgcAnOigeqcqRs"
consumer_secret="VHT2CXZrIRvJQCVVKY8VaXFFr20NmQgWfAVeVeKij7Du4pfrIs"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="703801335980773377-7tiks85kqBaeqd7jc0yxZzfBBEEGM2P"
access_token_secret="uwsceG85ug1jCeKeCi1Vab7q5zon1fRaB778qO8z5E5pk"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(json.loads(data)['text'])
        
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=["trump"])
