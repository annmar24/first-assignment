import pandas as pd
from statistics import mean
from math import trunc

with open('train.tsv', 'rb') as f:
    data = pd.read_csv(f, sep='\t',  names=['price', 'rooms', 'area', 'level', 'address', 'description'])
    #calculate mean price
    mean0 = trunc(mean(data['price']))
    #open file and write mean to it
    out0 = open('out0.csv', 'w')
    out0.write(str(mean0))

    #calculate price per meter
    price = data['price'] / data['area']
    data['price_per_meter'] = price
    mean_per_meter = mean(data['price_per_meter'])

    #select rows where there are more than twa room and price is lower than mean price per meter
    selector = data[(data['rooms'] >= 3) & (data['price_per_meter'] < mean_per_meter)]
    #write to file
    selector.to_csv('out1.csv', sep='\t', columns=['rooms', 'price', 'price_per_meter'], header=0, index=0)

