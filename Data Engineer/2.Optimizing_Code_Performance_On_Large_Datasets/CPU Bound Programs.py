##################################################################################################################
###  CPU Bound Programs
### In this section, we Learn how to Learn how to process data more quickly by being aware of CPU bounds
##################################################################################################################

### Finding Duplicate Values
iz_operations = 0
# Initialize a list to store our duplicates
duplicates = []

### The time.time function gives us the elapsed time in seconds since January 1st, 1970. 
### This means subtracting one time from another gives you the number of seconds in between the times
import time
start = time.time()

### We're timing how long this line takes to run.
duplicates = []

elapsed = time.time() - start
print("Took {} seconds to run.".format(elapsed))

### timing code run between hashmap and DataFrame.duplicated() function
import time
start = time.time()

duplicate_series = query_series.duplicated()
duplicate_values_series = query_series[duplicate_series]

pandas_elapsed = time.time() - start
print(pandas_elapsed)

start = time.time()
counts = {}
for item in query:
    if item not in counts:
        counts[item] = 0
    counts[item] += 1

duplicates = []
for key, val in counts.items():
    if val > 1:
        duplicates.append(key)
elapsed = time.time() - start
print(elapsed)

### Stable Time Estimates
import time
import statistics
import matplotlib.pyplot as plt
def pandas_algo():
    duplicate_series = query_series.duplicated()
    duplicate_values_series = query_series[duplicate_series]
    
def algo():
    counts = {}
    for item in query:
        if item not in counts:
            counts[item] = 0
        counts[item] += 1

    duplicates = []
    for key, val in counts.items():
        if val > 1:
            duplicates.append(key)
        
pandas_elapsed = []
for i in range(1000):
    start = time.time()
    pandas_algo()
    pandas_elapsed.append(time.time() - start)

elapsed = []
for i in range(1000):
    start = time.time()
    algo()
    elapsed.append(time.time() - start)

print(statistics.median(pandas_elapsed))
print(statistics.median(elapsed))

plt.hist(pandas_elapsed)
plt.show()
plt.hist(elapsed)


### The general process behind refactoring is:

### 1. Measure how long the current code takes to run.
### 2. Rewrite the code so that the algorithm you want is nicely isolated from the rest of the code.
###    Ideally, it will be a function, with defined inputs and outputs.
### 3. Try rewriting the algorithm to reduce time complexity.
### 4. Measure the new algorithm to see if it's faster.
### 5. Rinse and repeat as needed.


### There are tools that can automatically profile your code, without you having to insert lines. Here are a few:

### 1. cProfile will show you how much time was spent in various levels of your application.
### 2. The unix time command. Calling your program from the command line with syntax like time python script.py 
###    will show you how long your program took to run.
### 3. The contexttimer package will enable you to quickly time parts of your program without having to add lots of code.
### 4. The lineprofiler package will show you how long each line of a profiled function takes to execute.
import cProfile
cProfile.run('print(10)')

### Practicing Writing Efficient Algorithms
import time 
import statistics
def run_with_timing(func):
    elapsed = []
    for i in range(10):
        start = time.time()
        func()
        elapsed.append(time.time() - start)
    return statistics.median(elapsed)

def pandas_algo():
    get_max_relevance = lambda x: x.loc[x["relevance"].idxmax(), "product_link"]
    return data.groupby("query").apply(get_max_relevance)

def algo():
    links = {}
    for i, row in enumerate(query):
        if row not in links:
            links[row] = [0,""]
        if relevance[i] > links[row][0]:
            links[row] = [relevance[i], product_link[i]]
    return links

print(run_with_timing(pandas_algo))
print(run_with_timing(algo))

### output
### 0.3030010461807251
### 0.01077723503112793