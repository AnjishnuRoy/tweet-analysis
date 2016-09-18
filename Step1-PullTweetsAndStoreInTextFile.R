library(httr)
library(devtools)
library(twitteR)
library(base64enc)
library(plyr)


#TWITTER API Authentication and SETUP.
# These are my PRIVATE keys, please do not make them public.
consumer_key <- 'Use_your_own' #This is confidential.
consumer_secret <- 'Use_your_own' #This is confidential.
access_token <- 'Use_your_own' #This is confidential.
access_secret <- 'Use_your_own' #This is confidential.
setup_twitter_oauth(consumer_key , consumer_secret, access_token, access_secret)

#Tweeter Scrapping Begins. No. of tweets pulled = 20 with tag = #SamsungGalaxyS7
tw <- searchTwitter("#SamsungGalaxyS7",n=20,lang="en")

#Print data collected
tw 

#Converting data collected into a formatted text file.
tw.df = ldply(tw, function(t) t$toDataFrame())

write.table(tw.df,"Tweets.txt",sep="\t",row.names=FALSE)

