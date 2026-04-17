# Advanced-Algorithms-Programming-T27
TPs of the class for T27

Elenie Girma Wakjira:Exercise 1

Eylül Safiye Varyemez: Exercise 2

Yan Shen：exercise 3

**Exercise 1:** For this exercise we built a spatial splitting system using three recursive functions that together implement a quadtree-style divide and conquer approach. split_region takes a rectangular region defined by its top-left corner and dimensions and recursively divides it into four equal quadrants, stopping once the region reaches the minimum allowed size. count_points_in_region iterates over a list of points and counts how many fall within a given rectangle using a half-open interval boundary convention, ensuring adjacent regions never double-count shared edges. find_dense_regions combines both functions by recursively splitting space while pruning any quadrant whose point density falls below a given threshold, returning only the leaf regions that are sufficiently dense. We tested all functions against edge cases including empty point lists, regions exactly equal to the minimum size, zero-area regions, points on boundaries, and impossibly high density thresholds.

**Complexity Analysis:** count_points_in_region runs in O(N) where N is the number of points, since every point must be checked individually. split_region produces O(4^d) recursive calls at depth d, and for a space of size S×S split down to 1×1 cells the total number of calls is O(S²), matching the number of unit cells. find_dense_regions significantly improves on this in practice: since sparse quadrants are pruned immediately before recursing, only dense branches are explored. If all points are clustered in one corner, three quadrants get discarded at every level, reducing the number of calls from O(S²) to O(N log N) in the best case. In the worst case where points are perfectly uniform, no pruning occurs and we fall back to O(S²). Memory usage is O(d) for the recursion stack at any given moment, where d = log₂(S/min_size) is the maximum depth, making this approach practical even for large spaces.

