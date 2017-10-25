##################################################################################################################
###  Optimizing Dataframe Memory Footprint
### In this section, we Learn how to reduce a Dataframe's memory footprint by selecting the correct data types
##################################################################################################################

# we can observe how the BlockManager organizes the data in the dataframe using DataFrame._data private attribute
import pandas as pd
moma = pd.read_csv("moma.csv")

# in order to check the types or footprint for a dataframe, we can use the following steps to check them.


### DataFrame._data
### 1. check all column names
### we can retrieve the internal BlockManager object
print moma._data

## Step1:
### Series.nbytes
### 1. retrieve the amount of memory the values in a column
print moma['']._data

## Step2:
### DataFrame.info()
### Goal: calculate the estimated shallow memory footprint
### Note: very estimated and basic memory (overview)
### Why: why we just can calculate the estimated memory
### Ans: numeric values (like float64 type) use the Numpy ndarrays, so we can calculate the accuracely memory
###      But for string values (like object type) use list of python, so we just can calculate the pointers memory (at least 8 bytes)
###      list of python and Numpy ndarrays are very different. Numpy ndarray is more efficiency
print moma.info()

## Step3
### DataFrame.info(memory_usage='deep')
### calculate the true memory footprint (total) (include actual linked string values)
print moma.info(memory_usage='deep')

## Step4:
### DataFrame.memory_usage(deep=True)
### calcuate the true momery footprint (each column)
print moma.memory_usage(deep=True)
### get sum momery footprint
### res: mb
print moma.memory_usage(deep=True).sum()/(1024*1024)


### DataFrame.select_dtypes()
### select one or more types' columns' dataframe
obj_cols_df = moma.select_dtypes(include=['object'])


### DataFrame.size
### calcuate the number of element (cells) in the dataframe
print moma.size


### types in pandas
###
### types:  object  bool  float(bytes)    int(bytes)   datetime
### values: object  bool  float16(2)      int8(1)      datetime64
### values:               float32(4)      int16(2)
### values:               float64(8)      int32(4)
### values:               float128(16)    int64(8)

### numpy.iinfo()
### get the type of max, min value
import numpy as np
np.iinfo('int8').min
np.iinfo('int8').max

### We can save memory by converting within the same type (from float64 to float32 for example),
### or by converting between types (from float64 to int32)

### saving memory using converting, we need to take care of missing values in numeric columns using a float subtype
### because the NumPy int type doesn't have a missing value object (like NaN for float values)
### find all float types' missing value count
moma.select_dtypes(include=['float']).isnull().sum()
### convert to one type
moma['ExhibitionSortOrder'].astype('int64')

### To help find the most space efficient type for a column, we can use the pandas.to_numeric() function.
### First, we need to convert to the general dtype,
### then use the downcast parameter when calling this function to ask pandas to find the optimal subtype
float_cols = moma.select_dtypes(include=['float'])
print float_cols.dtypes
for col in float_cols.columns:
    moma[col] = pd.to_numeric(moma[col], downcast='float')
print(moma['ExhibitionID'].dtypes)


### We can use the pandas.to_datetime() function to convert a column to the datetime type.
### This method accepts and returns a series object that we can assign back to the dataframe.
moma["ExhibitionBeginDate"] = pd.to_datetime(moma["ExhibitionBeginDate"])
moma["ExhibitionEndDate"] = pd.to_datetime(moma["ExhibitionEndDate"])

### Converting To Categorical To Save Memory
### We should stick to using the category type primarily for object columns where less than 50% of the values are unique
### We can't do arithmetic with category columns or use methods like Series.min() and Series.max() without converting to a true numeric dtype first.
### check count for each value in one column
print(moma['ConstituentType'].value_counts())

### convert to category type
### The category subtype handle missing values by setting them to -1
moma['ConstituentType'] = moma['ConstituentType'].astype('category')

### we use the Series.cat.codes attribute to return the integer values the category type uses to represent each value
moma['ConstituentType'].cat.codes

### Series.unique()
### find all unique value in one series
moma[col].unique()


### Selecting Types While Reading The Data In
### The dtype parameter accepts a dictionary that has (string) column names as the keys and NumPy type objects as the values
import numpy as np
col_types = {"id": np.int32}
df = pd.read_csv('data.csv', dtypes=col_types)

### The parse_dates parameter accepts a list of strings containing the names of the columns we want to parse as datetime values.
df = pd.read_csv('data.csv', parse_dates=["StartDate", "EndDate"])

### we can use the usecols parameter to specify which columns we want to include
df = pd.read_csv('data.csv', usecols=["StartDate", "EndDate"])
