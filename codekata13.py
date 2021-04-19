'''
## 문제
양수로 이루어진 m x n 그리드를 인자로 드립니다.
상단 왼쪽에서 시작하여, 하단 오른쪽까지 가는 길의 요소를 다 더했을 때,가장 작은 합을 찾아서 return 해주세요.

한 지점에서 우측이나 아래로만 이동할 수 있습니다.

Input:
[
&nbsp;&nbsp;  [1,3,1],
&nbsp;&nbsp;  [1,5,1],
&nbsp;&nbsp;  [4,2,1],
]

Output: 7

설명: 1→3→1→1→1 의 합이 제일 작음
'''

# dynamic + greedy 유형


def min_path_sum(grid):
    n = len(grid)
    m = len(grid[0])

    # 다음 칸으로 갈 떼 이전 까지의 합을 가지고 있어야 함(grid 에)

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            elif i == 0:  # 가장 위쪽 라인의 최소 합은 우측으로만 쭉 왔을 때 값
                grid[i][j] += grid[i][j-1]
            elif j == 0:  # 가장 왼쪽 라인의 최소 합은 아래쪽으로만 쭉 왔을 때 값
                grid[i][j] += grid[i-1][j]
            else:  # 나머지의 경우, 내 기준 왼쪽/위쪽 중 값이 작은 값에서 해당 죄표의 값을 더한 값이 최소값
                grid[i][j] += min(grid[i][j-1], grid[i-1][j])

    return grid[n-1][m-1]


print(min_path_sum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1],
]))
