# Advanced-Algorithms-Programming-T27

**LAB 4 REVISION**


Elenie Girma Wakjira:

Eylül Safiye Varyemez: Exercise 2

Yan Shen:

**Exercise 2:**

Complexity Analysis Questions:

The divide-and-conquer functions (max_engagement, sum_engagement, count_above_threshold) all run in O(n) since every post is visited exactly once, proven by T(n) = 2·T(n/2) + O(1) via the Master Theorem. Merge Sort outperforms Insertion Sort significantly for large inputs with O(n log n) vs O(n²) worst case, though Insertion Sort can be faster for very small arrays. Merge Sort’s recursion depth is O(log n) — only 13-14 levels for 10,000 posts — making stack overflow virtually impossible. Finally, find_peak_hour achieves O(log n) by exploiting the unimodal property of the array: comparing likes[mid] with likes[mid+1] determines which half contains the peak, halving the search space each time, but the algorithm would fail if the array had multiple peaks.​​​​​​​​​​​​​​​​
