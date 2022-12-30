if __name__ == '__main__':
    n = int(input())
    assert n>=0
    num=[print(x**2) for x in range(n)]
    print(num)