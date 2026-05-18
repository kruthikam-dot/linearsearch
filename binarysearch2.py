def binary_search(marks, target):
    low, high = 0, len(marks) - 1

    while low <= high:
        mid = (low + high) // 2
        if marks[mid] == target:
            return mid
        elif marks[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

marks= [35,42,50,61,78,85,90]
target = 78

result = binary_search(marks, target)
print(result)