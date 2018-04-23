import sys

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
