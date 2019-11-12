# Lab 8

#1. 
from random import randrange

tosses = [randrange(1,6) for _ in range(20)]
print(tosses)
def q1(values):
    inRun = False
    for i in range(len(values)):
        if i != 0 and inRun and values[i] != values[i-1]:
            print(')', end=" ")
            inRun = False
        if not inRun and i != len(values)-1 and values[i] == values[i+1]:
            print('(', end=" ")
            inRun = True
        print(values[i], end=" ")
    if inRun: print(')', end=" ")
q1(tosses)


#2.
def q2(values):
    current, longest, left, right = 1, 0, 0, 0
    for i in range(1, len(values)):
        if values[i] == values[i-1]:
            current += 1
            if current > longest:
                right = i
                left = i - current
                longest = current
        else:
            current = 1
    left += 1
    right += 1
    for i in range(len(values)):
        if i == left: print('(', end=" ")
        elif i == right: print(')', end=" ")
        print(values[i], end=" ")
print(" ")
q2(tosses)


#3.
boo = [False, False, True, False, False, False, False, True, True, False, False]
def q3(values):
    current, longest, left, right = 1, 0, 0, 0
    for i in range(1, len(values)):
        if values[i] == values[i-1]:
            current += 1
            if current > longest:
                right = i
                left = i - current
                longest = current
        else:
            current = 1
    left += 1
    return ((left, right))
print(" ")
print(q3(boo))


#4.
def q3helper(arr):
    current, longest, left, right = 1, 0, 0, 0
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1] and arr[i] == '_':
            current += 1
            if current > longest:
                right = i
                left = i - current
                longest = current
        else:
            current = 1
    left += 1
    return ((left, right))

def q4(size):
    nest = ['_' for _ in range(size)]
    while '_' in nest:
        l, r = q3helper(nest)
        mid = (l + r) // 2
        nest[mid] = 'X'
        print(nest)
        if l > r: break
    for i in range(size):
        if nest[i] == '_':
            nest[i] = 'X'
            print(nest)
q4(10)

#5.
def isPal(L):
    if L == L[::-1]: return True
    return False
