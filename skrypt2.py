import pandas as pd

with open('train.tsv', 'rb') as f1, open('description.csv', 'rb') as f2:
    data1 = pd.read_csv(f1, sep='\t',  names=['price', 'rooms', 'area', 'level', 'address', 'description'])
    data2 = pd.read_csv(f2)
    new_data = data1.join(data2.set_index('liczba'), on='level')
    new_data.to_csv('out2.csv', sep='\t', index=0)

