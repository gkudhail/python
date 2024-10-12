import pandas as pd
import spacy
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyser
from spacy.lang.en.stop_words import STOP_WORDS

nltk.download('vader_lexicon') # lexicon downloaded
nlp = spacy.load("en-core_web_sm") #tokenizrer for tagger parser NER and word vectors for English
dataframe = pd.read_csv('amazon_product_reviews.csv')#file loaded
cleaned_data = dataframe.dropna(subset=['reviews.txt'])

def preprocessed_text(text):#for preprocessing
    doc = nlp(text)
    tokens = [token.text for token in doc if token.text.lower()#stopwords and punctuation removed
    cleaned_text = ' '.join(tokens) # text formed as string
    return cleaned_text.lower()

cleaned_reviews = cleaned_data['reviews.text'].apply(preprocessed.text)

sentiment_analyser = SentimentIntensityAnalyser() 

def sentiment_analyzed(review): #function examining sentiment 

    sentiments_scores = sentiment_analyser.polarity_scores(review) #Vader implemented for analyzing sentiment
    compound_scores = sentiments_scores['compound'] #compound sentiment scores are extracted
    positive_threshold = 0.1
    negative threshold = -0.1

if compound_scores > positive_threshold:
    return "Positive"

elif compound_sores < negative threshold:
    return "Negative"
else:
    return "Neutral"

print("Sentiment Results Analysed:") #sentiments are analyzed 
for review in cleaned_reviews:
    polarity = sentiment_analyzed(review)
    print("Sentiment Polarities:", polarity)

    
    

