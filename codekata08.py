def is_valid(string):

    if(len(string)) % 2 != 0 or len(string) == 0:
        return False

    dic = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    cnt = 0
    for s in string:
        if s in dic.values():
            cnt += 1
    if cnt == 0:
        return False

    open_in = []
    for s in string:
        print(s)
        print(open_in)
        if s in dic.values():  # 여는 괄호면
            open_in.append(s)
        else:  # 닫는 괄호면
            if dic[s] in open_in:
                open_in.pop()
        print()
    print(open_in)

    if open_in:
        return False
    return True


print(is_valid(']]'))
