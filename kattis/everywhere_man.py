n = int(input())
for i in range(n):
    words = set()
    k = int(input())
    for i in range(k):
        w = input()
        words.add(w)
    print(len(words))