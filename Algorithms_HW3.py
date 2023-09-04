# Task 1 ************************
def find_two_lowest(arr: list):
    if len(arr) < 2:
        return "List should have at least two elements"

    sorted_arr = sorted(arr)
    lowest_elements = [sorted_arr[0], sorted_arr[1]]
    return lowest_elements


my_list = [198, 3, 4, 9, 10, 9, 2]
result = find_two_lowest(my_list)
print(result)  # Output will be [2, 3]

# Task 2 ************************
def invert_list(arr: list):
    inverted_arr = []  # Initialize an empty list to store the inverted numbers

    for num in arr:
        inverted_num = -num  # Change the sign of the current number
        inverted_arr.append(inverted_num)  # Add the inverted number to the new list

    return inverted_arr


my_list = [1, 5, -2, 4]
result = invert_list(my_list)
print(result)  # Output will be [-1, -5, 2, -4]

# Task 3 ************************

def max_diff(arr: list):
    # Check if the list is empty
    # If it is, return 0 as there's no difference to be calculated
    if len(arr) == 0:
        return 0

    # Sort the list in ascending order
    # After sorting, the smallest element will be at index 0,
    # and the largest will be at the last index
    arr.sort()

    # Calculate and return the difference between the largest and smallest elements
    # Use indexes of the elements
    largest = arr[-1]
    smallest = arr[0]
    difference = largest - smallest

    return difference

# Example usage:
my_list = [3, 5, 7, 2]
result = max_diff(my_list)
print(result)  # Output will be 3 (5 - 2)

# Task 4 ************************
def count_larger_neighbors(arr: list):
    # Initialize a variable 'count' to 0. This variable will keep track of the number of elements
    # that are larger than both their adjacent neighbors.
    count = 0

    # Loop through the list from index 1 to len(arr) - 2. We skip the first and the last elements
    # because they don't have both left and right neighbors.
    for i in range(1, len(arr) - 1):
        # Check if the current element (arr[i]) is greater than its left neighbor (arr[i - 1])
        # and its right neighbor (arr[i + 1]).
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            # If the condition is met, increment the 'count' variable by 1.
            count += 1

    # Return the final count of elements that are larger than both their neighbors.
    return count

# Example usage:
my_list = [2, 56, 7, 21, 22, 19, 26]
result = count_larger_neighbors(my_list)
print(result)  # Output will be 3 (56, 22)

# Task 5 ************************

def subtract_min(arr: list):
    # Find the minimum element in the list using the 'min' function and store it in 'min_element'.
    min_element = min(arr)

    # Subtract the 'min_element' from each element in the array.
    result = [element - min_element for element in arr]

    return result

# Example usage:
my_list = [9, 2, 5, 4, 7, 6, 1]
result = subtract_min(my_list)
print(result)  # Output will be [8, 1, 4, 3, 6, 5, 0]

