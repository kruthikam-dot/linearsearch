def linearsearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
arr = [101, 102, 103, 104, 105]
target = 10
result = linearsearch(arr, target)
if result != -1:
    print(f"Number found at index {result}")
else:
    print("Number not found")