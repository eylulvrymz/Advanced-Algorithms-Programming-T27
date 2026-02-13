"""Approach 1"""
def rotateWtemp(Vect, k):
    n = len(Vect)
    k = k % n  # Get rid of k values bigger than n
    temp_arr = Vect.copy() # A copy of Vect

    for i in range(n):
        new_index = (i + k) % n
        Vect[new_index] = temp_arr[i]

# Complexity is O(n) for both time and memory

"""Approach 2"""
def rotate1by1(Vect, k):
    n = len(Vect)
    k = k % n

    # Repeat k times
    for _ in range(k):
        last_element = Vect[n-1]
        
        # For j from n-1 to 1 backwards
        for j in range(n - 1, 0, -1):
            Vect[j] = Vect[j-1]
            
        Vect[0] = last_element

# Complexity: Time O(n*k), Memory O(1)

"""Approach 3"""
def reverse(Vect, first, last):
    while first < last:
        # Swap Vect[first] and Vect[last]
        Vect[first], Vect[last] = Vect[last], Vect[first]
        first = first + 1
        last = last - 1

def rotateOptimal(Vect, k):
    n = len(Vect)
    k = k % n

    reverse(Vect, 0, n-1)     # 1. Reverse all of the array
    reverse(Vect, 0, k-1)     # 2. Reverse the first k elements within themselves
    reverse(Vect, k, n-1)     # 3. Reverse the rest within themselves

# Complexity: Time O(n), Memory O(1)