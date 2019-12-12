import hashlib
def main():
    dict = {"dog" : 1, "horse" : 2, "cat" : 4, "cow" : 5, "tiger" : 6}
    x = input("Enter the secret word: ")
    hash_result = hashlib.md5(x.encode())
    print("Number of map: ", dict[x], "; encode word: ", hash_result.hexdigest())

if __name__ == '__main__':
    main()
