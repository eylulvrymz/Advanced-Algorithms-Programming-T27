# Advanced-Algorithms-Programming-T27
TPs of the class for T27

Elenie Girma Wakjira

Eylul Safiye Varyemez

Yan Shen

**Exercise 1:** For this exercise we built a user management system using a Binary Search Tree where each node stores a user ID, name, and friend list. insert places users by comparing IDs recursively and ignores duplicates. find traverses left or right at each node, returning the node or None. inorder_traversal performs a left-root-right recursion, naturally producing a sorted list of user IDs with no additional sorting step. delete handles all three cases ; leaf removal, single-child promotion, and the two-child case where the node is replaced by its inorder successor — preserving BST ordering throughout. suggest_friends collects direct friends into a set for O(1) lookup, counts how often each friend-of-friend candidate appears across all friend lists, excludes the user and their existing connections, and returns the top results by frequency. The analytics functions get_height, is_balanced, and get_leaf_count all operate through recursive tree traversal, with is_balanced using a sentinel value of −2 to short-circuit as soon as a violation is detected. We tested all functions against edge cases including empty trees, duplicate insertions, deletion of leaves and two-child nodes, friend references to users not in the tree, and sequential insertion producing a degenerate right-skewed chain.

**Complexity Analysis:** insert, find, and delete all run in O(log n) average and O(n) worst case when the tree degenerates into a chain from sequential insertion. inorder_traversal runs in O(n) since every node is visited once. suggest_friends runs in O(F² · log n) where F is the number of direct friends, as each friend lookup costs O(log n) and each friend's list has up to F entries. get_height, is_balanced, and get_leaf_count all run in O(n) in the worst case. Memory usage across all functions is O(h) for the call stack, where h is O(log n) on average and O(n) in the degenerate case.

**Exercise 2:** For this exercise, the TrendingHeap class was created with a max-heap data structure based on a Python list of dictionaries containing posts' likes, post_id and timestamp. The heap order principle, the maximum value being the root of the heap, is upheld with the help of two helper methods: _heapify_up and _heapify_down, used whenever there is any alteration made to the heap. In order to fulfill the request for efficient modifications without going through the entire array, a dictionary called pos was used to map each post_id to the index in which it currently resides in the heap. The five required methods were implemented correctly, including get_top_k which uses a copy of the heap rather than destroying the original one.

**Complexity Analysis:** For the complexity analysis of Exercise 2, `get_top_k(k)` takes O(n + k log n) because it calls `pop_max` k times with the copied heap structure, which is much faster compared to the O(n log n) required to sort all posts, given that only k items will be ordered. `update_likes` would take O(n) for every update with a sorted array as a result of the reinsertion cost caused by value change, while the heap will accomplish this in O(log n) with `_heapify_up` and `_heapify_down` methods, where the location is given in O(1) using `pos`. Finally, when you need to automatically remove posts that have expired after 24 hours, the best way would be lazy deletion, done in `pop_max` or `peek_max` methods with a time check within, without allocating additional memory.

决定采用简洁单段英文格式。# Exercise 3: Prefix and Range Trees

This exercise implements two data structures for a social network use case.
Part A builds an AutocompleteTrie that supports fast prefix-based username search
in O(P + R) time. Part B builds an ActivitySegmentTree that stores daily post counts
and answers range sum, max, and min queries in O(log n) time. Run Exercise3Test.java to verify all functionality.