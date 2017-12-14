import os
from tkinter import *
import tkinter.messagebox
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sys

top = Tk()

CONSUMER_KEY = 'tpTxQCdyQzBJempdCeLpTuGz2'
CONSUMER_SECRET = 'ttM1cCD4eudWzJOfp0DIh5zwcJbl1q0yLFXkK3XHdFuW4zNtX4'
ACCESS_KEY = '923299178733821952-CllipI2BO649Y9YqWpMf9aP6Ix9LVPt'
ACCESS_SECRET = 'sMXd9brjzB8RZbPxrLw5R3JKK9sBHt1cAJ4l7PYV6nMaw'

frame = Frame(width=350, height=60)
frame.pack()

def tweetdata():
    print ("User Id: ", E1.get())
    class TweetListener(StreamListener):
    # A listener handles tweets are the received from the stream.
    #This is a basic listener that just prints received tweets to standard output

        def on_data(self, data):
            print (""+data)
            return True

        def on_error(self, status):
           print (""+status)

    auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    api = tweepy.API(auth)

    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    twitterStream = Stream(auth,TweetListener())
    user_id=E1.get()
    #user_id=923299178733821952
    user = api.get_user(user_id)
    #geo = api.geo_id(user_id)
    #user = api.get_user(430402090)
    friends_count= 0

    for friend in user.friends():
        #print (friend.screen_name)
        friends_count= friends_count+ 1
    print('Task 1: User Information')
    print ('*************************')
    print ('Screen Name: '+user.screen_name)
    print ('Description: '+user.description)
    print ('Followers: ',user.followers_count)
    print ('Friends: ',friends_count)
    print ('Statuses: ', user.statuses_count)
    print ('Url :',user.url)
    print ('User location: ',user.location)

    print('\nTask 2: User friend and follower list ')
    print ('*************************************')
    print( "Friends List:")
    for friend in user.friends():
        print (friend.screen_name)

    print( "\nFollowers List:")
    for follower in api.followers_ids(user_id)[:20]:
        print (api.get_user(follower).screen_name)

    print('\nTask 3: Twitter tweets ')
    print ('***********************')
    class StdOutListener(StreamListener):
        def __init__(self, api=None):
            super(StdOutListener, self).__init__()
            self.tweets = 0

        def on_data(self, data):
            self.tweets += 1
            if self.tweets < 5: 
                all_data = json.loads(data)
                tweet = all_data["text"]
                username = all_data["user"]["screen_name"]                    
                print (username, 'POSTED', tweet)
                return True
            else:
                return False

        def on_error(self, status):
            print (status)

    l = StdOutListener()
    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api=tweepy.API(auth)

    stream = Stream(auth, l)
    stream.filter(locations = [-86.33,41.63,-86.20,41.74] )
    print('***End***')
    os.system('python keywordTweets.py -q indiana,weather -d data')

bottomframe = Frame(top)
bottomframe.pack( side = TOP )
L1 = Label(top, text="Enter Twitter id: ")

L1.pack( side = TOP)
E1 = Entry(top, bd =5)
E1.pack(side = TOP)

B1 = tkinter.Button(bottomframe, text = "Search", command = tweetdata)
bottomframe.pack( side = BOTTOM )
B1.pack()

top.mainloop()
