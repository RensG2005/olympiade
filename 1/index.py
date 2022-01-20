import sys
 
 
for line in sys.stdin:
    count = 0
    arr = []
    for letter in line:
        if letter not in arr:
            arr.append(letter)
            count += 1
        else:
            continue
    print(count - 1)