def get_all_prev_squares(val):
    sum = 0
    for i in range(val):
        sum += i**2
    return sum

if __name__ == '__main__':
    val = int(input("Enter a value until which you need the square"))
    print(get_all_prev_squares(val))