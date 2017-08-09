### Resources
### 1. PySpark's documentation for the RDD data structure 
###    (http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD)
### 2. Visual representation of methods (IPython Notebook format) 
###    (http://nbviewer.jupyter.org/github/jkthompson/pyspark-pictures/blob/master/pyspark-pictures.ipynb)
### 3. Visual representation of methods (PDF format)
###    (http://training.databricks.com/visualapi.pdf)

# step1
### We don't need the hamlet@ at the beginning of these IDs for our data analysis
raw_hamlet = sc.textFile("hamlet.txt")
split_hamlet = raw_hamlet.map(lambda line: line.split('\t'))
split_hamlet.take(5)
def format_id(x):
    id = x[0].split('@')[1]
    results = list()
    results.append(id)
    if len(x) > 1:
        for y in x[1:]:
            results.append(y)
    return results

hamlet_with_ids = split_hamlet.map(lambda line: format_id(line))
hamlet_with_ids.take(10)

# step2
### we want to get rid of elements that don't contain any actual words hamlet_with_ids.take(5)
real_text = hamlet_with_ids.filter(lambda line: len(line) > 1)
hamlet_text_only = real_text.map(lambda line: [l for l in line if l != ''])
hamlet_text_only.take(10)

# step3
### Remove any list items that only contain the pipe character (|), 
### and replace any pipe characters that appear within strings with an empty character.
hamlet_text_only.take(10)
def fix_pipe(line):
    results = list()
    for l in line:
        if l == "|":
            continue
        elif "|" in l:
            fmtd = l.replace("|", "")
            results.append(fmtd)
        else:
            results.append(l)
    return results

clean_hamlet = hamlet_text_only.map(lambda line: fix_pipe(line))