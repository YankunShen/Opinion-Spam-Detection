import pandas as pd
import csv


with open('/Users/shenyankun/Downloads/op_spam_v1.4/positive_polarity/training_truthful.csv', 'r') as f1:
    truth = f1.read()

with open('/Users/shenyankun/Downloads/op_spam_v1.4/positive_polarity/training_deceptive.csv', 'r') as f2:
    fake = f2.read()

with open('/Users/shenyankun/Downloads/op_spam_v1.4/positive_polarity/training.csv', 'w') as f3:
    f3.write(truth)
    f3.write(fake)