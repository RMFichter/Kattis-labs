import sys

inputs = []
for line in sys.stdin:
    inputs.append(line)

integers = [len(word) for word in inputs]
if integers[0]<integers[1]:
    print("no")
else:
    print("go")
