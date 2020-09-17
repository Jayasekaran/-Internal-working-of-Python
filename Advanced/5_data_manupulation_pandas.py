import numpy as np
import pandas as pd
# coppy the csv file - president_heights.csv
data = pd.read_csv('data\president_heights.csv')
print(data)
heights = np.array(data['height(cm)'])
print(heights)

#compute a variety of summary statistics    
print("Mean height:       ", heights.mean())
print("Standard deviation:", heights.std())
print("Minimum height:    ", heights.min())
print("Maximum height:    ", heights.max())

# compute quantiles
print("25th percentile:   ", np.percentile(heights, 25))
print("Median:            ", np.median(heights))
print("75th percentile:   ", np.percentile(heights, 75))

#Pandas Series is a one-dim array of indexed data. It can be created from a list or array :
data = pd.Series([0.25, 0.5, 0.75, 1.0])
print("# Pandas Series : \n",data)
print("# sequence of value  : \n",data.values)
print("# sequence of indices  : \n",data.index)
print("# accessed by the associated index  : \n",data[1:3])

data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=['a', 'b', 'c', 'd'])
print("# Pandas Series : \n",data)

# Series as specialized dictionary
population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(population_dict)
print("# population series from dict : \n",population)
print("# access the population from the series: \n",population['California':'Illinois'])

#Pandas DataFrame Object
#DataFrame is an analog of a two-dimensional array with both flexible row indices and flexible column name

area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
             'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)
print("# area- series from dict : \n",area)

# construct a single two-dimensional object containing population and area
states = pd.DataFrame({'population': population,
                       'area': area})
print("# DataFrame from series : \n", states)
print("# access to the index labels: : \n", states.index)
print("# access to the col labels: : \n", states.columns)