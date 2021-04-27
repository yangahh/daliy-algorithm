def reverse_string(s) :
    s.reverse()
    return s

def reverse_string2(s):
    return list(reversed(s))

'''
# reverse
- list의 자료형 함. 즉, list 타입에서 제공하는 함수
- string 타입에서는 사용하지 못함(오직 list타입에서만 사용 가능)
- list 요소를 역순으로 정렬해준다.
- 원본을 변경한다
- 시간 복잡도는 O(n)

# reversed
- 파이썬 내장 함수. 즉, list에서 제공해주는 함수가 아니다.
- 순서가 있는 데이터 자료형을 인자로 받는. list, tuple, string 타입에서 사용 가능
- iterator의 요소를 역순으로 리턴
- 원본을 변경하지는 않는다.
- 시간 복잡도는 O(1)
'''



