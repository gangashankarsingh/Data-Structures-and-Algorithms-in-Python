def is_multiple(n,m):
    return True if n % m == 0 else False


if __name__ == '__main__':
    x,y = input("Enter value of n and m ").split(',')
    print(is_multiple(int(x),int(y)))