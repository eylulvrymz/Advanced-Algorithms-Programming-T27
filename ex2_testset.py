# =============================================
# EDGE CASE TESTS – Exercise 2: Graph Coloring
# =============================================

from Exercise_2 import is_valid_labeling, assign_labels, find_min_labels

def run_test(test_name, graph, expected_min_k, test_labeling=None, expected_valid=None):
    print(f"\n--- {test_name} ---")

    # Test find_min_labels
    min_k, best_labeling = find_min_labels(graph)
    print(f"Minimum labels needed : {min_k}  (expected: {expected_min_k})")
    print(f"Labeling used         : {best_labeling}")
    assert min_k == expected_min_k, f"FAILED: got {min_k}, expected {expected_min_k}"
    print("find_min_labels       : PASSED")

    # Test is_valid_labeling if a labeling is provided
    if test_labeling is not None and expected_valid is not None:
        result = is_valid_labeling(test_labeling, graph)
        print(f"is_valid_labeling     : {result}  (expected: {expected_valid})")
        assert result == expected_valid, f"FAILED: got {result}, expected {expected_valid}"
        print("is_valid_labeling     : PASSED")


# -----------------------------------------------
# CASE 1: Empty graph (no edges)
# Every node can get the same label → needs only 1
# -----------------------------------------------
empty_graph = {
    "nodes": [0, 1, 2, 3],
    "edges": [],
    "neighbors": {0: [], 1: [], 2: [], 3: []}
}
run_test(
    "Case 1: Empty Graph (no edges)",
    empty_graph,
    expected_min_k=1,
    test_labeling=[0, 0, 0, 0],
    expected_valid=True
)


# -----------------------------------------------
# CASE 2: Single node (no edges, no neighbors)
# Only one node → needs only 1 label
# -----------------------------------------------
single_node_graph = {
    "nodes": [0],
    "edges": [],
    "neighbors": {0: []}
}
run_test(
    "Case 2: Single Node",
    single_node_graph,
    expected_min_k=1,
    test_labeling=[0],
    expected_valid=True
)


# -----------------------------------------------
# CASE 3: Fully connected graph K4
# Every node connects to every other → needs 4 labels
#   0 — 1
#   |\ /|
#   | X |
#   |/ \|
#   3 — 2
# -----------------------------------------------
complete_graph = {
    "nodes": [0, 1, 2, 3],
    "edges": [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)],
    "neighbors": {
        0: [1, 2, 3],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [0, 1, 2]
    }
}
run_test(
    "Case 3: Fully Connected Graph K4",
    complete_graph,
    expected_min_k=4,
    test_labeling=[0, 0, 1, 2],   # invalid: 0 and 1 are connected but share label 0
    expected_valid=False
)


# -----------------------------------------------
# CASE 4: Two nodes with one edge
# Simple as it gets → needs 2 labels
#   0 — 1
# -----------------------------------------------
two_node_graph = {
    "nodes": [0, 1],
    "edges": [(0, 1)],
    "neighbors": {0: [1], 1: [0]}
}
run_test(
    "Case 4: Two Nodes One Edge",
    two_node_graph,
    expected_min_k=2,
    test_labeling=[0, 1],
    expected_valid=True
)


# -----------------------------------------------
# CASE 5: Odd cycle (triangle)
# 3 nodes all connected in a loop → needs 3 labels
# (can't 2-color an odd cycle)
#   0 — 1
#    \ /
#     2
# -----------------------------------------------
triangle_graph = {
    "nodes": [0, 1, 2],
    "edges": [(0,1),(1,2),(0,2)],
    "neighbors": {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1]
    }
}
run_test(
    "Case 5: Odd Cycle (Triangle)",
    triangle_graph,
    expected_min_k=3,
    test_labeling=[0, 1, 0],   # invalid: 0 and 2 are connected but share label 0
    expected_valid=False
)


# -----------------------------------------------
# CASE 6: Even cycle (square)
# 4 nodes in a loop → needs only 2 labels
#   0 — 1
#   |   |
#   3 — 2
# -----------------------------------------------
square_graph = {
    "nodes": [0, 1, 2, 3],
    "edges": [(0,1),(1,2),(2,3),(3,0)],
    "neighbors": {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [2, 0]
    }
}
run_test(
    "Case 6: Even Cycle (Square)",
    square_graph,
    expected_min_k=2,
    test_labeling=[0, 1, 0, 1],
    expected_valid=True
)


# -----------------------------------------------
# CASE 7: Sparse graph (chain/path)
# Nodes in a straight line → needs only 2 labels
#   0 — 1 — 2 — 3 — 4
# -----------------------------------------------
path_graph = {
    "nodes": [0, 1, 2, 3, 4],
    "edges": [(0,1),(1,2),(2,3),(3,4)],
    "neighbors": {
        0: [1],
        1: [0, 2],
        2: [1, 3],
        3: [2, 4],
        4: [3]
    }
}
run_test(
    "Case 7: Sparse Graph (Path/Chain)",
    path_graph,
    expected_min_k=2,
    test_labeling=[0, 1, 0, 1, 0],
    expected_valid=True
)


print("\n\nAll edge case tests passed!")