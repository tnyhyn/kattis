from sys import stdin


def evaluate_rolls(s, r):
    s.sort(reverse=True)
    r.sort(reverse=True)
    if s == r: return "Tie."
    if s == [2,1]: return "Player 1 wins."
    elif r == [2,1]: return "Player 2 wins."
    if s[0] == s[1] and r[0] == r[1]:
        if s > r: return "Player 1 wins."
        else: return "Player 2 wins."
    if s[0] == s[1]: return "Player 1 wins."
    if r[0] == r[1]: return "Player 2 wins."
    if s > r: return "Player 1 wins."
    else: return "Player 2 wins."



while True:
    n = [int(i) for i in stdin.readline().split()]
    if n == [0,0,0,0]: break
    s = [n[0], n[1]]
    r = [n[2], n[3]]
    print(evaluate_rolls(s, r))
