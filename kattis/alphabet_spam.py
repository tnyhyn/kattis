spam = str(input())
ws, lc, uc, sym, size = 0, 0, 0, 0, len(spam)
for i in spam:
    if i == '_': ws += 1
    elif i.islower(): lc += 1
    elif i.isupper(): uc += 1
    else: sym += 1
print(ws/size)
print(lc/size)
print(uc/size)
print(sym/size)