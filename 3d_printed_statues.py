import sys

# Recursive Dynamic Programming
def minDays(s, p):
        if s - p > 0:
            solutions = []
                for k in range(p+1):
                    solutions.append(minDays(s - p + k , p + k))
            return 1 + min(solutions)
        else:
            return 1



for line in sys.stdin:
    n = int(line)

for k in range(n)
    s = k+1
    solutions = []
    for i in range(p+1)
        try:
            solutions.append(1+min_days[s-p+i][p+i])
        except IndexError:
            min_days[s-p+i][p+i] = minDays(s-p+i,p+i)
            solutions.append(1+min_days[s-p+i][p+i])
    min_days[s][p] = min(solutions)

print(min_days[n][1])
