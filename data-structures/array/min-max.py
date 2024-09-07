# Function to get max value
def getMax(arr):
    maxValue = float("-inf")

    for item in arr:
        maxValue = max(item, maxValue)

    return maxValue


# Function to get min value
def getMin(arr):
    minValue = float("inf")

    for item in arr:
        minValue = min(item, minValue)

    return minValue


if __name__ == "__main__":
    arr = [53, 234, 45, 342, 6, 134, 75]
    print(f"Max value is {getMax(arr)}")
    print(f"Min value is {getMin(arr)}")


"""
Inbuilt min() and max() functions can take separate parameters or iterable.
min(1,2,3) => 1
min([1,2,3]) => 1
"""
