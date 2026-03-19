# Advanced-Algorithms-Programming-T27

**LAB 4 REVISION**


Elenie Girma Wakjira:Exercise 1

Eylül Safiye Varyemez: Exercise 2

Yan Shen:

**Exercise 1:**
For this exercise we are trying to model the structure where users reply to comments and create deeply nested threads. We use recursive data structure; CommentNode, where each comment contains the user id, comment id, time stamp, their content, likes and replies. Each comment will contain a list of replies and each reply acting as comments and going on like that. We use recursive functions to traverse, search, count, and manage the nested threads to perform real operations like displaying comment section or searching for a user's comments. 

**Functions implemented:**
- display_thread: prints the thread with indentation showing nesting level
- count_total_comments: counts all comments including nested replies
- total_likes: sums all likes across the entire thread
- find_deepest_reply: finds the maximum nesting depth
- search_by_user: collects all comments written by a specific user
- contains_keyword: checks if a keyword exists anywhere in the thread
- delete_comment: removes a comment and all its replies
- get_thread_without_comment: returns a fresh copy without the deleted comment
  
**Exercise 2:**

In this exercise, we defined a Post dataclass with an engagement_score property that automatically computes likes×1 + comments×2 + shares×3. For Part A, max_engagement recursively splits the posts array in half and returns the larger engagement score between the two halves. Part B follows the same divide-and-conquer splitting logic in sum_engagement to total all scores, which average_engagement then divides by the number of posts. Part C’s count_above_threshold uses the same recursive splitting but counts only the posts whose engagement score exceeds the given threshold at the leaf level. Part D implements classic Merge Sort through two functions — merge_sort_by_engagement recursively splits the array and merge combines the two sorted halves by comparing engagement scores — resulting in a fully sorted posts list. Finally, find_peak_hour takes a 24-element hourly likes array and recursively narrows down to the peak hour by comparing the middle element with its right neighbor, leveraging the unimodal nature of the data to halve the search space at each step.​​​​​​​​​​​​​​​​

Complexity Analysis Questions:

The divide-and-conquer functions (max_engagement, sum_engagement, count_above_threshold) all run in O(n) since every post is visited exactly once, proven by T(n) = 2·T(n/2) + O(1) via the Master Theorem. Merge Sort outperforms Insertion Sort significantly for large inputs with O(n log n) vs O(n²) worst case, though Insertion Sort can be faster for very small arrays. Merge Sort’s recursion depth is O(log n) — only 13-14 levels for 10,000 posts — making stack overflow virtually impossible. Finally, find_peak_hour achieves O(log n) by exploiting the unimodal property of the array: comparing likes[mid] with likes[mid+1] determines which half contains the peak, halving the search space each time, but the algorithm would fail if the array had multiple peaks.​​​​​​​​​​​​​​​​
