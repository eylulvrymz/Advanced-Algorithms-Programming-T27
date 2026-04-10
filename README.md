# Advanced-Algorithms-Programming-T27
TPs of the class for T27


**Exercise 1:** For this exercise we built a graph structure using a SocialGraph class that maintains both an adjacency matrix and an adjacency list simultaneously, storing the number of users and edges alongside them. We implemented core operations like add_friendship, remove_friendship, and are_friends, as well as utility functions to retrieve friends, degree, and graph-level statistics. For graph property analysis, we built is_complete_graph, graph_density, and degree_distribution. We also implemented conversion functions to switch between the two representations in both directions, and tested all functions against edge cases like empty graphs, single-node graphs, and disconnected users.

**Complexity Analysis:** are_friends takes O(1) with the adjacency matrix due to direct array access, but O(deg(u)) with the adjacency list since the linked list must be traversed. For a network the size of Facebook (n = 10⁹, avg degree 150), the matrix would require roughly 125,000 TB while the adjacency list needs only ~1.8 TB, making the list around 70,000× more space-efficient. Although the matrix offers faster edge removal at O(1) compared to O(deg(u)) for the list, the O(n²) memory cost makes it entirely impractical for large sparse networks.
