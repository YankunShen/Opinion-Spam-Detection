import pandas as pd
import csv


# with open('/Users/shenyankun/Downloads/op_spam_v1.4/positive_polarity/training_positive.csv', 'r') as f1:
#     truth = f1.read()
#
# with open('/Users/shenyankun/Downloads/op_spam_v1.4/negative_polarity/training_negative.csv', 'r') as f2:
#     fake = f2.read()
#
# with open('/Users/shenyankun/Downloads/op_spam_v1.4/training.csv', 'w') as f3:
#     f3.write(truth)
#     f3.write(fake)

# shuffle the training file
df = pd.read_csv('/Users/shenyankun/Downloads/op_spam_v1.4/training.csv')
df = df.sample(frac=1)
df.to_csv('/Users/shenyankun/Downloads/op_spam_v1.4/training_shuffle.csv')