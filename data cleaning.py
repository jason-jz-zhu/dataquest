# like union all
z = pd.concat([x,y], axis=0)

# filter used columns
used_field = ['DBN', 'rr_s']
survey = survey.loc[:,used_field]

# example using apply()
# we'll need to add a leading 0
# to the CSD if the CSD is less than two digits long
def pad_csd(num):
    tmp = str(num)
    if len(tmp) > 1:
        return tmp
    else:
        return tmp.zfill(2)

data["class_size"]["padded_csd"] = data["class_size"]["CSD"].apply(pad_csd)

# combine two columns into one
dataframe["new_column"] = dataframe["column_one"] + dataframe["column_two"]

# convert object to int
data[c] = pd.to_numeric(data[c], errors='coerce')

# filter value like where
class_size = class_size[class_size["GRADE "] == "09-12"]

# group by and agg Function
class_size = class_size.groupby("DBN").agg(numpy.mean)

# reset index
class_size.reset_index(inplace=True)

# merge like join
combined = data["sat_results"]
combined = combined.merge(data["ap_2010"], on="DBN", how="left")

# check row and column number
combined.shape

# fill missing value with mean
combined = combined.fillna(combined.mean())
# fill remaining missing value with 0
# this is becuase  if a column consists entirely of null or NaN values,
# pandas won't be able to fill in the missing values when we use
# the df.fillna() method along with the df.mean() method,
# because there won't be a mean.
combined = combined.fillna(0)
