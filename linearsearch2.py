def linearsearch(str, target):
    for i in range(len(str)):
        if str[i] == target:
            return i
    return -1
str = ['rice','sugar','milk','oil','soap']
target = 'milk'
result = linearsearch(str, target)
if result != -1:
    print(f"element found at index {result}")
else:
    print("element not found")