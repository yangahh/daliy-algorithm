#def get_max_area(height):
#    max_value = 0
#
#    for i in range(len(height)-1):
#        for j in range(1, len(height)):
#            a = height[i]
#            b = height[j]
#            # 둘 중 작은 높이를 height로 지정
#            h = a if a <= b else b
#            w = j - i
#            water = h * w
#            if water > max_value:
#                max_value = water
#
#    return max_value

# solution2 (21.04.25)
def get_max_area(height):
    area_list = []
    for i in range(len(height)-1):
        for j in range(i, len(height)):
            x = j - i
            y = min(height[i], height[j])
            area_list.append(x * y)

    return max(area_list)



# solution3 (21.04.25)
def get_max_area(height):
    max_area = 0
    for i in range(len(height)-1):
        for j in range(i, len(height)):
            x = j - i
            y = min(height[i], height[j])
            if x * y > max_area:
                max_area = x * y
    
    return max_area
