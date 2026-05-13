def is_valid_labeling(labeling, graph):
    for (u, v) in graph["edges"]:
        if labeling[u] == labeling[v]:
            return False
    return True


def assign_labels(k, graph):
    N = len(graph["nodes"])
    labeling = [-1] * N  # -1 means uncolored

    def backtrack(node):
        if node == N:
            return True  # all nodes colored

        for color in range(k):
            valid = True
            for v in graph["neighbors"][node]:
                if labeling[v] == color:
                    valid = False
                    break

            if valid:
                labeling[node] = color
                if backtrack(node + 1):
                    return True
                labeling[node] = -1  # undo (backtrack)

        return False  # no color worked

    success = backtrack(0)
    return (success, labeling)


def find_min_labels(graph):
    k = 1
    while k <= len(graph["nodes"]):
        success, labeling = assign_labels(k, graph)
        if success:
            return (k, labeling)
        k += 1

    return (-1, [])  # should never reach here for a valid graph


# ------- Test -------

graph = {
    "nodes": [0, 1, 2, 3],
    "edges": [(0, 1), (1, 2), (2, 3), (3, 0)],
    "neighbors": {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [2, 0]
    }
}

# Test is_valid_labeling
labeling = [0, 1, 0, 1]
print("Valid labeling?", is_valid_labeling(labeling, graph))  # True

bad_labeling = [0, 0, 1, 1]
print("Bad labeling?", is_valid_labeling(bad_labeling, graph))  # False

# Test assign_labels
success, result = assign_labels(2, graph)
print("assign_labels(k=2):", success, result)  # True, [0, 1, 0, 1]

# Test find_min_labels
min_k, best_labeling = find_min_labels(graph)
print("Minimum labels needed:", min_k)       # 2
print("Labeling used:", best_labeling)        # [0, 1, 0, 1]