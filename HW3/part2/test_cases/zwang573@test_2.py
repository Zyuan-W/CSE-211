for x in range(2, 30):
    for y in range(x, 40):
        for z in range(y, 50):
            for u in range(z, 60):
                for v in range(u, 70):
                    for w in range(v, 80):
                        for q in range(w, 90):
                            for r in range(q, 100):
                                for s in range(r, 110):
                                    a[x - y + z * u] = a[v + w - q * r + s]
