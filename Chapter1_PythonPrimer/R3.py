def get_min_max(list_val):
    min_val = max_val = list_val[0]
    for i in list_val:
        if i < min_val:
            min_val = i
        if i > max_val:
            max_val = i
    return min_val, max_val


if __name__ == '__main__':
    x, y = get_min_max([21, 11, 23, -1, -9999929, 3212, 19999999])
    print("Min and max are {} and {} respectively ".format(x, y))
