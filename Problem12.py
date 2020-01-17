def is_even(i):
    return i % 2 == 0


def every_digit_even(num):
    while num != 0:
        rem = num % 10
        if is_even(rem):
            pass
        else:
            return False
        num //= 10
    return True


Lst = []
for i in range(2000,3001):
    if every_digit_even(i):
        Lst.append(i)
    else:
        pass
for j in Lst:
    print(j, end=', ')