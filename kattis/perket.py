from sys import stdin


def ans(arr):
    def calculate_bs(arr):
        if not arr: return float('inf')
        sour, bitterness = 1, 0
        for i,j in arr:
            sour *= i
            bitterness += j
        return abs(sour - bitterness)

    def recur(pair, arr):
        if not arr: return calculate_bs(pair)
        return min(recur(pair + [arr[0]], arr[1:]), recur(pair, arr[1:]))
    min_sum = recur([], arr)
    print(min_sum)

n = int(input())
ingre = []
for i in range(n):
    k = [int(i) for i in stdin.readline().split()]
    ingre.append(k)
ans(ingre)
