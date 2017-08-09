### Before we can write and run SQL queries, we need to tell Spark to treat the DataFrame as a SQL table
### To register a DataFrame as a table, call the registerTempTable() method on that DataFrame object. This method requires one string parameter, name, 
### that we use to set the table name for reference in our SQL queries.


# step1
### Use the registerTempTable() method to register the DataFrame df as a table named census2010
### Then, run the SQLContext method tableNames to return the list of tables.
from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.registerTempTable('census2010')
tables = sqlCtx.tableNames()
print(tables)

# step2
### Write a SQL query that returns the age column from the table census2010, and use the show() method to display the first 20 results.
query = 'SELECT age FROM census2010'
sqlCtx.sql(query).show(20)

# step3
### The males and females columns (in that order) where age > 5 and age < 15
query = 'select males,females from census2010 where age > 5 and age < 15'
sqlCtx.sql(query).show()

# step4
### Write a SQL query that returns a DataFrame containing the males and females columns from the census2010 table.
### Use the describe() method to calculate summary statistics for the DataFrame and the show() method to display the results.
query = 'select males,females from census2010'
sqlCtx.sql(query).describe().show()

# step5
### Read these additional datasets into DataFrame objects and then use the registerTempTable() function 
### to register these tables individually within SQLContext:
df_2000 = sqlCtx.read.json("census_2000.json")
df_1990 = sqlCtx.read.json("census_1990.json")
df_1980 = sqlCtx.read.json("census_1980.json")

df_2000.registerTempTable('census2000')
df_1990.registerTempTable('census1990')
df_1980.registerTempTable('census1980')
tables = sqlCtx.tableNames()
print(tables)

# step6
### Write a query that returns a DataFrame with the total columns for the tables census2010 and census2000 (in that order)
query = """
 select census2010.total, census2000.total
 from census2010
 inner join census2000
 on census2010.age=census2000.age
"""

sqlCtx.sql(query).show()


### The functions and operators from SQLite that we've used in the past are available for us to use in Spark SQL:

### COUNT()
### AVG()
### SUM()
### AND
### OR



# step7
### Write a query that calculates the sums of the total column from each of the tables, in the following order
query = """
 select sum(census2010.total), sum(census2000.total), sum(census1990.total)
 from census2010
 inner join census2000
 on census2010.age=census2000.age
 inner join census1990
 on census2010.age=census1990.age
"""
sqlCtx.sql(query).show()