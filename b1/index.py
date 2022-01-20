def maxCrossingSum(arr, l, m, h):
    sm = 0
    left_sum = -10000
    for i in range(m, l-1, -1):
        sm = sm + arr[i]
        if (sm > left_sum):
            left_sum = sm
    sm = 0
    right_sum = -1000
    for i in range(m + 1, h + 1):
        sm = sm + arr[i]
        if (sm > right_sum):
            right_sum = sm
    return max(left_sum + right_sum, left_sum, right_sum)

def maxSubArraySum(arr, l, h):
    if (l == h):
        return arr[l]
    midden = (l + h) // 2
    return max(maxSubArraySum(arr, l, m),
               maxSubArraySum(arr, m+1, h),
               maxCrossingSum(arr, l, m, h))
#input array
arr = [30, 98, 59, 38, 35, 78, 94, 66, -75, 97, -34, -20, -61, 91, 13, 51, 41, -97, 58, 49, -16, 49, 1, -12, -82, 86, -7, -32, -78, -80]
n = len(arr)

maximum = maxSubArraySum(arr, 0, n-1)
print(maximum)
