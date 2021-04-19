def same_reverse(num):
    num_list = [s for s in str(num)]
    return num_list == num_list[::-1]
