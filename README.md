# Advanced-Algorithms-Programming-T27
LAB 5 REVISION

Elenie Girma Wakjira:Exercise 1

Eylül Safiye Varyemez: Exercise 2

Yan Shen：exercise 3

**Exercise 2:**
In Exercise 2, we used the three classic binary tree traversals to obtain the list of node names, the cumulative number of posts, and the kth node. For the **in-order** traversal (Left -> Root -> Right), we stored the names sequentially, the cumulative number of posts, and the kth node using a shared counter. For the **pre-order** (Root -> Left -> Right), we exported the tree as indented formatted string, recursively copied the entire tree node by node using deep copy, and exported it as a pipe-separated string. For the **post-order** (Left -> Right -> Root), we stored the cumulative number of posts, the leaf nodes, the average depth of leaf nodes, and the most popular category by comparing the maximum values. We employed the use of small state objects to pass variables such as counters and cumulative values, as Python does not support the passing of variables by reference.
