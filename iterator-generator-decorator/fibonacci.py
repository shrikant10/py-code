
def fibonacci():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':

    print('Print N fibonacci Series: ')

    series = fibonacci()

    for _ in range(10):
        print(next(series))
