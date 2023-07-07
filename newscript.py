# how  to import a function from one script to another see you the folling 
# the function count which exist in the textanalysis.py script .
from textanalysis import count
count_result = count('general.txt', 'that')
print("{} words".format(count_result))

help(count)



