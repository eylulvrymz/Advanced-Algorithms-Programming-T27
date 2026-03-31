# Advanced-Algorithms-Programming-T27
LAB 5 REVISION

Elenie Girma Wakjira:Exercise 1

Eylül Safiye Varyemez: Exercise 2

Yan Shen：exercise 3

**Exercise 2:**
In Exercise 2, we used the three classic binary tree traversals to obtain the list of node names, the cumulative number of posts, and the kth node. For the **in-order** traversal (Left -> Root -> Right), we stored the names sequentially, the cumulative number of posts, and the kth node using a shared counter. For the **pre-order** (Root -> Left -> Right), we exported the tree as indented formatted string, recursively copied the entire tree node by node using deep copy, and exported it as a pipe-separated string. For the **post-order** (Left -> Right -> Root), we stored the cumulative number of posts, the leaf nodes, the average depth of leaf nodes, and the most popular category by comparing the maximum values. We employed the use of small state objects to pass variables such as counters and cumulative values, as Python does not support the passing of variables by reference.

**Complexity Analysis:** All three traversals take **O(n)** time because all nodes are visited once. They also take **O(h)** space for the recursive call stack, which is **O(log n)** for balanced trees and **O(n)** for unbalanced trees. Post-order is used when aggregating data such as the number of posts because the child nodes must be processed before the parent. Pre-order is used when copying data to a different location or exporting data because the parent is processed before the child. For implementing the category export feature, pre-order is the best option because the parent category is processed before the child category.
