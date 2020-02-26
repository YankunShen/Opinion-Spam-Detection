import os

# combine all separate files into one whole file

# get all file names
fnames = []

for root, d_names, f_names in os.walk('/Users/shenyankun/Downloads/op_spam_v1.4/positive_polarity/deceptive_from_MTurk'):
    for f in f_names:
        fnames.append(os.path.join(root, f))

print('fnames=', fnames)

with open('/Users/shenyankun/Downloads/op_spam_v1.4/positive_polarity/deceptive_from_MTurk.txt', 'w') as f:
    for file_name in fnames:
        if ".DS_Store" in file_name:
            continue
        file = open(file_name, 'r')
        data = file.read()
        f.write(data)
        f.write('\n')