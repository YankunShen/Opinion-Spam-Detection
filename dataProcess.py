import random
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


def split(textpath, labelpath, train_text_path, train_label_path, val_text_path, val_label_path, split_count):
    with open(textpath, 'r') as txtf, open(labelpath, 'r') as labf:
        texts = txtf.readlines()
        labs = labf.readlines()
    idx = random.sample(range(len(texts)), len(texts))
    texts = [clean(texts[i]) for i in idx]
    labs = [labs[i] for i in idx]

    val_texts = texts[: split_count]
    val_labs = labs[: split_count]
    train_texts = texts[split_count:]
    train_labs = labs[split_count:]

    with open(train_text_path, 'w') as txtf, open(train_label_path, 'w') as labf:
        for r, l in zip(train_texts, train_labs):
            txtf.write(r + '\n')
            labf.write(l)

    with open(val_text_path, 'w') as txtf, open(val_label_path, 'w') as labf:
        for r, l in zip(val_texts, val_labs):
            txtf.write(r + '\n')
            labf.write(l)





if __name__=='__main__':
    split('/Users/shenyankun/Downloads/op_spam_v1.4/opspam_review.txt', '/Users/shenyankun/Downloads/op_spam_v1.4/opspam_label.txt',
          '/Users/shenyankun/Downloads/op_spam_v1.4/train_review.txt', '/Users/shenyankun/Downloads/op_spam_v1.4/train_label.txt',
          '/Users/shenyankun/Downloads/op_spam_v1.4/val_review.txt', '/Users/shenyankun/Downloads/op_spam_v1.4/val_label.txt', 320)

    split('/Users/shenyankun/Downloads/op_spam_v1.4/val_review.txt', '/Users/shenyankun/Downloads/op_spam_v1.4/val_label.txt',
          '/Users/shenyankun/Downloads/op_spam_v1.4/val_review.txt', '/Users/shenyankun/Downloads/op_spam_v1.4/val_label.txt',
          '/Users/shenyankun/Downloads/op_spam_v1.4/test_review.txt', '/Users/shenyankun/Downloads/op_spam_v1.4/test_label.txt', 160)