# ElectionPrediction using sentiment analysis on social data

## Dataset Information

The Dataset consists of post/tweets for different social-media sites for their parties in the respective tables.

## Requirements
The general libraries used are:
* `tweepy`
* `praw`
* `demoji`
* `vaderSentiment`
* `nltk`
* `deep_translator`

## Collecting Data
Use the `twi_scrap.py` and `red_scrap.py` to fetch data from the respective social-media sites.

## Usage
Run `wordcount.py` to visualize the term frequency scores and sentiments scores.

## Other
You need to enter your api keys for twitter-tweepy and reddit-praw in `wallet.py` before scraping. 
