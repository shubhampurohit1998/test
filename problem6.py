import math
c = 50
h = 30
Lst = []
for i in range(3):
    d = int(input())
    q = math.sqrt((2*c*d)/h)
    Lst.append(math.floor(q))
for i in Lst:
    print(i)