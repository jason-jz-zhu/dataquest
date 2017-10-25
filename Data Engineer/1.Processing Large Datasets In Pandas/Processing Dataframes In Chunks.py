##################################################################################################################
###  Processing Dataframes In Chunks
### In this section, we Learn how to break a problem down into dataframe chunks.
### We need a different strategy for working with data sets that don't fit into memory even after we've optimized types and filtered columns.
### Instead of trying to load the full data set into memory, we can load and process it in chunks
##################################################################################################################


#Step1: select the correct chunk size
### Given that we want each chunk to consume less than 50% of our total available memory
### The pandas.read_csv() function makes this workflow easier for us.
### It has a chunksize parameter that we can use to specify the number of rows we want each dataframe chunk to contain
import pandas as pd
memory_footprints = []
chunk_iter = pd.read_csv("moma.csv", chunksize=250)
for chunk in chunk_iter:
    memory_footprints.append(chunk.memory_usage(deep=True).sum()/(1024*1024))

### do some calculate among chunk
%%timeit
dtypes = {"ConstituentBeginDate": "float", "ConstituentEndDate": "float"}
chunk_iter = pd.read_csv("C:/Users/Jiazhen/Downloads/moma.csv", chunksize=250, dtype=dtypes)
lifespans = []
for chunk in chunk_iter:
    #### pd.Series - pd.Series = pd.Series
    diff = chunk['ConstituentEndDate'] - chunk['ConstituentBeginDate']
    lifespans.append(diff)
#### pd.concat() function
lifespans_dist = pd.concat(lifespans)
# >> series_list = [pd.Series([1,2]), pd.Series([2,3])]
# >> pd.concat(series_list)
# 0    1
# 1    2
# 0    2
# 1    3
# dtype: int64
print(lifespans_dist)

### reading in only those two columns for each dataframe chunk
### it saves 2/3 time
%%timeit
lifespans = []
chunk_iter = pd.read_csv("moma.csv", chunksize=250, dtype={"ConstituentBeginDate": "float", "ConstituentEndDate": "float"},  usecols=['ConstituentBeginDate', 'ConstituentEndDate'])
for chunk in chunk_iter:
    lifespans.append(chunk['ConstituentEndDate'] - chunk['ConstituentBeginDate'])
lifespans_dist = pd.concat(lifespans)


### Series.value_counts() can calcuate the distribution of this column
### Counting Unique Values
chunk_iter = pd.read_csv("moma.csv", chunksize=250, usecols=['Gender'])
overall_vc = list()
for chunk in chunk_iter:
    chunk_vc = chunk['Gender'].value_counts()
    overall_vc.append(chunk_vc)
combined_vc = pd.concat(overall_vc)
final_vc = combined_vc.groupby(combined_vc.index).sum()
print(combined_vc)
print final_vc

### Now we want to understand how the gender distribution changed with each exhibition, but we have memory constraints relative to the full data set.
### approach 1
moma = pd.read_csv("moma.csv", usecols=['ExhibitionID', 'Gender'])
id_gender_counts = moma['Gender'].groupby(moma['ExhibitionID']).value_counts()

### approach 2
### Working With Intermediate Dataframes
chunk_iter = pd.read_csv("moma.csv", chunksize=250)
df_list = []
for chunk in chunk_iter:
    temp = chunk['Gender'].groupby(chunk['ExhibitionID']).value_counts()
    df_list.append(temp)
final_df = pd.concat(df_list)
id_gender_counts = final_df.groupby(final_df.index).sum()
