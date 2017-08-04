# we can observe how the BlockManager organizes the data in the dataframe using DataFrame._data private attribute
import pandas as pd
moma = pd.read_csv("moma.csv")

### DataFrame._data
### 1. check all column names
### 2. check which columns belong to which type of value 
print moma._data

### Series.nbytes
### 1. retrieve the amount of memory the values in a column consume
print moma['']._data

### DataFrame.info()
### 1. calculate the estimated shallow memory footprint
### 2. calcuate the 
print moma.info()

### DataFrame.size()
### 1. calcuate the number of element in the dataframe
print moma.size()