# def get_width(t_list, target):
#     find_index = list(filter(lambda x: t_list[x] == target, range(len(t_list))))
#     width = find_index[-1] - find_index[0]

#     return width

def get_max_area(height):
    max_value = 0
    for i in range(len(height)-1):
        for j in range(1, len(height)):
            a = height[i]
            b = height[j]
            # 둘 중 작은 높이를 height로 지정
            h = a if a <= b else b
            w = j - i
            water = h * w
            if water > max_value:
                max_value = water

    return max_value


print(get_max_area([35, 46, 43, 59, 59]))
