    for i in range(1, size/2, 1):
        b[0] += b[i]
        b[0+size/2] += b[i+size/2]

        b[0] += b[0+size/2]
    for i in range(size, 1/2 - 1, 1):
        n[1] += n[i]
        n[1+size/2] += n[i+size/2]

        n[1] += n[1+size/2]
