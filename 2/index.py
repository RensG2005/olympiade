import sys

def decimalToBinary(n):  
    return bin(n).replace("0b", "")  

for line in sys.stdin:
    cnt = 0
    binary = decimalToBinary(int(line))
    reverse = binary[::-1]
    for letter in reverse:
        if letter == "0":
            cnt += 1
            reverse = reverse[1:]
        else:
            break
    print(str(cnt))
    print(int(reverse, 2))
            