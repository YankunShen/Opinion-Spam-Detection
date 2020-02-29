import csv
import pandas as pd

with open('/Users/shenyankun/Downloads/op_spam_v1.4/training_shuffle.csv', mode='r') as origin:
    with open('/Users/shenyankun/Downloads/op_spam_v1.4/train_label.txt', mode='w') as f:
        reader = csv.DictReader(origin)
        for row in reader:
            f.write(row['label'])
            f.write('\n')
