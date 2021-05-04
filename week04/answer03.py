# solution1
def groupAnagrams(strs):

    result = []  
    sorted_word = []

    for word in strs:
        if ''.join(sorted(word)) not in sorted_word:
            sorted_word.append(''.join(sorted(word)))
            result.append([word])
        else:
            i = sorted_word.index(''.join(sorted(word)))
            result[i].append(word)
    
    for group in result:
        group.sort()
    result.sort()

    return result


# solution2
def groupAnagrams2(strs):
    group = {}
    for word in strs:
        key = ''.join(sorted(word))
        if key not in group:
            group[key] = [word]
        else:
            group[key].append(word)
    
    return sorted([sorted(value) for value in group.values()])


# solution3
def groupAnagrams3(strs):
    group = {}
    for word in strs:
        key = tuple(sorted(word))  # 여기서 tuple을 하지 않으면 mutable하므로 dictionary의 key가 될 수 없음
        group[key] = group.get(key, []) + [word]

    return sorted([sorted(value) for value in group.values()])



#print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams(['apple','ppeal','star','arts','google','googel','tars','car']))
