Coursera Project - Sentimental Analysis using Fake twitter data

We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv 
which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. 
We have also words that express positive sentiment and negative sentiment,in the files positive_words.txt and negative_words.txt.

Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is.
You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score
(which is how many happy words are in the tweet),Negative Score (which is how many angry words are in the tweet),
and the Net Score for each tweet. 
At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.

Inputs:

positive_words.txt will have all the positive words.
negative_words.txt will have all the negative words.
project_twitter_data.csv will have the tweet_text,retweet_count,reply_count as column name which will be used for the sentimental analysis.

sentimentClassifier.py - will have the python code used to analyse the project_twitter_data.csv data and produce resulting_data.csv
scatterPlot.py - will have the python code used to produce a graph of the Net Score vs Number of Retweets scatter plot using Matplotlib

Output:

resulting_data.csv will be the output file after our analysis with Number of Retweets,Number of Replies,Positive Score,Negative Score,Net Score as header.
SentimentalAnalysis.png is the plot of Net Score vs Number of Retweets from the resulting_data.csv
