from urllib import request
import numpy as np
from scipy.stats import pearsonr

#global variables
headers = []
data = []
years = []
smoothing = []

#download file

data_url = 'https://data.giss.nasa.gov/gistemp/graphs/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.txt'
local_file = 'data.txt'
request.urlretrieve(data_url, local_file)

#read data

file = open('data.txt')
for index, line in enumerate(file):
    line_separate = line.split()
    if index == 3:
        headers = line_separate
    elif index > 4:
        data.append(line_separate)

#filter data, only years and No smoothing

for x in data:
    years.append(float(x[0]))
    smoothing.append(float(x[1]))

#pearson correlation

pearson_correlation = pearsonr(years, smoothing)
print(pearson_correlation)