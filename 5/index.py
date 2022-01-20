import sys

arr = []

for line in sys.stdin:
	line = line.strip()
	arr.append([int(i) for i in line.split(" ")])


arr.pop
print(arr)
