def is_valid_invitation(invited: list[int], graph: dict[int, list[int]]) -> bool:
    invited_set = set(invited)
    for user in invited:
        for neighbor in graph.get(user, []):
            if neighbor in invited_set:
                return False
    return True

# Exact solution – Backtracking with pruning

def find_max_invitations_exact(graph: dict[int, list[int]]) -> tuple[int, list[int]]:
    nodes = list(graph.keys())
    n = len(nodes)

    # Global best tracked as a mutable container so nested function can write to it
    best = [0, []]  # [size, list_of_users]

    def backtrack(index: int, current: list[int], candidates: set[int]):
        # Update best if current solution is better
        if len(current) > best[0]:
            best[0] = len(current)
            best[1] = current[:]

        # Pruning
        remaining = len([nd for nd in nodes[index:] if nd in candidates])
        if len(current) + remaining <= best[0]:
            return

        for i in range(index, n):
            node = nodes[i]
            if node not in candidates:
                continue

            # Include `node` – remove it and its neighbors from candidates
            new_candidates = candidates - {node} - set(graph.get(node, []))
            current.append(node)
            backtrack(i + 1, current, new_candidates)
            current.pop()

    backtrack(0, [], set(nodes))
    return best[0], best[1]

# Greedy heuristic
def find_max_invitations_greedy(graph: dict[int, list[int]]) -> tuple[int, list[int]]:
    remaining = {node: set(neighbors) for node, neighbors in graph.items()}
    invited = []

    while remaining:
        # Pick node with minimum degree among remaining nodes
        node = min(remaining, key=lambda u: len(remaining[u]))
        invited.append(node)

        # Remove node and all its neighbors from the remaining graph
        neighbors_to_remove = remaining.pop(node)  # removes `node` itself
        for neighbor in neighbors_to_remove:
            if neighbor in remaining:
                # Also remove `node` from that neighbor's adjacency list
                remaining[neighbor].discard(node)
                # Remove the neighbor entirely (it is adjacent to chosen node)
                neighbors_of_neighbor = remaining.pop(neighbor)
                # Clean up back-references from neighbors-of-neighbor
                for nn in neighbors_of_neighbor:
                    if nn in remaining:
                        remaining[nn].discard(neighbor)

    return len(invited), invited

# Comparison utility

def compare_solutions(graph: dict[int, list[int]]) -> None:
    """Run both methods on the same graph and print a comparison."""
    exact_size, exact_list = find_max_invitations_exact(graph)
    greedy_size, greedy_list = find_max_invitations_greedy(graph)

    print(f"  Exact  → size={exact_size}, invited={sorted(exact_list)}")
    print(f"  Greedy → size={greedy_size}, invited={sorted(greedy_list)}")
    print(f"  Valid (exact) : {is_valid_invitation(exact_list, graph)}")
    print(f"  Valid (greedy): {is_valid_invitation(greedy_list, graph)}")
    gap = exact_size - greedy_size
    print(f"  Optimality gap: {gap} node(s)\n")
