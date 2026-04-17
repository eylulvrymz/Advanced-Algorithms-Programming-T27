# Advanced-Algorithms-Programming-T27
TPs of the class for T27

Elenie Girma Wakjira:Exercise 1

Eylül Safiye Varyemez: Exercise 2

Yan Shen：exercise 3

**Exercise 1:** For this exercise we built a spatial splitting system using three recursive functions that together implement a quadtree-style divide and conquer approach. split_region takes a rectangular region defined by its top-left corner and dimensions and recursively divides it into four equal quadrants, stopping once the region reaches the minimum allowed size. count_points_in_region iterates over a list of points and counts how many fall within a given rectangle using a half-open interval boundary convention, ensuring adjacent regions never double-count shared edges. find_dense_regions combines both functions by recursively splitting space while pruning any quadrant whose point density falls below a given threshold, returning only the leaf regions that are sufficiently dense. We tested all functions against edge cases including empty point lists, regions exactly equal to the minimum size, zero-area regions, points on boundaries, and impossibly high density thresholds.

**Complexity Analysis:** count_points_in_region runs in O(N) where N is the number of points, since every point must be checked individually. split_region produces O(4^d) recursive calls at depth d, and for a space of size S×S split down to 1×1 cells the total number of calls is O(S²), matching the number of unit cells. find_dense_regions significantly improves on this in practice: since sparse quadrants are pruned immediately before recursing, only dense branches are explored. If all points are clustered in one corner, three quadrants get discarded at every level, reducing the number of calls from O(S²) to O(N log N) in the best case. In the worst case where points are perfectly uniform, no pruning occurs and we fall back to O(S²). Memory usage is O(d) for the recursion stack at any given moment, where d = log₂(S/min_size) is the maximum depth, making this approach practical even for large spaces.

**Exercise 2:** The script contains three basic functions that draw and calculate self-similar geometrical shapes:

The Sierpinski Triangle (draw_sierpinski): The function creates a triangle using the divide-and-conquer approach where it draws three triangles from each triangle. It terminates the recursion process when depth = 0 and draws the final filled polygons.

The Fractal Tree (draw_tree): The function simulates a tree structure using a recursive algorithm where it first draws the main trunk and then two secondary branches at +30 and -30 degrees. The thickness of the branch decreases, and the color changes from brown to green depending on the depth.

The Fractal Dimension (fractal_dimension): The box-counting method was used to estimate the fractal dimension by counting the number of overlapped grids for different grid sizes. The calculation is done based on the slope of log(number of grids) vs log(1/grid size).

**Complexity Analysis:** Complexity of the Sierpinski Triangle: As each iteration of the triangle divides it into three triangles identical to the initial one, the complexity of drawing the triangles follows a formula of 3^d. Thus, for a depth of recursion of 5, the number of triangles will be equal to 3^5 = 243. Dimensions of Fractals (D): The dimension of a straight line will be equal to D = 1 since it fully occupies a one-dimensional space.The dimension of a fully filled square will be equal to D = 2 as it fully occupies a two-dimensional space.The dimension of the Sierpinski Triangle lies somewhere in between (about 1.585).

# Exercise 3 – Procedural Generation

Three functions: `midpointDisplacement` splits a line recursively with random offsets, `generateTerrain` builds a 2D height map using diamond-square, and `detectArtifacts` flags cells where height changes too sharply.

## Run

```bash
javac Exercise3.java exercise3_test.java
java Exercise3
java exercise3_test
```

Higher roughness = spikier terrain. Higher depth = more detail. Adjust the threshold in `detectArtifacts` to control sensitivity.