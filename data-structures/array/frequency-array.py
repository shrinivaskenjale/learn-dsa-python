"""
Find frequency of array elements.

Using frequency array technique, we map values in given index to index of frequency array.

1. Create array of size greater than or equal to maximum index that can be mapped to value in original array. Fill frequency array with 0s.

2. Iterate over original array and for each value increment value in frequency array at index that corresponds to current value in original array.

"""

# Suppose max value in array can be 10
arr = [1, 2, 4, 3, 8, 4, 2, 0, 0, 7, 7, 3, 0]

# We will map the value in the array to index of freq array
# Create frequency array of size 10+1
freq = [0] * 11

# Iterate
for value in arr:
    freq[value] += 1

# Output
for index, value in enumerate(freq):
    if value != 0:
        print(index, "is present", value, "times")


# For characters, you can map characters using unicode.

# Freq array can be used to check if there are duplicate items in array.
