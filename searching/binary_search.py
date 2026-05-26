arr = [1, 2, 3, 4, 5]
target = 4
low = 0
high = len(arr) - 1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        print("Found")
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
