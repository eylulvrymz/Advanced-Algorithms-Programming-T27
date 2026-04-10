from Exercise2 import *

def run_tests():
    print("--- Starting SocialGraph Edge Case Tests ---")

    # CASE 1: Standard Social Network (Multiple Components + Isolated User)
    # Testing: find_connected_components, find_isolated_users, has_path [cite: 48, 50, 55]
    users = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
    g1 = SocialGraph(users)
    g1.add_friendship("Alice", "Bob")
    g1.add_friendship("Bob", "Charlie")
    g1.add_friendship("David", "Eve")
    # Frank remains isolated 

    print("\n[Case 1: Standard Network]")
    print(f"Isolated Users (Expected ['Frank']): {g1.find_isolated_users()}")
    print(f"Connected Components Count (Expected 3): {len(g1.find_connected_components())}")
    print(f"Path Alice -> Charlie (Expected True): {g1.has_path('Alice', 'Charlie')}")
    print(f"Path Alice -> David (Expected False): {g1.has_path('Alice', 'David')}")

    # CASE 2: Empty Graph
    # Testing: Handling of null/empty vertex sets [cite: 48]
    g2 = SocialGraph([])
    print("\n[Case 2: Empty Graph]")
    print(f"Components (Expected []): {g2.find_connected_components()}")
    print(f"Isolated (Expected []): {g2.find_isolated_users()}")

    # CASE 3: Complete Graph (Fully Connected)
    # Testing: is_connected and graph density logic [cite: 24, 49]
    users_small = ["A", "B", "C"]
    g3 = SocialGraph(users_small)
    g3.add_friendship("A", "B")
    g3.add_friendship("B", "C")
    g3.add_friendship("A", "C")
    print("\n[Case 3: Complete Graph]")
    print(f"Is Connected (Expected True): {g3.is_connected()}")
    print(f"Component Sizes (Expected [3]): {g3.get_component_sizes()}")

    # CASE 4: Cyclic Friendship (Infinite Loop Check)
    # Testing: visited_set logic in DFS [cite: 45, 46]
    g4 = SocialGraph(["A", "B", "C"])
    g4.add_friendship("A", "B")
    g4.add_friendship("B", "C")
    g4.add_friendship("C", "A") # Creates a circle/cycle
    print("\n[Case 4: Cyclic Graph]")
    try:
        order = g4.dfs_iterative("A")
        print(f"DFS Iterative Order (No infinite loop): {order}")
    except Exception as e:
        print(f"Error in Cyclic Graph: {e}")

    # CASE 5: Single User (The "Loner" Edge Case)
    # Testing: Behavior with a single node and no edges 
    g5 = SocialGraph(["Zane"])
    print("\n[Case 5: Single User]")
    print(f"Is Connected (Expected True): {g5.is_connected()}")
    print(f"Isolated Users (Expected ['Zane']): {g5.find_isolated_users()}")

if __name__ == "__main__":
    # Ensure your SocialGraph class is defined above this
    run_tests()

"""
Results:

--- Starting SocialGraph Edge Case Tests ---

[Case 1: Standard Network]
Isolated Users (Expected ['Frank']): ['Frank']
Connected Components Count (Expected 3): 3
Path Alice -> Charlie (Expected True): True
Path Alice -> David (Expected False): False

[Case 2: Empty Graph]
Components (Expected []): []
Isolated (Expected []): []

[Case 3: Complete Graph]
Is Connected (Expected True): True
Component Sizes (Expected [3]): [3]

[Case 4: Cyclic Graph]
DFS Iterative Order (No infinite loop): ['A', 'C', 'B']

[Case 5: Single User]
Is Connected (Expected True): True
Isolated Users (Expected ['Zane']): ['Zane']

"""