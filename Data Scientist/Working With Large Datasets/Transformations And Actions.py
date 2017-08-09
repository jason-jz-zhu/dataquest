raw_hamlet = sc.textFile('hamlet.txt')
split_hamlet = raw_hamlet.map(lambda line: line.split('\t'))

## flatMap() is different than map() because it doesn't require an output for every element in the RDD. 
## The flatMap() method is useful whenever we want to generate a sequence of values from an RDD.

def hamlet_speaks(line):
    id = line[0]
    speaketh = False
    
    if "HAMLET" in line:
        speaketh = True
    
    if speaketh:
        yield id,"hamlet speaketh!"

hamlet_spoken = split_hamlet.flatMap(lambda x: hamlet_speaks(x))
hamlet_spoken.take(10)

### Output
### Out[1]: 
### [('hamlet@0', 'hamlet speaketh!'),
###  ('hamlet@75', 'hamlet speaketh!'),
###  ('hamlet@1004', 'hamlet speaketh!'),
###  ('hamlet@9144', 'hamlet speaketh!'),
###  ('hamlet@12313', 'hamlet speaketh!'),
###  ('hamlet@12434', 'hamlet speaketh!'),
###  ('hamlet@12760', 'hamlet speaketh!'),
###  ('hamlet@12858', 'hamlet speaketh!'),
###  ('hamlet@14821', 'hamlet speaketh!'),
###  ('hamlet@15261', 'hamlet speaketh!')]

def filter_hamlet_speaks(line):
    if "HAMLET" in line:
        return True
    else:
        return False
    
hamlet_spoken_lines = split_hamlet.filter(lambda line: filter_hamlet_speaks(line))
hamlet_spoken_lines.take(5)

### Output
### Out[1]: 
### [['hamlet@0', '', 'HAMLET'],
###  ['hamlet@75', 'HAMLET', 'son to the late, and nephew to the present king.'],
###  ['hamlet@1004', '', 'HAMLET'],
###  ['hamlet@9144', '', 'HAMLET'],
###  ['hamlet@12313',
###   'HAMLET',
###   '[Aside]  A little more than kin, and less than kind.']]

## Count(): The count() method returns the number of elements in an RDD. 
##          count() is useful when we want to make sure the result of a transformation contains the right number of elements.

## Collect(): Running .collect() on an RDD returns a list representation of it.

spoken_count = 0
spoken_101 = list()
spoken_count = hamlet_spoken_lines.count()
spoken_collect = hamlet_spoken_lines.collect()
spoken_101 = spoken_collect[100]