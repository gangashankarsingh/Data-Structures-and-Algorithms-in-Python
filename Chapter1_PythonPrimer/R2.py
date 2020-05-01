def is_even(k):
    return True if k[-1] in ['0','2','4','6','8'] else False


if __name__ == '__main__':
    x= input("Enter a number to check if its even ")
    print(is_even(x))