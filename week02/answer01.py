## solution1
#def roman_to_num(s):
#    total = 0
#
#    for i in range(len(s)):
#        if s[i] == 'I':
#            total += 1
#        elif s[i] == 'V':
#            if i != 0 and s[i - 1] == 'I':
#                total += 3
#            else:
#                total += 5
#        elif s[i] == 'X':
#            if i != 0 and s[i - 1] == 'I':
#                total += 8
#            else:
#                total += 10
#        elif s[i] == 'L':
#            if i != 0 and s[i - 1] == 'X':
#                total += 30
#            else:
#                total += 50
#        elif s[i] == 'C':
#            if i != 0 and s[i - 1] == 'X':
#                total += 80
#            else:
#                total += 100
#        elif s[i] == 'D':
#            if i != 0 and s[i - 1] == 'C':
#                total += 300
#            else:
#                total += 500
#        else:
#            if i != 0 and s[i - 1] == 'C':
#                total += 800
#            else:
#                total += 1000
#
#    return total

# solution2 (21.04.25)
def roman_to_num(s):
    symbol = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
  
    for i in range(len(s)):
        if i == len(s)-1:
            result += symbol[s[i]]
        elif (symbol[s[i]] * 5 == symbol[s[i+1]]) or (symbol[s[i]] * 10 == symbol[s[i+1]]):
            result -= symbol[s[i]]
        else:
            result += symbol[s[i]]

    return result
      
