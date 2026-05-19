def maximize_reach_exact(budget, costs, reaches):
    N = len(costs)
    
    # Initialize 2D DP table with zeros
    dp = [[0] * (budget + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        for w in range(0, budget + 1):
            # Option 1: skip user i
            dp[i][w] = dp[i - 1][w]
            
            # Option 2: include user i (if affordable)
            if costs[i - 1] <= w:
                include = dp[i - 1][w - costs[i - 1]] + reaches[i - 1]
                if include > dp[i][w]:
                    dp[i][w] = include
    
    # Backtrack to find selected users
    selected = []
    w = budget
    for i in range(N, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)  # user index
            w -= costs[i - 1]
    
    return (dp[N][budget], selected)


def is_within_budget(selection, costs, budget):
    total = 0
    for i in selection:
        total += costs[i]
    return total <= budget


def maximize_reach_greedy(budget, costs, reaches):
    N = len(costs)
    
    # Build ratio list, avoid division by zero
    ratios = []
    for i in range(N):
        if costs[i] > 0:
            ratios.append((reaches[i] / costs[i], i))
    
    # Sort by ratio descending
    ratios.sort(reverse=True)
    
    selected = []
    total_cost = 0
    total_reach = 0
    
    for ratio, i in ratios:
        if total_cost + costs[i] <= budget:
            selected.append(i)
            total_cost += costs[i]
            total_reach += reaches[i]
    
    return (total_reach, selected)


# ── Tests ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Basic test
    budget  = 10
    costs   = [3, 4, 5, 2]
    reaches = [4, 5, 6, 3]

    print("=== Basic Test ===")
    exact_reach, exact_users = maximize_reach_exact(budget, costs, reaches)
    print(f"Exact   → reach: {exact_reach}, users: {exact_users}")
    print(f"Budget check: {is_within_budget(exact_users, costs, budget)}")

    greedy_reach, greedy_users = maximize_reach_greedy(budget, costs, reaches)
    print(f"Greedy  → reach: {greedy_reach}, users: {greedy_users}")
    print(f"Budget check: {is_within_budget(greedy_users, costs, budget)}")

    # Counterexample where greedy fails
    print("\n=== Greedy Counterexample ===")
    budget2  = 10
    costs2   = [6, 5, 5]
    reaches2 = [7, 5, 5]   # greedy picks user 0 (ratio 7/6 ≈ 1.17), misses users 1+2 (reach 10)

    exact_reach2, exact_users2 = maximize_reach_exact(budget2, costs2, reaches2)
    print(f"Exact   → reach: {exact_reach2}, users: {exact_users2}")

    greedy_reach2, greedy_users2 = maximize_reach_greedy(budget2, costs2, reaches2)
    print(f"Greedy  → reach: {greedy_reach2}, users: {greedy_users2}")

    # Edge cases
    print("\n=== Edge Cases ===")

    # Budget = 0
    r, u = maximize_reach_exact(0, costs, reaches)
    print(f"Budget=0 → reach: {r}, users: {u}")

    # Single user, fits
    r, u = maximize_reach_exact(3, [3], [4])
    print(f"N=1 fits → reach: {r}, users: {u}")

    # Single user, too expensive
    r, u = maximize_reach_exact(2, [3], [4])
    print(f"N=1 too expensive → reach: {r}, users: {u}")

    # All users too expensive
    r, u = maximize_reach_exact(1, [5, 6, 7], [10, 20, 30])
    print(f"All too expensive → reach: {r}, users: {u}")
