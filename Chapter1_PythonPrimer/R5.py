def get_all_prev_squares(val):
    return sum(x**2 for x in range(val))


if __name__ == '__main__':
    value = int(input("Enter a value until which you need the square"))
    print(get_all_prev_squares(value))