if __name__ == '__main__':
    x = 10
    y = 20
    j = x + y
    j = x + y
    sum = 0
    a = []
    a = [0] * 10
    a[1] = 1
    b = []
    b = [0] * 10
    sum = addNumbers(x, y)
    if sum > 20:
        print(['"Sum is greater than 20. sum = "'], ['sum'], ['endl'])

    else:
        print(['"Sum is less than or equal to 20.  sum = "'], ['sum'], ['endl'])

    print(['"For loop: "'])
    for i in range(0, 5, 1):
        print(['i'], ['" "'])

    print(['endl'])
    print(['"While loop: "'])
    j = 5
    while j >= 0:
        print(['j'], ['" "'])
        j -= 1

    print(['endl'])

def addNumbers(a, b):
    return a + b

