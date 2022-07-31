import tweepy
import config

client = tweepy.Client(
        consumer_key=config.API_KEY,
        consumer_secret=config.API_SECRET,
        access_token=config.ACCESS_TOKEN,
        access_token_secret=config.ACCESS_TOKEN_SECRET
        )


# reading text from file
with open('tasks.txt','r') as f:
    tasks = f.readlines()

with open('count.txt') as c:
    count = c.read()

count = count.split()
day = count[0]
# creating tweet
tweet = f"Day {day} of #100DaysOfCode\n"
for task in tasks:
    tweet += f"✅ {task}"


# tweeting
client.create_tweet(text=tweet)
#print(tweet)


