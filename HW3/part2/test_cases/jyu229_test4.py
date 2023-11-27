for i in range(2, 5):
    for j in range(3, 6):
        a[i + j] = a[i * j % 3]