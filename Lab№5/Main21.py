import random
def main():
    N = 500
    M = 500
    a = [[random.randint(0, 10) for j in range(M)] for i in range(N)]
        
    print(a)


if __name__ == '__main__':
    main()
