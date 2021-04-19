def get_len_of_str(s):
  count = 0
  answer_list = []
  for a in s:
    if a not in answer_list:
      answer_list.append(a)
    else:
      count = max(count, len(answer_list))
      answer_list = [a]
  answer = max(count,len(answer_list))
  return answer

