tup = ()
Lst = []
temp = input()
s = ''
for i in temp:
    if i == ',':
        Lst.append(s)
        tup = tup + (s ,)
        s = ''
        continue
    else:
        s = s+i
print(tup)
print(Lst)
   # ['34', '67', '55', '33', '12', '98']