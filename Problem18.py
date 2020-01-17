upper = 0
lower = 0
special = 0
num = 0
Lst = []
for i in range(3):
    temp = input()
    for j in range(len(temp)):
        n = ord(temp[j])
        if 65 <= n < 97:
            upper += 1
        elif 97 <= n <= 122:
            lower += 1
        elif 48 <= n <= 57:
            num += 1
        elif n == ord('#') or n == ord('@') or n == ord('$'):
            special += 1
    if upper >= 1 and lower >= 1 and special >= 1 and num >= 1 and 6 <= len(temp) <= 12:
        Lst.append([temp, "Accepted"])
    else:
        Lst.append([temp, "Rejected"])
print(Lst)