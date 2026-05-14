# Advanced-Algorithms-Programming-T27-LAB09
Elenie Girma Wakjira: Exercise 1
Eylül Safiye Varyemez: Exercise 2

**Exercise 1:** For this exercise we implemented three functions to find the smallest group of users that covers an entire social network. is_valid_coverage marks each selected user and their neighbors as covered, then checks that no node was left out. find_minimum_coverage finds the exact smallest dominating set by trying all possible subsets from smallest to largest and stopping as soon as a valid one is found. find_fast_coverage is a faster greedy version that repeatedly picks whichever user covers the most uncovered nodes at each step until everyone is covered. We tested all three against empty graphs, single nodes, isolated nodes, paths, stars, complete graphs, triangles, and cycles, and also compared the greedy and exact results side by side on small graphs.

**Complexity Analysis:** is_valid_coverage runs in O(N + E) since it touches each node and edge at most once. find_minimum_coverage runs in O(2^N · (N + E)) in the worst case as it enumerates all subsets, making it feasible only for small graphs up to around N = 20. find_fast_coverage runs in O(N²) since at each of the N rounds it scans all nodes and their neighbors to find the best candidate, making it practical even for very large graphs. The greedy solution is not guaranteed to find the minimum — it provides an O(log N) approximation — meaning it may return a slightly larger set than optimal on certain graph structures. Memory usage is O(N) across all three functions for the covered array and the uncovered set tracked during the greedy loop.


**Exercise 2:** For Exercise 2, we implemented all three required functions. We started with `is_valid_labeling` which checks if a given labeling is valid by simply going through every edge and making sure no two connected nodes share the same label, hitting the required O(E) complexity. Then we built `assign_labels` which tries to color the graph using at most k colors through a backtracking approach — it goes node by node, tries each color, and if it gets stuck it undoes its last choice and tries something else, which covers the greedy backtracking requirement. Finally `find_min_labels` ties it all together by repeatedly calling `assign_labels` starting from k = 1 and going up until it finds a valid coloring, which gives us the minimum number of labels needed. On top of that, we wrote a test file covering all the edge cases the assignment asks about — an empty graph, a single node, a fully connected graph, a two node graph, an odd cycle, an even cycle, and a sparse path — each one testing both the minimum label count and whether a given labeling is valid or not. Everything was kept simple and straightforward, matching the pseudocode we wrote, so the logic is easy to follow and verify.

**Complexity Analysis:**

When k is Too Small:
If you only have one color, any graph with even a single edge will immediately fail since connected nodes can't share a label. Before running backtracking at all, you can catch obvious impossible cases early — like when a node has more neighbors than available colors, or when k = 2 but the graph has an odd cycle.

Effect of Graph Density:
The denser the graph, the harder it is to color. An empty graph needs just 1 label since there are no conflicts. A complete graph K_n needs n labels since every node conflicts with every other. More edges = more constraints = more colors needed.

Checking vs Finding:
This is the key insight of the whole exercise. Verifying a labeling is O(E) — just check every edge once. Finding the labeling in the first place is O(k^N) in the worst case — exponential. For N = 30 and k = 3 that's around 200 trillion operations, which is completely infeasible. This gap between easy verification and hard construction is exactly why Graph Coloring is NP-Complete, and why in practice people use greedy heuristics or approximations rather than searching for the exact minimum.
