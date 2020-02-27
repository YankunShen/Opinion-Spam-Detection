import re


def clean(s, char=False):
    ns = s.lower()
    ns = ns.replace('<br />', ' ')
    ns = re.sub('[0-9]+', 'N', ns)  # replace num with 'N'
    ns = re.sub('[^a-zA-Z0-9 \-.,\'\"!?()]', ' ', ns)  # Eliminate all but these chars
    # r'...' denotes raw strings which ignore escape code, i.e., r'\n' is '\'+'n'
    ns = re.sub('([.,!?()\"\'])', r' \1 ', ns)  # Space out punctuation
    ns = re.sub('\s{2,}', ' ', ns)  # Trim ws
    str.strip(ns)
    return ns


with open('/Users/shenyankun/Downloads/op_spam_v1.4/positive_polarity/training/train_review.txt', 'r') as f1:
    reviews = f1.read()
    clean(reviews)
