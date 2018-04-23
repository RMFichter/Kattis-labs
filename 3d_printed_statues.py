import sys
import math

# ---------- Read Console input --------

for line in sys.stdin:
    n = int(line)

# ----------- DynP algorithm. -----------

best_solutions = [] #List to store list of best solutions for each number of statues and printers
# Fill in the best solutions when there are 0 statues left to build given that we started with n to build.
possible_no_printers = range(1,n+1) # Any more than n printers is completely unneccesary
solutions = [0 for i in possible_no_printers]
best_solutions.append(solutions) #If number of statues left to build is 0 the best number of days until finished is 0
solutions = [1 for i in possible_no_printers]
best_solutions.append(solutions) #If number of statues left to build is 1 the best number of days until finished is 1 regardless of how many printers you have.

for k in range(n-1):
    s=k+2 # want to iterate from 2 to n statues left to build.
    best_solutions.append([])
    for no_printers in reversed(possible_no_printers):
        if no_printers >= s: # While there are more than or equal amount of printers than statues left to build, we simply build them and it takes 1 day.
            best_solutions[s].insert(0,1)
        else:
            possible_solutions = []
            for x in range(max([0,2*no_printers - n]),no_printers+1): # For each feasible choice of number of statues to build:
                possible_solutions.append(1+best_solutions[s-x][min([2*no_printers - x,n])-1])
            best_solutions[s].insert(0,min(possible_solutions)) # Insert Optimal solution to number of days left for that choice if acting optimally after the choice

print(best_solutions[n-1][1-1]) # n statues to build, 1 printer at hand.
