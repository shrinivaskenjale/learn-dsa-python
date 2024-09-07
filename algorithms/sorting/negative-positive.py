"""
Separate negative and positive numbers while maintaining relative order between all negative and all positive numbers.

Input = [8,-4,3,-3,-9,-5,2,4]
Output = [-4,-3,-9,-5,8,3,2,4]
"""


def separate(array, low, high):
    if low >= high:
        return

    mid = low + (high - low) // 2

    separate(array, low, mid)
    separate(array, mid + 1, high)
    merge(array, low, mid, high)


def merge(array, low, mid, high):
    low


array = [8, -4, 3, -3, -9, -5, 2, 4]
# separate(array)
ans = []
for item in array:
    if item < 0:
        ans.append(item)

for item in array:
    if item > 0:
        ans.append(item)
print(ans)
