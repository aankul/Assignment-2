
# coding: utf-8

# ### Analysis

# ### 1) Total User Reach (follower count + Listed count)

# In[4]:

import json
import argparse
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import operator

#Parse the argument
parser = argparse.ArgumentParser(description='Process some characters.')
parser.add_argument("search",help="ENTER THE KEYWORD: ")
args = parser.parse_args()

#Get the keyword from the arguments
file_name = args.search
#file_name = 'soccer'


#Open JSON file and load it
with open(file_name + ".json") as tweetfile:
    response = json.loads(tweetfile.read())

#count the total number of follower count and listed count   
count = 0
for tweets in response.get("statuses") :
    count += tweets.get("user").get("followers_count")
    count += tweets.get("user").get("listed_count")

print("The user reach is :- ")
print (count)
print ("\n")
print ("\n")
print ("\n")


# ### 2) Higest occuring terms in the tweets

# In[43]:

text = ""

#Get the english texts
for tweets in response.get("statuses") :
    if(tweets.get("lang") == "en") :
        text = text + tweets.get("text")

#Convert it into tokens
tokens = word_tokenize(text.lower())

#Remove the stopwords
filtered_words = [word for word in tokens if word not in stopwords.words('english')]

wrd_dic = {}
for wrd in filtered_words:
    if len(wrd) > 2 :
        if wrd not in wrd_dic:
            wrd_dic[wrd] = 1
        else:
            wrd_dic[wrd] = wrd_dic[wrd]+1

sorted_x = sorted(wrd_dic.items(), key=operator.itemgetter(1),reverse=True)

print ("Most mentioned term in the tweets:")
for (key, val) in sorted_x :
    if(val > 2) :
        print(key," : ",val)
print ("\n")
print ("\n")
print ("\n")


# ### 3) Top 10 Retweets

# In[51]:

#Get the retweet counts
rt_dict = {}
for tweets in response.get("statuses") :
    t = tweets.get("retweet_count")
    txt = tweets.get("text")
    rt_dict[txt] = t
    
sorted_rt = sorted(rt_dict.items(), key=operator.itemgetter(1),reverse=True)


print ("Top 10 retweets")
i=0
for (key, val) in sorted_rt :
    if(i < 10) :
        print(key," : ",val)
        i = i+1
print ("\n")
print ("\n")
print ("\n")


# ### 4) Tweets grouped by the timezones

# In[37]:

#Get the tweets per timezone
dic = {}
for tweets in response.get("statuses") :
    tz = tweets.get("user").get("time_zone")
    if tz:
        if tz not in dic:
            dic[tz] = 1
        else:
            dic[tz] = dic[tz]+1

sorted_tz = sorted(dic.items(), key=operator.itemgetter(1),reverse=True)

print ("Number of tweets per timezones")
for (key, val) in sorted_tz:
    print(key," : ",val)
print ("\n")
print ("\n")
print ("\n")


# ### 5) Number of potential spam users

# In[63]:

count = 0;
for tweets in response.get("statuses") :
    followers = tweets.get("user").get("followers_count")
    frnds = tweets.get("user").get("friends_count")
    url = tweets.get("url")
    desc = tweets.get("user").get("description")
    if(followers == 0) :
        followers = 1
    if((frnds/followers) > 0.1 and url!="null" and len(desc) > 25):
        count = count + 1
print ("Number of potential spam users: ")
print (count)
