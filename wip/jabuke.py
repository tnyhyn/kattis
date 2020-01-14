from sys import stdin
import math

a = [int(i) for i in stdin.readline().split()]
b = [int(i) for i in stdin.readline().split()]
c = [int(i) for i in stdin.readline().split()]
n = int(input())


def area(a,b,c):
    def calc(x, y1, y2):
        return x*(y1 - y2)
    return abs(calc(a[0],b[1],c[1])+calc(b[0],c[1],a[1])+calc(c[0],a[1],b[1]))/2

def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang
 
def inside_triangle(pt, a, b, c):
     k1 = getAngle(a,b,c)
     k2 = getAngle(b,c,a)
     k3 = getAngle(c,a,b)
     print(k1, k2, k3)

print(area(a,b,c))
count = 0
for i in range(n):
    pt = [int(i) for i in stdin.readline().split()]
    # count += inside_triangle(pt, a, b, c)
    inside_triangle(pt, a, b, c)
# print(count)


