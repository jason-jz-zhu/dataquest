# -*- coding: utf-8 -*-
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

import cProfile
import sqlite3

query = "SELECT DISTINCT teamID from Teams inner join TeamsFranchises on Teams.franchID == TeamsFranchises.franchID where TeamsFranchises.active = 'Y';"
conn = sqlite3.connect("lahman2015.sqlite")

cur = conn.cursor()
teams = [row[0] for row in cur.execute(query).fetchall()]
query = "SELECT SUM(HR) FROM Batting WHERE teamId=?"
def calculate_runs(teams):
    home_runs = []
    for team in teams:
        runs = cur.execute(query, [team]).fetchall()
        runs = runs[0][0]
        home_runs.append(runs)
    return home_runs

profile_string = "home_runs = calculate_runs(teams)"
cProfile.run(profile_string)


###　in-memory SQLite database
import sqlite3

memory = sqlite3.connect(':memory:') # create a memory database
disk = sqlite3.connect('lahman2015.sqlite')

dump = "".join([line for line in disk.iterdump() if "Batting" in line])
memory.executescript(dump)

cur = memory.cursor()
query = "SELECT SUM(HR) FROM Batting WHERE teamId=?"
def calculate_runs(teams):
    home_runs = []
    for team in teams:
        runs = cur.execute(query, [team]).fetchall()
        runs = runs[0][0]
        home_runs.append(runs)
    return home_runs

profile_string = "home_runs = calculate_runs(teams)"
cProfile.run(profile_string)


### Python 3 threading library to implement threading in our programs
import threading
import time

def task(team):
    time.sleep(3)
    print(team)
for i, team in enumerate(teams):
    thread = threading.Thread(target=task, args=(team,))
    thread.start()
    print("Started task {}".format(i))

print(teams)