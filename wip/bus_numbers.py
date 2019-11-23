from sys import stdin

def bn(arr):
    pairs = []
    arr.sort()
    l, r = 0, 0
    for i in range(len(arr)-1)):
        if (arr[i]+1) == arr[i+1]:




n = int(input())
l = [int(i) for i in stdin.readline().split()]
bn(l)