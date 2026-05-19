from Exercise2 import maximize_reach_exact, maximize_reach_greedy, is_within_budget

# - Edge Case Tests -

print("=== Edge Case 1: Budget = 0 ===")
# No money at all, nobody can be selected
reach, users = maximize_reach_exact(0, [3, 4, 5], [4, 5, 6])
print(f"Exact  → reach: {reach}, users: {users}")  # Expected: 0, []
reach, users = maximize_reach_greedy(0, [3, 4, 5], [4, 5, 6])
print(f"Greedy → reach: {reach}, users: {users}")  # Expected: 0, []

print("\n=== Edge Case 2: All users too expensive ===")
# Every user costs more than the budget
reach, users = maximize_reach_exact(2, [5, 6, 7], [10, 20, 30])
print(f"Exact  → reach: {reach}, users: {users}")  # Expected: 0, []
reach, users = maximize_reach_greedy(2, [5, 6, 7], [10, 20, 30])
print(f"Greedy → reach: {reach}, users: {users}")  # Expected: 0, []

print("\n=== Edge Case 3: Single user, fits in budget ===")
reach, users = maximize_reach_exact(5, [3], [8])
print(f"Exact  → reach: {reach}, users: {users}")  # Expected: 8, [0]
reach, users = maximize_reach_greedy(5, [3], [8])
print(f"Greedy → reach: {reach}, users: {users}")  # Expected: 8, [0]

print("\n=== Edge Case 4: Single user, does not fit ===")
reach, users = maximize_reach_exact(2, [3], [8])
print(f"Exact  → reach: {reach}, users: {users}")  # Expected: 0, []
reach, users = maximize_reach_greedy(2, [3], [8])
print(f"Greedy → reach: {reach}, users: {users}")  # Expected: 0, []

print("\n=== Edge Case 5: All users have the same cost and reach ===")
# Should just pick as many as the budget allows
reach, users = maximize_reach_exact(9, [3, 3, 3, 3], [5, 5, 5, 5])
print(f"Exact  → reach: {reach}, users: {users}")  # Expected: 15, 3 users
reach, users = maximize_reach_greedy(9, [3, 3, 3, 3], [5, 5, 5, 5])
print(f"Greedy → reach: {reach}, users: {users}")  # Expected: 15, 3 users

print("\n=== Edge Case 6: Budget exactly covers one user ===")
reach, users = maximize_reach_exact(5, [5, 3, 4], [9, 6, 7])
print(f"Exact  → reach: {reach}, users: {users}")  # Expected: 13, users 1+2
reach, users = maximize_reach_greedy(5, [5, 3, 4], [9, 6, 7])
print(f"Greedy → reach: {reach}, users: {users}")

print("\n=== Edge Case 7: Empty user list ===")
reach, users = maximize_reach_exact(100, [], [])
print(f"Exact  → reach: {reach}, users: {users}")  # Expected: 0, []
reach, users = maximize_reach_greedy(100, [], [])
print(f"Greedy → reach: {reach}, users: {users}")  # Expected: 0, []

print("\n=== Edge Case 8: Budget covers everyone ===")
# Plenty of budget, all users should be selected
reach, users = maximize_reach_exact(100, [3, 4, 5], [4, 5, 6])
print(f"Exact  → reach: {reach}, users: {users}")  # Expected: 15, all users
reach, users = maximize_reach_greedy(100, [3, 4, 5], [4, 5, 6])
print(f"Greedy → reach: {reach}, users: {users}")  # Expected: 15, all users