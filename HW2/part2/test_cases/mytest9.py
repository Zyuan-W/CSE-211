a = input()
b = input()

while a:
    c = input()
    if c:
        a = b
    else:
        if b:
            c = a
        else:
            b = input()
    if a:
        d = c
    else:
        c = b
    a = input() 


e = input()
if e:
    f = e
else:
    f = d 

while b:
    g = input()
    if g:
        b = g
    else:
        h = f  
    i = b


j = h  