'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache):
    if n < 0:  # If n is less than 0
        return 0  # Return 0
    if n == 0:  # If n is 0
        return 1  # Return 1
    
    # Does the cache have the answer the branch is looking for?
    elif n in cache:
        return cache[n]
    else:  # Otherwise, it's not, so compute answer "normal" way.
        # Once completed, we're gonna store it in our cache.
        cache[n] = (eating_cookies(n-1, cache)
        + eating_cookies(n-2, cache) +
        eating_cookies(n-3, cache))
        return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 100

    print(f"There are {eating_cookies(num_cookies, {})} ways for Cookie Monster to eat {num_cookies} cookies")
