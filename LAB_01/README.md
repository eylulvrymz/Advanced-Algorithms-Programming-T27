**T27 Team Members:**

Elenie Girma WAKJIRA

Eylül Safiye VARYEMEZ

Yan SHEN

**Assigned Questions:**

Eylül Safiye Varyemez: Questions 4 & 5
**Q4** Normally when we are calculating the result of a polinom, computer constantly tries to take the square or cube of numbers. That's unnecessaryly tiring so we used a different approach. Using the Horner Method, we enclosed the polynomial in nested parentheses. We forbid the power method so the efficiency increased and we got our results much faster. The coden starts with the coefficient at the very end of the list (the highest ranking). At each step, it multiplies the current result by x, adds the next coefficient, and works its way back. Naive approach (calculating each term separately?) would be O(n^2), what we did is O(n) (better).

**Q5** We want to rotate the array we have by k. We used 3 approaches. In first one, we copied but this method uses memory. The code creates a backup of the array and places the elements one by one into their new positions. Complexity is O(n) for both time and memory. In the second one we rotated one by one, this method takes too much time. The code shifts the array one step to the right each time and repeats this k times. Complexity: Time O(n*k), Memory O(1). In the third approach, we used a more efficient method by reversing the array. The code inverts the array completely first, then in parts, bringing the elements to their correct positions without using any extra space. Complexity: Time O(n), Memory O(1).
Elenie Girma Wakjira: Questions 2 & 3
