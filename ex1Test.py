from exercise1_coverage import SocialGraph, is_valid_coverage, find_minimum_coverage, find_fast_coverage
# Helpers

def make_path_graph(n):
    """0 - 1 - 2 - ... - (n-1)"""
    g = SocialGraph(n)
    for i in range(n - 1):
        g.add_edge(i, i + 1)
    return g

def make_complete_graph(n):
    """Every pair of nodes connected."""
    g = SocialGraph(n)
    for i in range(n):
        for j in range(i + 1, n):
            g.add_edge(i, j)
    return g

def make_star_graph(n):
    """Node 0 connected to all others; no other edges."""
    g = SocialGraph(n)
    for i in range(1, n):
        g.add_edge(0, i)
    return g

def run_test(name, result, expected_size=None, valid_check_graph=None):
    size, selected = result
    status_parts = []

    if expected_size is not None:
        size_ok = size == expected_size
        status_parts.append(f"size={size} (expected {expected_size}) → {'OK' if size_ok else 'FAIL'}")

    if valid_check_graph is not None:
        valid = is_valid_coverage(selected, valid_check_graph)
        status_parts.append(f"valid coverage → {'OK' if valid else 'FAIL'}")

    print(f"  [{name}] selected={selected} | {' | '.join(status_parts)}")

# Tests: is_valid_coverage

def test_is_valid_coverage():
    print("\n=== is_valid_coverage ===")

    # Basic case star graph, center covers all
    g = make_star_graph(5)
    assert is_valid_coverage([0], g) == True
    print("  [star, center only] → OK")

    # Valid: all nodes selected
    g2 = make_path_graph(4)
    assert is_valid_coverage([0, 1, 2, 3], g2) == True
    print("  [path, all selected] → OK")

    # Invalid: middle node of path not covered
    g3 = make_path_graph(5)
    assert is_valid_coverage([0, 4], g3) == False
    print("  [path 0-1-2-3-4, only endpoints selected] → correctly False")

    # Edge case: empty graph, empty selection
    g4 = SocialGraph(0)
    assert is_valid_coverage([], g4) == True
    print("  [empty graph, empty selection] → OK")

    # Edge case: single node, selected
    g5 = SocialGraph(1)
    assert is_valid_coverage([0], g5) == True
    print("  [single node, selected] → OK")

    # Edge case: single node, not selected
    g6 = SocialGraph(1)
    assert is_valid_coverage([], g6) == False
    print("  [single node, not selected] → correctly False")

    # Fully connected graph: any single node covers all
    g7 = make_complete_graph(5)
    assert is_valid_coverage([2], g7) == True
    print("  [complete K5, single node] → OK")
  
# Tests: find_minimum_coverage


def test_find_minimum_coverage():
    print("\n=== find_minimum_coverage ===")

    # Empty graph
    g = SocialGraph(0)
    result = find_minimum_coverage(g)
    assert result == (0, []), f"Expected (0, []), got {result}"
    print("  [empty graph] → (0, []) OK")

    # Single node
    g = SocialGraph(1)
    run_test("single node", find_minimum_coverage(g), expected_size=1, valid_check_graph=g)

    # Single isolated node (no edges): must select itself
    g = SocialGraph(3)  # 3 isolated nodes
    result = find_minimum_coverage(g)
    assert is_valid_coverage(result[1], g)
    assert result[0] == 3  # each isolated node needs to be selected
    print(f"  [3 isolated nodes] size={result[0]} (expected 3) → OK")

    # Path 0-1-2-3: minimum dominating set size = 2 (e.g. {1, 3} or {0, 2})
    g = make_path_graph(4)
    run_test("path n=4", find_minimum_coverage(g), expected_size=2, valid_check_graph=g)

    # Star graph: center alone dominates all → size = 1
    g = make_star_graph(6)
    run_test("star n=6", find_minimum_coverage(g), expected_size=1, valid_check_graph=g)

    # Complete graph K4: any single node covers all → size = 1
    g = make_complete_graph(4)
    run_test("complete K4", find_minimum_coverage(g), expected_size=1, valid_check_graph=g)

    # Triangle 0-1-2: any one node covers all → size = 1
    g = SocialGraph(3)
    g.add_edge(0, 1); g.add_edge(1, 2); g.add_edge(0, 2)
    run_test("triangle", find_minimum_coverage(g), expected_size=1, valid_check_graph=g)

    # Path n=5: minimum = 2 ({1, 3} covers all)
    g = make_path_graph(5)
    run_test("path n=5", find_minimum_coverage(g), expected_size=2, valid_check_graph=g)

    # Cycle 0-1-2-3-4-0: minimum = 2
    g = SocialGraph(5)
    for i in range(5):
        g.add_edge(i, (i + 1) % 5)
    run_test("cycle n=5", find_minimum_coverage(g), expected_size=2, valid_check_graph=g)

