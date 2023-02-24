from urllib import request
from scipy.stats import pearsonr
import plotly.express as px
import pandas as pd

#global variables
headers = []
data = []
years = []
smoothing = []
relation_between_values = []

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

#slipt data

for x in data:
    years.append(float(x[0]))
    smoothing.append(float(x[1]))

df = pd.DataFrame(list(zip(years, smoothing)), columns=['year', 'smoothing'])

#pearson correlation

pearson_correlation = pearsonr(years, smoothing)
# print(pearson_correlation)

#scatter graphic

title_graphic = 'PValue: ' + str(pearson_correlation.pvalue) + ', Statistic: ' + str(pearson_correlation.statistic)
graphic = px.scatter(df, x='year', y='smoothing', title=title_graphic, trendline="ols")
graphic.show()