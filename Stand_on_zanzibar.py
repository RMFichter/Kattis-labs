import sys

inputs = []
for line in sys.stdin:
    stringlist = line.split()
    intlist = [int(string) for string in stringlist]
    inputs.append(intlist)


outputs = []
for line in inputs:
    if len(line) > 1:
        lb=0
        for i in range(len(line)-1):
            if line[i+1]-2*line[i] > 0:
                lb += line[i+1]-2*line[i]
        outputs.append(lb)

for lb in outputs:
    print(lb)
