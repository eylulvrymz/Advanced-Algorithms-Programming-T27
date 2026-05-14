from itertools import combinations


class SocialGraph:
    def __init__(self, n):
        self.n = n
        self.adjacency_list = {i: [] for i in range(n)}

    def add_edge(self, u, v):
        if v not in self.adjacency_list[u]:
            self.adjacency_list[u].append(v)
        if u not in self.adjacency_list[v]:
            self.adjacency_list[v].append(u)

    def get_neighbors(self, node):
        return self.adjacency_list[node]

    def get_all_nodes(self):
        return list(self.adjacency_list.keys())

    def get_node_count(self):
        return self.n


# Verification O(N + E)

def is_valid_coverage(selected_users, graph):
    
    covered = [False] * graph.get_node_count()

    for user in selected_users:
        covered[user] = True
        for neighbor in graph.get_neighbors(user):
            covered[neighbor] = True

    return all(covered)


# Exact Solution – Brute Force (N ≤ 20)


def find_minimum_coverage(graph):
    nodes = graph.get_all_nodes()
    n = graph.get_node_count()

    # Edge case: empty graph (no nodes)
    if n == 0:
        return (0, [])

    for size in range(1, n + 1):
        for subset in combinations(nodes, size):
            subset_list = list(subset)
            if is_valid_coverage(subset_list, graph):
                return (size, subset_list)

    # Fallback: all nodes (always valid)
    return (n, nodes)

# Greedy Approximation – O(N^2)


def find_fast_coverage(graph):
    nodes = graph.get_all_nodes()

    if graph.get_node_count() == 0:
        return (0, [])

    selected_users = []
    uncovered = set(nodes)

    while uncovered:
        best_user = None
        best_newly_covered = set()

        for user in nodes:
            # Potential coverage: the user itself + all its neighbors
            potential = set(graph.get_neighbors(user)) | {user}
            newly_covered = potential & uncovered

            if len(newly_covered) > len(best_newly_covered):
                best_user = user
                best_newly_covered = newly_covered

        # Pick the best node found this round
        selected_users.append(best_user)
        uncovered -= best_newly_covered

    return (len(selected_users), selected_users)
