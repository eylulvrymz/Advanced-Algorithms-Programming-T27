# Advanced-Algorithms-Programming-T27
LAB 5 REVISION

Elenie Girma Wakjira:Exercise 1

Eylül Safiye Varyemez: Exercise 2

Yan Shen：exercise 3

**Exercise 1:** 
For this exercise we built a binary tree structure using a CategoryNode class to store unique IDs, names, and stream counts, along with child and parent pointers. We implemented core measuring functions like calculate_height, count_nodes, and is_balanced to analyze the tree’s geometry, as well as verification tools to check if the tree is full, perfect, or complete. For navigation, we built find_category using a pre-order DFS and used parent pointers for the find_path_to_root function. We also handled the lowest_common_ancestor using a recursive approach and tested all functions against edge cases like empty, single-node, and skewed trees to ensure the logic was solid.


**Complexity Analysis:** 
All three traversals take O(n) time because every node is visited once. They also take O(h) space for the recursive call stack, which is O(log n) for balanced trees but becomes O(n) if the tree is unbalanced and deep. **Post-order** is used when adding up data like post counts because the child nodes must be processed before the parent. **Pre-order** is used for copying or exporting the tree because the parent needs to be handled before its children. For the category export feature, **pre-order** is the best choice because it processes the parent category first.

**Exercise 2:**
In Exercise 2, we used the three classic binary tree traversals to obtain the list of node names, the cumulative number of posts, and the kth node. For the **in-order** traversal (Left -> Root -> Right), we stored the names sequentially, the cumulative number of posts, and the kth node using a shared counter. For the **pre-order** (Root -> Left -> Right), we exported the tree as indented formatted string, recursively copied the entire tree node by node using deep copy, and exported it as a pipe-separated string. For the **post-order** (Left -> Right -> Root), we stored the cumulative number of posts, the leaf nodes, the average depth of leaf nodes, and the most popular category by comparing the maximum values. We employed the use of small state objects to pass variables such as counters and cumulative values, as Python does not support the passing of variables by reference.

**Complexity Analysis:** All three traversals take **O(n)** time because all nodes are visited once. They also take **O(h)** space for the recursive call stack, which is **O(log n)** for balanced trees and **O(n)** for unbalanced trees. Post-order is used when aggregating data such as the number of posts because the child nodes must be processed before the parent. Pre-order is used when copying data to a different location or exporting data because the parent is processed before the child. For implementing the category export feature, pre-order is the best option because the parent category is processed before the child category.


# Exercise 3 – Generalized Trees (N-ary Trees)

## Files
- `Nodes.java` — `GeneralizedCategoryNode` and `BinaryNode` data structures
- `Exercise3.java` — all methods and main demo

## How to run
```bash
javac Nodes.java Exercise3.java
java Exercise3
```

## Methods

| Method | Description |
|---|---|
| `binary_to_generalized(root)` | Binary tree → N-ary tree |
| `generalized_to_binary(root)` | N-ary tree → Binary tree (first child / next sibling) |
| `pre_order_generalized(node)` | Root → children recursively |
| `post_order_generalized(node)` | Children → root recursively |
| `level_order_generalized(node)` | BFS level by level |
| `calculate_fan_out(node)` | Max children count across all nodes |
| `calculate_height_generalized(node)` | Longest root-to-leaf path |
| `count_nodes_generalized(node)` | Total node count |
| `count_leaves_generalized(node)` | Nodes with no children |
| `calculate_branching_factor(node)` | Average children per non-leaf node |

## Complexity
All methods run in **O(n)** time and **O(h)** space (h = tree height).