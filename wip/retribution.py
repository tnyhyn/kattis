from sys import stdin, stdout
import math
import heapq


def main():
    def dist(p1, p2):
        return math.sqrt((p2[1] - p1[1])**2 + (p2[0] - p1[0])**2)

    n, m, p = stdin.readline().split()
    n, m, p = int(n), int(m), int(p)
    judges, tars, feathers = [0]*n, [0]*m, [0]*p
    for i in range(n):
        j1, j2= stdin.readline().split()
        judges[i] = [int(j1), int(j2)]
    for i in range(m):
        t1, t2= stdin.readline().split()
        tars[i] = [int(t1), int(t2)]
    for i in range(p):
        f1, f2= stdin.readline().split()
        feathers[i] = [int(f1), int(f2)]

    t_heap, f_heap = [], []
    [t_heap.append(((dist(tars[t], judges[j]), j, t))) for j in range(n) for t in range(m)]
    [f_heap.append(((dist(feathers[f], judges[j]), j, f))) for j in range(n) for f in range(p)]
    heapq.heapify(t_heap)
    heapq.heapify(f_heap)

    setj, settf = set(), set()
    sum = 0
    while n > len(setj):
        d, j, t = heapq.heappop(t_heap)
        if j not in setj and t not in settf:
            sum += d
            setj.add(j)
            settf.add(t)
    setj, settf = set(), set()
    while n > len(setj):
        d, j, f = heapq.heappop(f_heap)
        if j not in setj and f not in settf:
            sum += d
            setj.add(j)
            settf.add(f)
    print(round(sum, 6))



if __name__ == "__main__":
    main()
