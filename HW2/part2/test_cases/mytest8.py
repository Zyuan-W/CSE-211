a = input()
b = input()

if b:
    a = b
else:
    while a:
        c = input()
        if c:
            a = c
        else:
            a = input()
    d = a

while b:
    if a:
        e = b
        b = a
    else:
        b = input()
    e = d
f = e