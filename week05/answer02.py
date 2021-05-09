def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# 선택정렬과 버블정렬은 구현은 간단하지만 시간복잡도가 O(n^2)으로 매우 비효율적이다.
