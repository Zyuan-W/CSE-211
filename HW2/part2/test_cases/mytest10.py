x = input()
y = input()

if x:
    y = x
else:
    x = input()
    if x:
        z = y
    else:
        y = input()

while x:
    a = input()
    if a:
        b = a
        if b:
            x = b
        else:
            a = input()
            if a:
                b = x
            else:
                x = y
    else:
        x = input()
        if x:
            c = b
        else:
            b = c
    d = c
    if d:
        e = d
    else:
        c = input()
        if c:
            d = e
        else:
            e = d

f = e
g = input()
while g:
    h = input()
    if h:
        g = f
    else:
        f = g
    i = f
    if i:
        j = g
    else:
        g = h

k = j
l = input()
if l:
    m = k
else:
    k = l

n = m
o = n
p = o