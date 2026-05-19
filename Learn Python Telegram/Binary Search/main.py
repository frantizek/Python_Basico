"""
Binary search is a search algorithm used to find the position of a target value within a sorted array. 

It works by repeatedly dividing the search interval in half. At each step, it compares the target value with the middle element of the array. 

If the target value matches the middle element, the position is returned. If the target value is less than the middle element, the search continues on the lower half of the array. If the target value is greater, the search continues on the upper half. 

This process continues until the target value is found or the search interval is empty. Binary search is efficient and has a time complexity of O(log n), where n is the number of elements in the array.
"""

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if the target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore the right half
        else:
            right = mid - 1

    # Target was not found in the array
    return -1

# Example usage
if __name__ == "__main__": 
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target_value = 5

    result = binary_search(sorted_array, target_value)

    if result != -1:
        print(f"Element {target_value} is present at index {result}.")
    else:
        print(f"Element {target_value} is not present in the array.")