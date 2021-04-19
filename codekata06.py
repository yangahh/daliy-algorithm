def roman_to_num(s):
    # d = {
    #     'I': 1,
    #     'V': 5,
    #     'X': 10,
    #     'L': 50,
    #     'C': 100,
    #     'D': 500,
    #     'M': 1000,
    # }
    # list_k = list(d.keys())
    # list_v = list(d.values())
    total = 0

    # for i in range(len(s)):
    #     if i == 0:
    #         total += d[s[i]]
    #     elif i > 0:
    #         if s[i] == 'V'

    for i in range(len(s)):
        if s[i] == 'I':
            total += 1
        elif s[i] == 'V':
            if i != 0 and s[i - 1] == 'I':
                total += 3
            else:
                total += 5
        elif s[i] == 'X':
            if i != 0 and s[i - 1] == 'I':
                total += 8
            else:
                total += 10
        elif s[i] == 'L':
            if i != 0 and s[i - 1] == 'X':
                total += 30
            else:
                total += 50
        elif s[i] == 'C':
            if i != 0 and s[i - 1] == 'X':
                total += 80
            else:
                total += 100
        elif s[i] == 'D':
            if i != 0 and s[i - 1] == 'C':
                total += 300
            else:
                total += 500
        else:
            if i != 0 and s[i - 1] == 'C':
                total += 800
            else:
                total += 1000

    return total


print(roman_to_num('CD'))
