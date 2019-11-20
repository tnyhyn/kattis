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
                        if word in used: continue
                        else: used.add(word)
                        words += 1
                        if len(word) >= len(longest_word):
                            lexico = word
                            longest_word = word
                            if lexico < longest_word:
                                longest_word = lexico
                        ws = word_score(word)
                        # print("word: {} | score: {}".format(word, ws))
                        score += ws
    print(score, longest_word, words)


def word_exists(A, i, j, word):
    directions = [(-1,0), (0,1), (1,0), (0,-1), (-1,-1), (-1,1), (1,1), (1,-1)]
    q = deque()
    initial_set = set()
    initial_set.add((i,j))
    q.append((word[0], word[1:], i, j, initial_set))
    # print("word: {}".format(word))
    while q:
        letters, rest, i, j, seen_before = q.popleft()
        if letters == word: 
            # print("found", letters)
            return True
        for d in directions:
            ni, nj = i+d[0], j+d[1]
            if ni < 0 or ni >= len(A) or nj < 0 or nj >= len(A[0]):
                continue
            # print("A: {} | words: {} | letters: {} | seen_before: {}".format(A[ni][nj],word,letters,seen_before))
            # # print("seen_before: {}".format(seen_before))
            if (ni, nj) in seen_before: continue
            if A[ni][nj] == rest[0]:
                # print("letters:",letters,"appended")
                seen = seen_before.copy()
                seen.add((ni,nj))
                q.append((''.join([letters, rest[0]]), rest[1:], ni, nj, seen))
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
    (boggle(dictionary, board))
    # print(board)
    if i != n-1: newline = input()
# print(dictionary)

