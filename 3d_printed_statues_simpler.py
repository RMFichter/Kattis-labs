import sys

for line in sys.stdin:
    n = int(line)

# The key for this problem is to realize that if you have less printers than
# the number of statues to be printed, the optimal strategy is to simply
# let all the printers print a new printer.

p = 1 #number of printers at start
days = 0 #number of days that have passed.
while p<n:
    p = 2*p
    days +=1
days += 1 #We now print the statues.
print(days)
