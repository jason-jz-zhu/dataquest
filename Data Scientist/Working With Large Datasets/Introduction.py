## Hadoop consists of a file system (Hadoop Distributed File System, or HDFS) and its own implementation of the MapReduce paradigm. 
## MapReduce converts computations into Map and Reduce steps that Hadoop can easily distribute over many machines. 

## Hadoop made it possible to analyze large data sets, but relied heavily on disk storage (rather than memory) for computation. 


## Hadoop wasn't a great solution for calculations requiring multiple passes over the same data or many intermediate steps, 
## due to the need to write to and read from the disk between each step. 
## This drawback also made Hadoop difficult to use for interactive data analysis, the main task data scientists need to do.

## Spark, which uses distributed, in-memory data structures to improve speeds for many data processing workloads by several orders of magnitude.

## The core data structure in Spark is a resilient distributed data set (RDD). As the name suggests, an RDD is Spark's representation of a data set that's distributed across the RAM, 
## or memory, of a cluster of many machines. An RDD object is essentially a collection of elements we can use to hold lists of tuples, 
## dictionaries, lists, etc. Similar to a pandas DataFrame, we can load a data set into an RDD, 
## and then run any of the methods accesible to that object.

## PySpark: allows us to interface with RDDs in Python
## Py4J: Python can interface with Java objects (in our case RDDs) and one of the tools that makes PySpark work.
## SparkContext: object manages the connection to the clusters, and coordinates the running of processes on those clusters. More specifically, it connects to the cluster managers.

# 1. 
## We automatically have access to the SparkContext object sc.
## We then run the following code to read the TSV data set into an RDD object raw_data:
raw_data = sc.textFile("daily_show.tsv")
# 2.
## We then use the take() method to print the first five elements of the RDD
raw_data.take(5)

### output
### Out[1]: 
### ['YEAR\tGoogleKnowlege_Occupation\tShow\tGroup\tRaw_Guest_List',
###  '1999\tactor\t1/11/99\tActing\tMichael J. Fox',
###  '1999\tComedian\t1/12/99\tComedy\tSandra Bernhard',
###  '1999\ttelevision actress\t1/13/99\tActing\tTracey Ullman',
###  '1999\tfilm actress\t1/14/99\tActing\tGillian Anderson']


## On the previous screen, Spark waited to load the TSV file into an RDD until raw_data.take(5) executed. 
## When our code called raw_data = sc.textFile("dail_show.tsv"), 
## Spark created a pointer to the file, but didn't actually read it into raw_data until raw_data.take(5) needed that variable to run its logic.


## The key idea to understand when working with Spark is data pipelining. 
## Every operation or calculation in Spark is essentially a series of steps that we can chain together 
## and run in succession to form a pipeline. Each step in the pipeline returns either a Python value (such as an integer), 
## a Python data structure (such as a dictionary), or an RDD object. We'll start with the map() function.

## map(f): function applies the function f to every element in the RDD. 
## Because RDDs are iterable objects (like most Python objects), Spark runs function f on each iteration and returns a new RDD.
# 3. 
daily_show = raw_data.map(lambda line: line.split('\t'))
daily_show.take(5)

### output
### Out[1]: 
### [['YEAR', 'GoogleKnowlege_Occupation', 'Show', 'Group', 'Raw_Guest_List'],
###  ['1999', 'actor', '1/11/99', 'Acting', 'Michael J. Fox'],
###  ['1999', 'Comedian', '1/12/99', 'Comedy', 'Sandra Bernhard'],
###  ['1999', 'television actress', '1/13/99', 'Acting', 'Tracey Ullman'],
###  ['1999', 'film actress', '1/14/99', 'Acting', 'Gillian Anderson']]


## There are two types of methods in Spark:
## 1. Transformations - map(), reduceByKey()
## 2. Actions - take(), reduce(), saveAsTextFile(), collect()
## Transformations are lazy operations that always return a reference to an RDD object. 
## Spark doesn't actually run the transformations, though, until an action needs to use the RDD resulting from a transformation. 
## Any function that returns an RDD is a transformation, and any function that returns a value is an action.


## RDD objects are immutable, meaning that we can't change their values once we've created them.

# 4.
## python code
import collections
tally = collections.defaultdict(int)
for line in daily_show:
    tally[line[0]] += 1

print tally

## spark code
tally = daily_show.map(lambda x: (x[0], 1)).reduceByKey(lambda x,y: x+y)

tally.take(tally.count())

# 5.
## We need a way to remove the element ('YEAR', 1) from our collection
def filter_year(line):
    if line[0] == 'YEAR':
        return False
    else:
        return True

filtered_daily_show = daily_show.filter(lambda line: filter_year(line))

# 6.
## we'll filter out actors for whom the profession is blank, 
## lowercase each profession, generate a histogram of professions, 
## and output the first five tuples in the histogram.
filtered_daily_show.filter(lambda line: line[1] != '') \
                   .map(lambda line: (line[1].lower(), 1)) \
                   .reduceByKey(lambda x,y: x+y) \
                   .take(5)