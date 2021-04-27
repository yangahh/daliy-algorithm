def min_path_sum(grid):
    n = len(grid)
    m = len(grid[0])

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
