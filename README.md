# Advanced-Algorithms-Programming-T27

Eylül Safiye Varyemez: Exercise 2

**Exercise 2:**

**Complexity Analysis:**

When k is Too Small:
If you only have one color, any graph with even a single edge will immediately fail since connected nodes can't share a label. Before running backtracking at all, you can catch obvious impossible cases early — like when a node has more neighbors than available colors, or when k = 2 but the graph has an odd cycle.

Effect of Graph Density:
The denser the graph, the harder it is to color. An empty graph needs just 1 label since there are no conflicts. A complete graph K_n needs n labels since every node conflicts with every other. More edges = more constraints = more colors needed.

Checking vs Finding:
This is the key insight of the whole exercise. Verifying a labeling is O(E) — just check every edge once. Finding the labeling in the first place is O(k^N) in the worst case — exponential. For N = 30 and k = 3 that's around 200 trillion operations, which is completely infeasible. This gap between easy verification and hard construction is exactly why Graph Coloring is NP-Complete, and why in practice people use greedy heuristics or approximations rather than searching for the exact minimum.
