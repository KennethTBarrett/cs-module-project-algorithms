'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

# Create two empty lists to populate
# Iterate through each entry in our input array.
    # If the entry isn't already in our first list to populate, add it.
    # Otherwise, if it is, append it to our second list.

# Now, iterate through each entry in our first list.
    # Check if that entry is in our second list.
    # If it isn't, our that's our number to return.

# This would be a O(n) time complexity because when we speak of time complexity,
# we're talking relevant, not absolute, and our for loops are not nested within
# one another.

def single_number(arr):

    list1, list2 = [], []

    for entry in arr:
        if entry not in list1:
            list1.append(entry)
        else:
            list2.append(entry)

    for entry in list1:
        if entry not in list2:
            return entry
    return -1

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")