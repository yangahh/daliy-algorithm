def is_valid(s):
    if len(s) % 2 == 1:
        return False
  
    bracket = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    cnt = 0
    for x in s:
        if x in bracket.values():
            cnt += 1
    
    if cnt == 0:
        return False

    open_bracket = []
    for x in s:
        if x in bracket: # 닫는 괄호면
            if bracket[x] in open_bracket:
                open_bracket.pop()
        else: # 여는 괄호면
            open_bracket.append(x)

    return not bool(open_bracket)

def is_valid2(s):
    if len(s) == 0:
        return False

    bracket = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    open_bracket = []
    close_bracket = []

    for x in s:
        if x in bracket: # 닫는 괄호면
            close_bracket.append(x)

            if bracket[x] in open_bracket:
                open_bracket.pop()
                close_bracket.pop()
        else: # 여는 괄호면
            open_bracket.append(x)

    return not bool(open_bracket or close_bracket)

