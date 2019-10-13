def secret(message):
    encryted_message = ''
    M = 1
    while M**2 < len(message):
        M += 1
        if M ** 2 >= len(message):
            M = M ** 2
    message = message + '*' * (M - len(message))
    K, matrix = int(M ** (1/2)), []
    for i in range(len(message) + 1):
        if i % K == 0:
            matrix.append(list(message[i - K: i]))
    matrix = matrix[1:]
    for i in range(K):
        for j in range(i, K):
            matrix[i][j],  matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(K):
        matrix[i] = list(reversed(matrix[i]))
    for i in matrix:
        for j in i:
            if j is not '*':
                encryted_message += j
    print(encryted_message)    


t = int(input())
for i in range(1, t + 1):
    message = input()
    secret(message)