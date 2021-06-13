
def print_fabonacci(num):

    a, b = 0, 1
    while a < num:
        print(a, end=' ')
        a, b = b, a+b
    # print()


if __name__ == '__main__':
    print_fabonacci(660)

