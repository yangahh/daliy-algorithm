# def reverse(number):
#     # 여기에 코드를 작성해주세요.
#     str_number = str(number)
#     result = []
#     if number >= 0:
#         for i in range(len(str_number) - 1, -1, -1):
#             result.append(str_number[i])
#         result = "".join(result)
#         return int(result)

#     else:
#         for i in range(len(str_number)-1, 0, -1):
#             result.append(str_number[i])
#         result = "".join(result)
#         return int(result) * (-1)


def reverse(number):
    # 여기에 코드를 작성해주세요.
    str_number = str(number)
    list_number = [x for x in str_number]

    if number >= 0:
        list_number.reverse()
        result = "".join(list_number)
        return int(result)

    else:
        del list_number[0]
        # list_number = list_number[1:]
        list_number.reverse()
        result = "".join(list_number)
    return int(result) * (-1)


print(reverse(3200))


# def reverse(number):
#   # str version
#   check = str(number)[::-1]
#   if check[0] == 0:
#     check = check[1:]
#   if check[-1] == '-':
#     check = int(check[:len(check) - 1]) * -1

#   return int(check)
#   # int version
#   check = abs(number)
#   result = 0
#   while check > 0:
#     result = (result * 10) + (check % 10)
#     check = check // 10

#   return result * -1 if number < 0 else result


def reverse2(number):
  # str version
  check = str(number)[::-1]
  if check[0] == 0:
    check = check[1:]
  if check[-1] == '-':
    check = int(check[:len(check) - 1]) * -1
  
  return int(check)
  
def reverse3(number):  
  # int version
  check = abs(number)
  result = 0
  while check > 0:
    result = (result * 10) + (check % 10)
    check = check // 10
  
  return result * -1 if number < 0 else result
