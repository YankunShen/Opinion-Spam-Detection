import pandas as pd
import csv

# get training data


# convert .txt to .csv
data = pd.read_csv('/Users/shenyankun/Downloads/op_spam_v1.4/negative_polarity/deceptive_from_MTurk.txt', delimiter='\n', names=['review'], index_col=[0])
data.to_csv('/Users/shenyankun/Downloads/op_spam_v1.4/negative_polarity/deceptive_from_MTurk.csv')

# add a column to the .csv file -- label
data = pd.read_csv('/Users/shenyankun/Downloads/op_spam_v1.4/positive_polarity/deceptive_from_MTurk.csv')
print(data.head())
print(data.shape)

#create a csv file -- label
lines = data.shape[0]
print(lines)
with open('/Users/shenyankun/Downloads/op_spam_v1.4/negative_polarity/deceptive_from_MTurk_label.csv', 'w') as f:
    fileds = ['label']
    writer = csv.DictWriter(f, fieldnames=fileds)
    writer.writeheader()
    for l in range(lines):
        writer.writerow({'label': -1})
data = pd.read_csv('/Users/shenyankun/Downloads/op_spam_v1.4/negative_polarity/deceptive_from_MTurk_label.csv')
print(data.head())
print(data.shape)

train = pd.read_csv('/Users/shenyankun/Downloads/op_spam_v1.4/negative_polarity/deceptive_from_MTurk.csv')
label = pd.read_csv('/Users/shenyankun/Downloads/op_spam_v1.4/negative_polarity/deceptive_from_MTurk_label.csv')
print(label.head())

dataframe = train.join(label, lsuffix="left", rsuffix="right")
print(dataframe.head())
print(dataframe.shape)

dataframe.to_csv('/Users/shenyankun/Downloads/op_spam_v1.4/negative_polarity/training_deceptive.csv')
print(dataframe.shape)
