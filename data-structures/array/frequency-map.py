"""
Find frequency of array elements.

Alternative to frequency array.
This method can be used with both numbers and chars without any change since there is no logic in mapping.

Benefit of freq array is that keys are sorted. In map, manually sort keys and then iterate over keys.

"""

# Suppose max value in array can be 10
arr = [1, 2, 4, 3, 8, 4, 2, 0, 0, 7, 7, 3, 0]

# Create empty map
count = {}

# Iterate
for value in arr:
    if value not in count:
        count[value] = 0

    count[value] += 1

# Output
for key, value in count.items():
    print(key, "is present", value, "times")
