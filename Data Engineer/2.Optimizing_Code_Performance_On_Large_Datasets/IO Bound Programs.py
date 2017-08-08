##################################################################################################################
###  I/O Bound Programs
### In this section, we Learn how to process data more quickly by being aware of I/O bounds.
##################################################################################################################


### CPU bound tasks will:
#### 1. Execute faster if you optimize the algorithm.
#### 2. Execute faster if your processor has a higher clock speed (can execute more operations).


### I/O bound tasks are tasks where:
#### 1. Our program is reading from an input (like a CSV file).
#### 2. Our program is writing to an output (like a text file).
#### 3. Our program is waiting for another program to execute something (like a SQL query).
#### 4. Our program is waiting for another server to execute something (like an API request).