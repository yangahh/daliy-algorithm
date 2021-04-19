def reverse_test(a):
    list_a = list(a)
    print(list_a)
    print(list_a.reverse()) # reverse()는 list에만 적용 가능
    print(''.join(list_a)) 

def reversed_test(a):
    print(''.join(reversed(a)))

def index_reverse(a):
    print(a[::-1])
    print(a[3:0:-1]) #인덱스 3부터 인덱스 0 전까지 (==인덱스 3부터 인덱스 1까지) 역순으로
    print(a[0:3:-1]) # 인덱스 0부터 인덱스 3전까지 >> 아무것도 출력되지 않음

reverse_test('asdf')
reversed_test('asdf')
index_reverse('abcdefgh')

