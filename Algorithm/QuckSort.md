# Quick Sort(퀵 정렬)




* 피벗(pivot)을 기준으로 작은 값들은 왼쪽에, 큰 값들은 오른쪽에 정렬하여 재귀적으로 반복한다.
```py

def quick_sort(arr):
    if len(arr) <= 1:       # 단일 항
        return arr

    # 기준을 잡는다, 여기서는 가운데 값을 잡았으나 제일 왼쪽이나 오른쪽으로 두어도 충분하다.
    pivot = arr[len(arr) // 2]
    left_side, middle_side, right_side = [], [], []

    for num in arr:
        if num < pivot:
            left_side.append(num)
        elif num > pivot:
            right_side.append(num)
        else:
            middle_side.append(num)

    # 정렬된 왼쪽 부분 + pivot과 일치하는 가운데 부분 + 정렬된 오른쪽 부분
    return quick_sort(left_side) + middle_side + quick_sort(right_side)

```