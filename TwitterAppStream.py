import tweepy

class IDPrinter(tweepy.StreamingClient):

    def on_tweet(self, tweet):
        print("****************************************")
        print(tweet.text)


printer = IDPrinter("AAAAAAAAAAAAAAAAAAAAANb7ewEAAAAAyaKZT9Kj15kBEXMpZTAuB3QCZOc%3DUDvPu7ByZzhD901AvV1ysGuMfvDASJ6aKsF0gSQSzMH4GQoA5q")
#printer.delete_rules('1549945787584581639')
print(printer.get_rules())
printer.add_rules(tweepy.StreamRule("Pudim"))
printer.add_rules(tweepy.StreamRule("-is:retweet"))
printer.filter()