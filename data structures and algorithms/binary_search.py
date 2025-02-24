# Binary search ir a faster serching algorithm for sorted
# arrays by repeatedly dividing the search interval in half.

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage

arr = list(range(59))

print(arr)

target = 18

print(binary_search(arr, target))
