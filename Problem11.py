def convert_decimal(num):
    rem = 0
    s = 0
    i = 0
    while num != 0:
        rem = num % 10
        s = s + (rem * 2**i)
        i += 1
        num //= 10
    return s


Lst = []
for i in range(4):
    temp = int(input())
    num = convert_decimal(temp)
    if num % 5 == 0:
        Lst.append(temp)
for j in Lst:
    print(j,end=', ')
#0100,0011,1010,1001