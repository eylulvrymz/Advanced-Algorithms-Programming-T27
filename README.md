# Advanced-Algorithms-Programming-T27-LAB09

Eylül Safiye Varyemez: Exercise 2

**Exercise 2:** For Exercise 2, we implemented all three required functions. We started with `is_valid_labeling` which checks if a given labeling is valid by simply going through every edge and making sure no two connected nodes share the same label, hitting the required O(E) complexity. Then we built `assign_labels` which tries to color the graph using at most k colors through a backtracking approach — it goes node by node, tries each color, and if it gets stuck it undoes its last choice and tries something else, which covers the greedy backtracking requirement. Finally `find_min_labels` ties it all together by repeatedly calling `assign_labels` starting from k = 1 and going up until it finds a valid coloring, which gives us the minimum number of labels needed. On top of that, we wrote a test file covering all the edge cases the assignment asks about — an empty graph, a single node, a fully connected graph, a two node graph, an odd cycle, an even cycle, and a sparse path — each one testing both the minimum label count and whether a given labeling is valid or not. Everything was kept simple and straightforward, matching the pseudocode we wrote, so the logic is easy to follow and verify.

**Complexity Analysis:**

When k is Too Small:
If you only have one color, any graph with even a single edge will immediately fail since connected nodes can't share a label. Before running backtracking at all, you can catch obvious impossible cases early — like when a node has more neighbors than available colors, or when k = 2 but the graph has an odd cycle.

Effect of Graph Density:
The denser the graph, the harder it is to color. An empty graph needs just 1 label since there are no conflicts. A complete graph K_n needs n labels since every node conflicts with every other. More edges = more constraints = more colors needed.

Checking vs Finding:
This is the key insight of the whole exercise. Verifying a labeling is O(E) — just check every edge once. Finding the labeling in the first place is O(k^N) in the worst case — exponential. For N = 30 and k = 3 that's around 200 trillion operations, which is completely infeasible. This gap between easy verification and hard construction is exactly why Graph Coloring is NP-Complete, and why in practice people use greedy heuristics or approximations rather than searching for the exact minimum.
