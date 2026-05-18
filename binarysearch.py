def binary_search(emp_id, target):
    low, high = 0, len(emp_id) - 1

    while low <= high:
        mid = (low + high) // 2
        if emp_id[mid] == target:
            return mid
        elif emp_id[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

emp_id = [1001,1005,1010,1015,1020,1025]
target = 1015

result = binary_search(emp_id, target)
print(result)