import sys
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Ensure required resource is present
nltk.download('vader_lexicon', quiet=True)
sia = SentimentIntensityAnalyzer()

# Emotion Lexicon
emotion_lexicon = {
    'Joy': {'love', 'great', 'awesome', 'amazing', 'excellent', 'happy', 'best', 'enjoy', 'wonderful', 
            'perfect', 'favorite', 'fun', 'glad', 'super', 'pleased', 'good', 'nice', 'cool', 'fantastic', 
            'brilliant', 'delight', 'loved', 'loving', 'likes'},
    'Anger': {'hate', 'angry', 'terrible', 'worst', 'horrible', 'garbage', 'mad', 'useless', 'trash', 
              'junk', 'suck', 'sucks', 'scam', 'annoying', 'annoyed', 'frustrating', 'frustrated', 
              'stupid', 'ridiculous', 'pissed', 'crap'},
    'Sadness': {'disappointed', 'disappointing', 'disappointment', 'sad', 'regret', 'unfortunate', 
                'unfortunately', 'poor', 'broke', 'broken', 'failed', 'fails', 'failure', 'cried', 
                'loss', 'boring', 'miss', 'pathetic'},
    'Fear': {'worried', 'worry', 'afraid', 'scared', 'concern', 'concerned', 'problem', 'problems', 
             'panic', 'nervous', 'risk', 'danger', 'creepy', 'doubt', 'issue', 'issues', 'warning', 
             'security', 'privacy', 'unsecure'},
    'Surprise': {'surprised', 'surprising', 'surprise', 'wow', 'unexpected', 'unexpectedly', 'shock', 
                 'shocked', 'amaze', 'amazed', 'astonished', 'astonishing', 'incredible', 'sudden', 'suddenly'}
}

def detect_emotion(text):
    words = re.findall(r'\b[a-z]+\b', str(text).lower())
    counts = {e: 0 for e in emotion_lexicon}
    for w in words:
        for emo, term_set in emotion_lexicon.items():
            if w in term_set:
                counts[emo] += 1
    max_count = max(counts.values())
    if max_count == 0:
        return 'Neutral/Other'
    top_emotions = [emo for emo, cnt in counts.items() if cnt == max_count]
    return top_emotions[0]

def analyze(text):
    scores = sia.polarity_scores(str(text))
    compound = scores['compound']
    if compound >= 0.05:
        sentiment = 'POSITIVE'
        symbol = '[+]'
    elif compound <= -0.05:
        sentiment = 'NEGATIVE'
        symbol = '[-]'
    else:
        sentiment = 'NEUTRAL'
        symbol = '[~]'
        
    emotion = detect_emotion(text)
    
    print('=' * 68)
    print(f'REVIEW: "{text}"')
    print('-' * 68)
    print(f'SENTIMENT:        {symbol} {sentiment}')
    print(f'COMPOUND SCORE:   {compound:+.3f}  (Scale: -1.000 to +1.000)')
    print(f'DOMINANT EMOTION: {emotion}')
    print(f'VALENCE SCORES:   Positive: {scores["pos"]:.2f} | Neutral: {scores["neu"]:.2f} | Negative: {scores["neg"]:.2f}')
    print('=' * 68)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        review_input = ' '.join(sys.argv[1:])
        analyze(review_input)
    else:
        print('\nCUSTOMER SENTIMENT ANALYTICS - TEST SUITE\nCreated by Harshita Tomer')
        print('Testing 4 sample customer reviews:\n')
        analyze('The sound quality on this Echo Dot is awesome, absolutely love listening to music on it!')
        analyze('It stopped working after 3 days and keeps dropping WiFi connection. Very disappointed.')
        analyze('I received the package on Monday afternoon.')
        analyze('Worst device I ever bought. Horrible customer service and total garbage!')
        print('\nTip: You can test your own text anytime by running:')
        print('  python test_sentiment.py "Your review text here"\n')
