'''
## 문제
주어진 숫자 배열에서, 0을 배열의 마지막쪽으로 이동시켜주세요.
원래 있던 숫자의 순서는 바꾸지 말아주세요.

* 새로운 배열을 생성해서는 안 됩니다.

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''


def move_zeroes(nums):
    i = 0
    for _ in range(len(nums)):  # 리스트 길이만큼만 반복
        if nums[i] == 0:
            nums.pop(i)  # 인덱스 i번째 원소 삭제
            print(nums)
            nums.append(0)
            print(nums)
            i -= 1
        i += 1

    return nums


print(move_zeroes([0, 0, 9, 0, 12]))
