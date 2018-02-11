#  use value_counts() to display the counts of how many times each category
data['Do you celebrate Thanksgiving?'].value_counts()

# convert to date
df['col'] = pd.to_datetime(df['col'])

# extract month
unrate['MONTH'] = unrate['DATE'].dt.month
