**T27 Team Members:**

Elenie Girma WAKJIRA

Eylül Safiye VARYEMEZ

Yan SHEN

**Assigned Questions:**

Eylül Safiye Varyemez: Questions 4 & 5

**Q4** Normally when we are calculating the result of a polinom, computer constantly tries to take the square or cube of numbers. That's unnecessaryly tiring so we used a different approach. Using the Horner Method, we enclosed the polynomial in nested parentheses. We forbid the power method so the efficiency increased and we got our results much faster. The coden starts with the coefficient at the very end of the list (the highest ranking). At each step, it multiplies the current result by x, adds the next coefficient, and works its way back. Naive approach (calculating each term separately?) would be O(n^2), what we did is O(n) (better).

**Q5** We want to rotate the array we have by k. We used 3 approaches. In first one, we copied but this method uses memory. The code creates a backup of the array and places the elements one by one into their new positions. Complexity is O(n) for both time and memory. In the second one we rotated one by one, this method takes too much time. The code shifts the array one step to the right each time and repeats this k times. Complexity: Time O(n*k), Memory O(1). In the third approach, we used a more efficient method by reversing the array. The code inverts the array completely first, then in parts, bringing the elements to their correct positions without using any extra space. Complexity: Time O(n), Memory O(1).

Elenie Girma Wakjira: Questions 2 & 3
In Exercise 2 we try to check if a given string of brackets is balanced. The stack helps us to track the number of brackets that have been opened. Once we encounter a closed bracket we push one open bracket out and compare the two. If they are of the same types we move on to the rest otherwise the string is not balanced so we return False. For time and space complexity, the time complexity is O(n) because the loop goes from the first character of the string to the last only one time. Space complexity is also O(n) because even in the worst case scenario the stack would have to hold space for all n brackets.

In Exercise 3 we try to arrange a list of intervals by merging the ones that overlap with each other. For efficiency we first sort them out in order and then loop through each interval comparing the start of the current interval with the end of the last merged one to see if they should be combined. If an overlap is found, the end time is updated to the maximum value to cover the full range; otherwise, the interval is added as a new entry. In terms of complexity, the time complexity is O(n logn) as the sorting makes the system slower than the loop. For space complexity it is O(n) since we would need space for a new list and worst case would be the list itself. 
