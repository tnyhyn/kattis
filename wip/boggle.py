from sys import stdin
from collections import deque, defaultdict


# Words with 3 or 4 letters count 1 point, words with 5 letters 2 points, 6 letters 3 points, 
# 7 letters 5 points. 8 letter words will give 11 points.

def boggle(di, A):
    score, words, longest_word = 0, 0, ''
    used = set()
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] in di:
                for word in di[A[i][j]]:
                    if word_exists(A, i, j, word):
                        words += 1
                        score += word_score(word)
    print(score, words)


def word_exists(A, i, j, word):
    directions = [(-1,0), (0,1), (1,0), (0,-1), (-1,-1), (-1,1), (1,1), (1,-1)]
    q = deque()
    q.append((word[0], i, j, set()))
    print("word: {}".format(word))
    while q:
        letters, i, j, seen = q.popleft()
        for c in word[1:]:
            if letters == word: 
                print("found", letters)
                return True
            for d in directions:
                ni, nj = i+d[0], j+d[1]
                # print("letters: {} | ni: {} | nj: {}".format(letters, ni, nj))
                # print("seen: {}".format(seen))
                if (ni, nj) in seen: continue
                if ni < 0 or ni >= len(A) or nj < 0 or nj >= len(A[0]):
                    continue
                if A[ni][nj] == c:
                    seen.add((ni,nj))
                    q.append((''.join([letters, c]), ni, nj, seen))
    return False


def word_score(word):
    if len(word) <= 4: return 1
    elif len(word) == 5: return 2
    elif len(word) == 6: return 3
    elif len(word) == 7: return 5
    else: return 11


dictionary = defaultdict(list)
w = int(input())
for i in range(w):
    word = str(input())
    dictionary[word[0]].append(word)
newline = input()
n = int(input())
for i in range(n):
    board = []
    for j in range(4):
        row = list(stdin.readline().rstrip())
        board.append(row)
    print(boggle(dictionary, board))
    # print(board)
    if i != n-1: newline = input()
# print(dictionary)

