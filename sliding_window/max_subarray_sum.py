arr = [1, 2, 3, 4, 5]
k = 3
max_sum = 0
for i in range(len(arr) - k + 1):
    current_sum = sum(arr[i:i+k])
    if current_sum > max_sum:
        max_sum = current_sum
print(max_sum)
