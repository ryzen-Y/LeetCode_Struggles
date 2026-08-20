# arr = [7, 1, 2, 5, 8, 4, 9, 3, 6]
# n = len(arr)
# k = 3
# max_sum = 0


# for i in range(0, n-k+1):
#     sum = 0
#     for j in range(i, i+k):
#         sum += arr[j]
#     max_sum = max(max_sum, sum)

# print(max_sum)


####


# arr = [7, 1, 2, 5, 8, 4, 9, 3, 6]
# n = len(arr)
# k = 3
# max_sum = 0
# index = 0

# for i in range(0, n-k+1):
#     sum = 0
#     for j in range(i, i+k):
#         sum += arr[j]
#     if max_sum < sum:
#         max_sum = sum
#         index = i

# print(max_sum, index)


# IMPLEMENTING SLIDING WINDOW #

arr = [7, 1, 2, 5, 8, 4, 9, 3, 6]
n = len(arr)
k = 3
i = 1
j = k

pre_sum = 0
for _ in range(k):
    pre_sum += arr[_]


index = 0
max_sum = pre_sum


while j < n:
    pre_sum = pre_sum + arr[j] - arr[i-1]
    if pre_sum > max_sum:
        max_sum = pre_sum
        index = i
    pre_sum = pre_sum
    i += 1
    j += 1

print(max_sum, index)
