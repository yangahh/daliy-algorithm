def same_reverse(num):
    num_list = [s for s in str(num)]
    return num_list == num_list[::-1]

# solution2 (21.04.23)
def same_reverse(num):
  return str(num) == str(num)[::-1]
