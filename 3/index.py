import sys

arr = []

for line in sys.stdin:
    arr.append(int(line))


def nextNumber(i):
    return(sum([int(x)**2 for x in str(i)]))



alreadyhad = []
def isluckynumber(i):
    if len(alreadyhad) == 0:
        alreadyhad.append(i)
    alreadyhad.append(nextNumber(alreadyhad[-1]))
    if(alreadyhad[-1] == 1):
        return True
    elif(len(alreadyhad) != len(set(alreadyhad))):
        return False
    else:
        return isluckynumber(alreadyhad[-1])



cnt = 0
for i in range(arr[0], arr[1], 1):
    if isluckynumber(i):
        cnt += 1
    alreadyhad.clear()
print(cnt)
