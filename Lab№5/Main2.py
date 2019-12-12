import random
def main():
    N = 500
    M = 500
    a = []
    new = []
    for i in range (N):
        for j in range (M):
            new.append(random.randint(0, 10))
        a.append(new)
        new = []
    print(a)


if __name__ == '__main__':
    main()
