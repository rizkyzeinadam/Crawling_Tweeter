import tweepy
import csv

api_key = "" ##Didapatkan Dari Twitter Dev
api_key_secret = "" ##Didapatkan Dari Twitter Dev
access_token = "" ##Didapatkan Dari Twitter Dev
access_token_secret= "" ##Didapatkan Dari Twitter Dev

tweetperquery = 100
maxTweets = 100
search_key = "rizkyzeinadam" ## Masukan target user contoh : @rizkyzeinadam yang diambil Nick nya saja jadi rizkyzeinadam
maxId= -1
tweetCount = 0

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = True , wait_on_rate_limit_notify=True)


while tweetCount < maxTweets:
    if  maxId <= 0:
        newTweets = api.search(q = search_key, count = tweetperquery,result_type="recent",tweet_mode = "extended")
        
    newTweets= api.search(q = search_key, count=tweetperquery,result_type="recent",tweet_mode = "extended", maxId=str(maxId-1))
    
    if not newTweets:
        print("Tweet Habis")
        break
        
    for tweet in newTweets:
        dictTweet = {
            "username" : tweet.user.name,
            "tweet" : tweet.full_text.encode('utf-8')
        }
        print("Username {username} : {tweet}".format(username=dictTweet["username"],tweet =dictTweet["tweet"]))
        with open(search_key+".csv",'a+',newline = '')  as csv_file:
            fieldNames = ["username","tweet"]
            writer = csv.DictWriter(csv_file, fieldnames = fieldNames, delimiter=",")
            writer.writerow(dictTweet)
            
    tweetCount += len(newTweets)
    maxId = newTweets[-1].id    
