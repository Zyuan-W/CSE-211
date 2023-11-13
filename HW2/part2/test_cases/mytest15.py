x = input()
while x:
    y = input()
    if y:
        x = y
    else:
        z = input()
        if z:
            y = z
        else:
            y = input()
        x = y
    a = z
    while a:
        b = input()
        if b:
            a = b
        else:
            a = input()
    c = a
d = c