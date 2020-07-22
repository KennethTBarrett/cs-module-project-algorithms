'''
Input: a List of integers
Returns: a List of integers
'''
# Define our starting index, as well as our last index.
# Confirm that our index is less than the length of our array. While it is...
    # If the index we specified as our starting index within our array is 0...
        # Ensure our index is less than the ending index. If it is...
            # We need to append the value, popped at the index.
            # We also need to take 1 off of the index and specified index.
        # If it's not...
        # Break
    # If the index we specified is NOT 0, we need to add 1 to our index to move up one.
def moving_zeroes(arr):
    i, end_i = 0, len(arr) - 1
    while i < len(arr):
        if arr[i] == 0:
            if i < end_i:
                arr.append(arr.pop(i))  # Pops the value and appends to the end.
                # This will change the index it's looking at by one,
                # as well as the index it stops looking at (end index).
                i -= 1
                end_i -= 1
            else:
                break
        i += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")