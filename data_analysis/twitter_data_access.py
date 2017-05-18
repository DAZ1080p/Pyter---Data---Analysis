
from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener

consumer_Key = 'XXXXXXXXXXXXXXXXXXXXXXX'
consumer_Secret = 'XXXXXXXXXXXXXXXXXXXXXXX'
access_Token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_Token_Secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

auth = OAuthHandler(consumer_Key,
                        consumer_Secret)

auth.set_access_token(access_Token, access_Token_Secret)

#class to print directly to console
class PrintListener(StreamListener):
    def on_status(self, status):
        #Original Tweets no retweets
        if not status.text[:3] == 'RT ':
            print(status.text)
            print(status.author.screen_name,
                status.created_at,
                status.source,
                '\n')

    def on_error(self, status_code):
        print("Error code: {}".format(status_code))
        return True
        # keep stream alive

    def on_timeout(self):
        print('Listener time out!')
        return True
        # keep steam alive

def print_to_terminal():
    listener = PrintListener()
    stream = Stream(auth, listener)
    languages = ('en',)
    stream.sample(languages=languages)
    #non language specific
    #stream.sample()


def pull_down_tweets(screen_name):
     api = API(auth)
     tweets = api.user_timeline(screen_name=screen_name, count=100)
     for  tweet in tweets:
         print(json.dumps(tweet._json, indent=4))
if __name__ == '__main__':
    #print_to_terminal()
    pull_down_tweets(auth.username)
