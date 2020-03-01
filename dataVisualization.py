# visualize the opspam data
from google.colab import drive
drive.mount('/content/drive')

!ls .views_len).describe()

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

with open('drive/My Drive/opspam/opspam_review.txt', 'r') as txtf:
    texts = txtf.readlines()
    reviews_len = [len(x) for x in texts ]


pd.Series(reviews_len).hist()
plt.show()
pd.Series(reviews_len).describe()

# distinguish positive and negative words
import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = nltk.sentiment.vader.SentimentIntensityAnalyzer()
positive_len = []
negative_len = []
neutral_len = []
text_len = []

with open('drive/My Drive/opspam/opspam_review.txt', 'r') as f:
  texts = f.readlines()
  for text in texts:
    pos = 0
    neg = 0
    neu = 0
    text_len.append(len(text))
    for word in text.split(' '):
      if (sid.polarity_scores(word)['compound']) >= 0.5:
        pos += 1
      elif (sid.polarity_scores(word)['compound']) <= -0.5:
        neg += 1
      else:
        neu += 1
    positive_len.append(pos)
    negative_len.append(neg)
    neutral_len.append(neu)

print("positive_len:" , positive_len)
print("negative_len:", negative_len)
print("neutral_len:", neutral_len)
print("text_len:", text_len)