q = input()
r = input()
s = input()
t = input()
if q:
    u = q
else:
    v = input()
    if v:
        r = v
    else:
        q = input()
    u = q
while r:
    if s:
        t = s
        while t:
            r = input()
            if r:
                s = input()
            t = s
        u = r
    else:
        s = input()
        while s:
            w = input()
            if w:
                r = w
            else:
                s = input()
            u = s
        x = r
y = u
z = x