s = input()

if s:
    r = input()
    while r:
        if s:
            r = s
        else:
            s = input()
        t = r
else:
    q = input()
    if q:
        s = q
    else:
        r = s
p = r