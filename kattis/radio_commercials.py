def radio(arr, cost):
    for i in range(len(arr)):
        arr[i] -= cost
    running_sum = arr[0]
    max_sum = arr[0]
    for i in range(1, len(arr)):
        running_sum = max(arr[i], running_sum + arr[i])
        max_sum = max(max_sum, running_sum)
    return max_sum

t = [int(i) for i in input().split(' ')]
n = [int(i) for i in input().split(' ')]

print(radio(n, t[1]))