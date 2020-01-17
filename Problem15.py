def expression(s, key):
    sum = 0
    temp = 1
    for i in range(len(s)):
        if s[i] != '+':
            temp *= key
        else:
            sum += temp
            temp = 1
    sum += temp
    print(sum)


exp = input()
expression(exp, 9)
