num = int(input())
for i in range(1, num + 1):
    square = lambda i: i * i
    print(i,':',square(i), end=', ')
