import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

# converts sentiment_score into positive and negitive
def get_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)['compound']
    
    if sentiment_score >= 0.05:
        return 'positive', sentiment_score
    elif sentiment_score <= -0.05:
        return 'negative', sentiment_score
    else:
        return 'neutral', sentiment_score

responses = [
    # list of responses

    
]

# sorts reposnes into dictionary sorted my postitive negitive and neutral
sorted_responses = {'positive': [], 'negative': [], 'neutral': []}
sentiment_scores = []

for response in responses:
    sentiment, sentiment_score = get_sentiment(response)
    sorted_responses[sentiment].append({'response': response, 'sentiment_score': sentiment_score})
    sentiment_scores.append(sentiment_score)

# prints Response along with sentiment_score
print("Positive Responses:")
for response_data in sorted_responses['positive']:
    print("-", response_data['response'], "Sentiment Score:", response_data['sentiment_score'])

print("\nNegative Responses:")
for response_data in sorted_responses['negative']:
    print("-", response_data['response'], "Sentiment Score:", response_data['sentiment_score'])

print("\nNeutral Responses:")
for response_data in sorted_responses['neutral']:
    print("-", response_data['response'], "Sentiment Score:", response_data['sentiment_score'])
    
avg_sentiment_score = sum(sentiment_scores) / len(sentiment_scores)
print("\nAverage Sentiment Score:", avg_sentiment_score)