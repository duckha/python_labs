import random
def makeArrays(N, M): # width and height of array
    a = [[random.randint(0, 10) for j in range(M)] for i in range(N)] # generator of array
    return a # return array


if __name__ == '__main__':
    makeArrays(100, 100) # make an array
