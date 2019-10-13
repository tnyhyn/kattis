def plant(arr):
    arr.sort(reverse=True)
    for i in range(len(arr)):
        arr[i] += i + 1
    return max(arr) + 1


t = int(input())
n = [int(i) for i in input().split(' ')]
print(plant(n))