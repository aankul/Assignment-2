import argparse
import oauth2 as oauth
import json
import os
import codecs


#Parse the argument
parser = argparse.ArgumentParser(description='Process some characters.')
parser.add_argument("search",help="ENTER THE KEYWORD: ")
args = parser.parse_args()

#Get the keyword from the arguments
keyword = args.search
#keyword = 'cricket'
 
#Authentication Keys
CONSUMER_KEY = "kkDcIct3CMaPW8yYB88YLaVyL"
CONSUMER_SECRET = "6dWlU8yBR6t38lBneeW5FcxR1FCoJeIPipqNSCTHjfIxW8VtlK"
ACCESS_KEY = "456545130-uY5aKKUC9o2aoY9RxUGMtXdwQJnIjcNrXuFL6bR4"
ACCESS_SECRET = "PzVH3FBkMa9t9WWhhvHOzt9wPszdxcQbOObTr827CV3CO"


# OAuth Authentication
consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)


# Calling API with the keyword
timeline_endpoint = "https://api.twitter.com/1.1/search/tweets.json?q="+keyword+"&count=300"
resp , data = client.request(timeline_endpoint)


# Decoding to JSON format
tweets = json.loads(data.decode())

#Storing the tweets
file_name = keyword +".json"

with open(file_name,'w') as f:
    json.dump(tweets,f,indent=4)

