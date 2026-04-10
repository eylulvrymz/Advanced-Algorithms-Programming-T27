class SocialGraph:
    def __init__(self, users):
        # User list start
        self.users = users
        self.adj_list = {user: [] for user in users}

    def add_friendship(self, u, v):
        if u in self.adj_list and v in self.adj_list:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)

    def get_friends(self, u):
        return self.adj_list.get(u, [])

    def get_degree(self, u):
        return len(self.get_friends(u))

    # --- Exercise 2: DFS ---

    # Part A: Recursive DFS
    def dfs_recursive(self, current_user, visited_set=None, order_list=None):
        if visited_set is None: visited_set = set()
        if order_list is None: order_list = []
        
        visited_set.add(current_user)
        order_list.append(current_user)
        
        for friend in self.get_friends(current_user):
            if friend not in visited_set:
                self.dfs_recursive(friend, visited_set, order_list)
        
        return order_list

    # Part B: Iterative DFS using stack
    def dfs_iterative(self, start_user):
        visited = set()
        stack = [start_user]
        result = []

        while stack:
            u = stack.pop()
            if u not in visited:
                visited.add(u)
                result.append(u)
                # Add neighbours to stack
                for v in self.get_friends(u):
                    if v not in visited:
                        stack.append(v)
        return result

    # Part C: Find all connected components
    def find_connected_components(self):
        visited = set()
        components = []

        for u in self.users:
            if u not in visited:
                # Update visited list and call DFS 
                component = self.dfs_recursive(u, visited)
                components.append(component)
        return components

    # Part D: Check if graph is connected
    def is_connected(self):
        components = self.find_connected_components()
        return len(components) == 1

    # Part E: Find if path exists between two users
    def has_path(self, start_user, target_user):
        visited = set()
        stack = [start_user]

        while stack:
            u = stack.pop()
            if u == target_user: 
                return True
            if u not in visited:
                visited.add(u)
                for v in self.get_friends(u):
                    if v not in visited:
                        stack.append(v)
        return False

    # Part F: Find path between users
    def find_path(self, start_user, target_user):
        visited = set()
        stack = [(start_user, [start_user])]

        while stack:
            u, path = stack.pop()
            if u == target_user: 
                return path
            if u not in visited:
                visited.add(u)
                for v in self.get_friends(u):
                    if v not in visited:
                        stack.append((v, path + [v]))
        return []

    # --- Traversal-Based Analytics ---

    def get_component_sizes(self):
        return [len(c) for c in self.find_connected_components()]

    def find_largest_component(self):
        components = self.find_connected_components()
        if not components: return []
        return max(components, key=len)

    def find_isolated_users(self):
        return [u for u in self.users if self.get_degree(u) == 0]

# --- Test Example ---
users = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
social_net = SocialGraph(users)

social_net.add_friendship("Alice", "Bob")
social_net.add_friendship("Bob", "Charlie")
social_net.add_friendship("David", "Eve")
# Frank has no friends (isolated)

print("Connected Components:", social_net.find_connected_components())
print("Isolated Users:", social_net.find_isolated_users())
print("Is there a path from Alice to Charlie?:", social_net.has_path("Alice", "Charlie"))
print("Is there a path from Alice to David?:", social_net.has_path("Alice", "David"))