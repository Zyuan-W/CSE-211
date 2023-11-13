a = input()
b = input()
c = input()
if a:
    a = b
else:
    if b:
        c = a
    else:
        b = input()
    a = c
d = input()
while d:
    e = input()
    if e:
        d = e
    else:
        if a:
            e = d
        else:
            d = input()
        a = e
    f = a
g = f
h = g