for i in range(3, 50):
    for j in range(i, 60):
        for k in range(j, 70):
            for l in range(k, 80):
                for m in range(l, 90):
                    for n in range(m, 100):
                        for o in range(n, 110):
                            for p in range(o, 120):
                                a[i * j + k - l] = a[m + n * o - p]
