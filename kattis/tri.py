from sys import stdin


def tri(i, j, k):
    if i + j == k: return('{}+{}={}'.format(i,j,k))
    if i == j + k: return('{}={}+{}'.format(i,j,k))
    if i - j == k: return('{}-{}={}'.format(i,j,k))
    if i == j - k: return('{}={}-{}'.format(i,j,k))
    if i * j == k: return('{}*{}={}'.format(i,j,k))
    if i == j * k: return('{}={}*{}'.format(i,j,k))
    if i / j == k: return('{}/{}={}'.format(i,j,k))
    if i == j / k: return('{}={}/{}'.format(i,j,k))


i, j, k = stdin.readline().split()
print(tri(int(i), int(j), int(k)))

