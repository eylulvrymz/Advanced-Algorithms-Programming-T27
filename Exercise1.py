class SocialGraph:
    def __init__(self, n):
        self.n = n
        self.m = 0
        self.matrix = [[0] * n for _ in range(n)]
        self.adj = [[] for _ in range(n)]

    def add_friendship(self, u, v):
        if u == v:
            return  # no self-loops
        if not self.are_friends(u, v):
            self.matrix[u][v] = 1
            self.matrix[v][u] = 1
            self.adj[u].append(v)
            self.adj[v].append(u)
            self.m += 1

    def remove_friendship(self, u, v):
        if self.are_friends(u, v):
            self.matrix[u][v] = 0
            self.matrix[v][u] = 0
            self.adj[u].remove(v)
            self.adj[v].remove(u)
            self.m -= 1

    def are_friends(self, u, v):
        return self.matrix[u][v] == 1

    def get_friends_matrix(self, u):
        friends = []
        for i in range(self.n):
            if self.matrix[u][i] == 1:
                friends.append(i)
        return friends

    def get_friends_list(self, u):
        return list(self.adj[u])

    def get_degree(self, u):
        return len(self.adj[u])

    def get_num_users(self):
        return self.n

    def get_num_edges(self):
        return self.m

    def is_complete_graph(self):
        expected = (self.n * (self.n - 1)) // 2
        return self.m == expected

    def graph_density(self):
        if self.n < 2:
            return 0.0
        return (2 * self.m) / (self.n * (self.n - 1))

    def degree_distribution(self):
        dist = {}
        for u in range(self.n):
            d = self.get_degree(u)
            dist[d] = dist.get(d, 0) + 1
        return dist

    def matrix_to_list(self):
        self.adj = [[] for _ in range(self.n)]
        for u in range(self.n):
            for v in range(self.n):
                if self.matrix[u][v] == 1:
                    self.adj[u].append(v)

    def list_to_matrix(self):
        self.matrix = [[0] * self.n for _ in range(self.n)]
        for u in range(self.n):
            for v in self.adj[u]:
                self.matrix[u][v] = 1



def run_tests():
    passed = 0
    failed = 0

    def check(description, result, expected):
        nonlocal passed, failed
        if result == expected:
            print(f"  PASS: {description}")
            passed += 1
        else:
            print(f"  FAIL: {description} --> got {result}, expected {expected}")
            failed += 1

    # Test 1: Self-loop
    print("\nTest 1: Self-loop")
    g = SocialGraph(3)
    g.add_friendship(0, 0)
    check("no self-loop added to matrix", g.matrix[0][0], 0)
    check("no self-loop added to adj", g.adj[0], [])
    check("edge count stays 0", g.m, 0)

    # Test 2: Duplicate edge
    print("\nTest 2: Duplicate edge")
    g = SocialGraph(3)
    g.add_friendship(0, 1)
    g.add_friendship(0, 1)  # second call should do nothing
    check("edge count is still 1", g.m, 1)
    check("adj[0] has only one entry", g.adj[0], [1])
    check("adj[1] has only one entry", g.adj[1], [0])

    # Test 3: Remove a friendship that doesn't exist 
    print("\nTest 3: Remove non-existent friendship")
    g = SocialGraph(3)
    g.remove_friendship(0, 1)  # should not crash
    check("edge count stays 0", g.m, 0)
    check("matrix unchanged", g.matrix[0][1], 0)

    # Test 4: graph_density on graph with 0 or 1 node 
    print("\nTest 4: graph_density on tiny graphs")
    g0 = SocialGraph(0)
    check("density with 0 nodes", g0.graph_density(), 0.0)
    g1 = SocialGraph(1)
    check("density with 1 node", g1.graph_density(), 0.0)

    # Test 5: is_complete_graph on empty graph (n=0) 
    print("\nTest 5: is_complete_graph edge cases")
    g = SocialGraph(0)
    check("complete graph with 0 nodes", g.is_complete_graph(), True)  # 0 == 0 edges expected
    g = SocialGraph(1)
    check("complete graph with 1 node", g.is_complete_graph(), True)  # 0 == 0 edges expected

    # Test 6: matrix_to_list then list_to_matrix round trip 
    print("\nTest 6: Round-trip conversion")
    g = SocialGraph(4)
    g.add_friendship(0, 1)
    g.add_friendship(1, 2)
    g.add_friendship(2, 3)
    original_matrix = [row[:] for row in g.matrix]  # save a copy
    g.matrix_to_list()
    g.list_to_matrix()
    check("matrix survives round-trip", g.matrix, original_matrix)

    # Test 7: degree_distribution on isolated graph 
    print("\nTest 7: degree_distribution all isolated")
    g = SocialGraph(4)
    dist = g.degree_distribution()
    check("all 4 users have degree 0", dist, {0: 4})

    # Test 8: get_friends_list returns a copy 
    print("\nTest 8: get_friends_list does not expose internal list")
    g = SocialGraph(3)
    g.add_friendship(0, 1)
    friends = g.get_friends_list(0)
    friends.append(99)  # mutate the returned list
    check("internal adj[0] not affected", g.adj[0], [1])

    print(f"\n{passed} passed, {failed} failed out of {passed + failed} tests")


run_tests()
