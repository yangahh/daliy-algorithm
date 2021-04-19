# solution1
def reverse(number):
    str_number = str(number)
    list_number = [x for x in str_number]

    if number >= 0:
        list_number.reverse()
        result = "".join(list_number)
        return int(result)

    else:
        del list_number[0]
        list_number.reverse()
        result = "".join(list_number)
        return int(result) * (-1)

# reverse()는 list에만 적용 가능
# reverse()후 join으로 다시 string으로 변환해줘야 함

# solution2 (2021.04.19)
def reverse(num):
    str_num = str(num)
    if str_num[0] == '-':
        return int(str_num[:0:-1]) * (-1)
    return int(str_num[::-1])

# 인덱스 슬라이싱을 통해 역순 정렬 : [::-1]
# ex) list[3:0:-1] : 인덱스3부터 인덱스0 이전 까지(즉, 인덱스1까지) 역순 정렬
