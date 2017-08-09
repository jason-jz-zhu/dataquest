### Unlike pandas, which can only run on one computer, Spark can use distributed memory (and disk when necessary) 
### to handle larger data sets and run computations more quickly.

### Spark DataFrames allow us to modify and reuse our existing pandas code to scale up to much larger data sets. 



# step1
### Print the first four lines of census_2010.json
f = open('census_2010.json')

for i in range(4):
    print(f.readline())
    
    
### The Spark SQL class is very powerful. 
### It gives Spark more information about the data structure we're using and the computations we want to perform. 
### Spark uses that information to optimize processes.

# step2
### use Spark SQL to read json file and put it into Spark dataframe
# Import SQLContext
from pyspark.sql import SQLContext

# Pass in the SparkContext object `sc`
sqlCtx = SQLContext(sc)

# Read JSON data into a DataFrame object `df`
df = sqlCtx.read.json("census_2010.json")

# Print the type
print(type(df))

# step3
### Call the printSchema() method on the Spark DataFrame df to display the schema that Spark inferred.
df.printSchema()

# step4
### Use the show() method to print the first five rows of the DataFrame.
df.show(5)

# Output
### +---+-------+-------+-------+----+
### |age|females|  males|  total|year|
### +---+-------+-------+-------+----+
### |  0|1994141|2085528|4079669|2010|
### |  1|1997991|2087350|4085341|2010|
### |  2|2000746|2088549|4089295|2010|
### |  3|2002756|2089465|4092221|2010|
### |  4|2004366|2090436|4094802|2010|
### +---+-------+-------+-------+----+

# step5
### Print the age value for each row object in first_five.
first_five = df.head(5)
for line in first_five:
    print(line.age)



# Pandas DataFrame
df['age']
df[['age', 'males']]

# Spark DataFrame
df.select('age')
df.select('age', 'males')

# step6
### Select the age, males, and females columns from the DataFrame and display them using the show() method.
df[['age', 'males', 'females']].show()
# is equal to
df.select('age', 'males', 'females').show()

# step7
### Use the pandas notation for Boolean filtering to select the rows where age is greater than five.
five_plus = df[df['age'] > 5]
five_plus.show()

# step8
### Find all of the rows where females is less than males, and use show() to display the first 20 results.
df[df['females'] < df['males']].show()

### we can convert a Spark DataFrame to a pandas DataFrame using the toPandas() method.
### Converting an entire Spark DataFrame to a pandas DataFrame works just fine for small data sets. 
### For larger ones, though, we'll want to select a subset of the data that's more manageable for pandas.

# step9
### Use the toPandas() method to convert the Spark DataFrame to a Pandas DataFrame, and assign it to the variable pandas_df.
### Then, plot a histogram of the total column using the hist() method.
pandas_df = df.toPandas()
pandas_df['total'].hist()