# Tests: find_fast_coverage

def test_find_fast_coverage():
    print("\n=== find_fast_coverage ===")

    # Empty graph
    g = SocialGraph(0)
    result = find_fast_coverage(g)
    assert result == (0, [])
    print("  [empty graph] → (0, []) OK")

    # Single node
    g = SocialGraph(1)
    result = find_fast_coverage(g)
    assert is_valid_coverage(result[1], g)
    print(f"  [single node] size={result[0]} → OK")

    # Star: greedy should pick the center immediately (highest coverage)
    g = make_star_graph(7)
    result = find_fast_coverage(g)
    assert is_valid_coverage(result[1], g)
    print(f"  [star n=7] size={result[0]} (expected 1) → {'OK' if result[0] == 1 else 'FAIL'}")

    # Complete graph: any one node covers all
    g = make_complete_graph(5)
    result = find_fast_coverage(g)
    assert is_valid_coverage(result[1], g)
    print(f"  [complete K5] size={result[0]} (expected 1) → {'OK' if result[0] == 1 else 'FAIL'}")

    # Path n=4: greedy should find size 2
    g = make_path_graph(4)
    result = find_fast_coverage(g)
    assert is_valid_coverage(result[1], g)
    print(f"  [path n=4] size={result[0]} (expected 2) → {'OK' if result[0] == 2 else 'check manually'}")

    # 3 isolated nodes: greedy must select all 3
    g = SocialGraph(3)
    result = find_fast_coverage(g)
    assert is_valid_coverage(result[1], g)
    print(f"  [3 isolated nodes] size={result[0]} (expected 3) → {'OK' if result[0] == 3 else 'FAIL'}")

    # Larger sparse graph: just verify coverage is valid
    g = make_path_graph(15)
    result = find_fast_coverage(g)
    assert is_valid_coverage(result[1], g)
    print(f"  [path n=15] size={result[0]} → valid coverage OK")

# Greedy vs Exact Comparison (small graphs)


def test_greedy_vs_exact():
    print("\n=== Greedy vs Exact Comparison ===")

    test_graphs = {
        "path n=4":     make_path_graph(4),
        "path n=6":     make_path_graph(6),
        "star n=6":     make_star_graph(6),
        "complete K5":  make_complete_graph(5),
        "cycle n=6":    _make_cycle(6),
    }

    for name, g in test_graphs.items():
        exact_size, _ = find_minimum_coverage(g)
        greedy_size, greedy_sel = find_fast_coverage(g)
        valid = is_valid_coverage(greedy_sel, g)
        ratio = greedy_size / exact_size if exact_size > 0 else 1
        print(f"  [{name}] exact={exact_size}, greedy={greedy_size}, valid={valid}, ratio={ratio:.2f}")

def _make_cycle(n):
    g = SocialGraph(n)
    for i in range(n):
        g.add_edge(i, (i + 1) % n)
    return g

# Running All


if __name__ == "__main__":
    print("=" * 50)
    print("LAB 9 – Exercise 1 Test Suite")
    print("=" * 50)

    test_is_valid_coverage()
    test_find_minimum_coverage()
    test_find_fast_coverage()
    test_greedy_vs_exact()

    print("\n" + "=" * 50)
    print("All tests completed.")
    print("=" * 50)
