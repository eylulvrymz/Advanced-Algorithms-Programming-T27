import sys
sys.path.insert(0, ".")          # allow import from same directory / outputs folder
from ex1_event_invitation import (
    is_valid_invitation,
    find_max_invitations_exact,
    find_max_invitations_greedy,
)

PASS = "\033[92mPASS\033[0m"
FAIL = "\033[91mFAIL\033[0m"

def assert_eq(label, got, expected):
    ok = got == expected
    status = PASS if ok else FAIL
    print(f"  [{status}] {label}")
    if not ok:
        print(f"         expected: {expected}")
        print(f"         got     : {got}")
    return ok


def assert_true(label, condition):
    status = PASS if condition else FAIL
    print(f"  [{status}] {label}")
    return condition


def section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


results = []   # collect (label, passed) for summary


def run(label, condition):
    results.append((label, condition))

# EDGE CASE 1 – Empty graph (no nodes, no edges)
section("Edge Case 1: Empty graph (no nodes, no edges)")
empty_graph: dict = {}

r = assert_true("is_valid_invitation on empty graph returns True",
                is_valid_invitation([], empty_graph))
run("EC1-valid-empty", r)

size, lst = find_max_invitations_exact(empty_graph)
r = assert_eq("exact MIS on empty graph → size 0", size, 0)
run("EC1-exact-size", r)
r = assert_eq("exact MIS on empty graph → empty list", lst, [])
run("EC1-exact-list", r)

size, lst = find_max_invitations_greedy(empty_graph)
r = assert_eq("greedy MIS on empty graph → size 0", size, 0)
run("EC1-greedy-size", r)

# EDGE CASE 2 – Single node
section("Edge Case 2: Single node, no edges")
single_graph = {0: []}

size, lst = find_max_invitations_exact(single_graph)
r = assert_eq("exact: single node → size 1", size, 1)
run("EC2-exact-size", r)
r = assert_eq("exact: single node → [0]", lst, [0])
run("EC2-exact-list", r)

size, lst = find_max_invitations_greedy(single_graph)
r = assert_eq("greedy: single node → size 1", size, 1)
run("EC2-greedy-size", r)


# EDGE CASE 3 – Fully connected graph (complete graph K_5)
# Everyone conflicts with everyone else → MIS = 1

section("Edge Case 3: Complete graph K_5 (every pair conflicts)")
k5 = {
    0: [1, 2, 3, 4],
    1: [0, 2, 3, 4],
    2: [0, 1, 3, 4],
    3: [0, 1, 2, 4],
    4: [0, 1, 2, 3],
}

size, lst = find_max_invitations_exact(k5)
r = assert_eq("exact K_5: MIS size = 1", size, 1)
run("EC3-exact-size", r)
r = assert_true("exact K_5: result is valid", is_valid_invitation(lst, k5))
run("EC3-exact-valid", r)

size, lst = find_max_invitations_greedy(k5)
r = assert_eq("greedy K_5: MIS size = 1", size, 1)
run("EC3-greedy-size", r)
r = assert_true("greedy K_5: result is valid", is_valid_invitation(lst, k5))
run("EC3-greedy-valid", r)


# EDGE CASE 4 – No edges (independent graph on 5 nodes)
# MIS = all nodes → size 5

section("Edge Case 4: No-edge graph (5 isolated nodes)")
no_edge = {0: [], 1: [], 2: [], 3: [], 4: []}

size, lst = find_max_invitations_exact(no_edge)
r = assert_eq("exact no-edge: size = 5", size, 5)
run("EC4-exact-size", r)
r = assert_true("exact no-edge: all nodes valid", is_valid_invitation(lst, no_edge))
run("EC4-exact-valid", r)

size, lst = find_max_invitations_greedy(no_edge)
r = assert_eq("greedy no-edge: size = 5", size, 5)
run("EC4-greedy-size", r)


# NORMAL CASE 1 – Simple path graph: 0-1-2-3-4
# MIS = {0, 2, 4} → size 3

section("Normal Case 1: Path graph 0-1-2-3-4")
path = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2, 4],
    4: [3],
}

size, lst = find_max_invitations_exact(path)
r = assert_eq("exact path: MIS size = 3", size, 3)
run("NC1-exact-size", r)
r = assert_true("exact path: result valid", is_valid_invitation(lst, path))
run("NC1-exact-valid", r)

size, lst = find_max_invitations_greedy(path)
r = assert_true("greedy path: size ≥ 2 (reasonable)", size >= 2)
run("NC1-greedy-reasonable", r)
r = assert_true("greedy path: result valid", is_valid_invitation(lst, path))
run("NC1-greedy-valid", r)


# NORMAL CASE 2 – Cycle C_6 (even cycle)
# MIS = {0,2,4} or {1,3,5} → size 3

section("Normal Case 2: Cycle C_6 (even cycle)")
c6 = {
    0: [1, 5],
    1: [0, 2],
    2: [1, 3],
    3: [2, 4],
    4: [3, 5],
    5: [4, 0],
}

size, lst = find_max_invitations_exact(c6)
r = assert_eq("exact C_6: MIS size = 3", size, 3)
run("NC2-exact-size", r)
r = assert_true("exact C_6: result valid", is_valid_invitation(lst, c6))
run("NC2-exact-valid", r)

size, lst = find_max_invitations_greedy(c6)
r = assert_true("greedy C_6: size ≥ 2", size >= 2)
run("NC2-greedy-reasonable", r)
r = assert_true("greedy C_6: result valid", is_valid_invitation(lst, c6))
run("NC2-greedy-valid", r)



# NORMAL CASE 3 – Star graph (hub + 4 leaves)
# MIS = all 4 leaves → size 4

section("Normal Case 3: Star graph K_{1,4}")
star = {
    0: [1, 2, 3, 4],   # hub
    1: [0],
    2: [0],
    3: [0],
    4: [0],
}

size, lst = find_max_invitations_exact(star)
r = assert_eq("exact star: MIS size = 4", size, 4)
run("NC3-exact-size", r)
r = assert_true("exact star: hub not in result", 0 not in lst)
run("NC3-exact-no-hub", r)
r = assert_true("exact star: result valid", is_valid_invitation(lst, star))
run("NC3-exact-valid", r)

size, lst = find_max_invitations_greedy(star)
r = assert_eq("greedy star: MIS size = 4", size, 4)
run("NC3-greedy-size", r)



# NORMAL CASE 4 – Greedy counterexample
# Graph: 0-1, 0-2, 1-3, 2-3, 3-4
# Degrees: 0→2, 1→2, 2→2, 3→3, 4→1
# Greedy (min-degree) picks node 4 first, then works inward.
# Exact MIS = {1, 2, 4} → size 3.


section("Normal Case 4: Path-with-branch (greedy counterexample structure)")
branch_graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2, 4],
    4: [3],
}

size, lst = find_max_invitations_exact(branch_graph)
r = assert_eq("exact branch: MIS size = 3", size, 3)
run("NC4-exact-size", r)
r = assert_true("exact branch: valid", is_valid_invitation(lst, branch_graph))
run("NC4-exact-valid", r)

greedy_size, greedy_lst = find_max_invitations_greedy(branch_graph)
r = assert_true("greedy branch: valid", is_valid_invitation(greedy_lst, branch_graph))
run("NC4-greedy-valid", r)
r = assert_true("greedy branch: size ≥ 2 (may be suboptimal)",
                greedy_size >= 2)
run("NC4-greedy-reasonable", r)
print(f"         Greedy size={greedy_size} (optimal=3, gap={3 - greedy_size})")


# IS_VALID_INVITATION – dedicated unit tests

section("Unit tests: is_valid_invitation")

graph_v = {0: [1], 1: [0, 2], 2: [1]}

r = assert_true("valid: {0, 2} no shared edge", is_valid_invitation([0, 2], graph_v))
run("V1", r)

r = assert_true("invalid: {0, 1} share edge → False",
                not is_valid_invitation([0, 1], graph_v))
run("V2", r)

r = assert_true("valid: single node always valid", is_valid_invitation([1], graph_v))
run("V3", r)

r = assert_true("valid: empty list → True", is_valid_invitation([], graph_v))
run("V4", r)

r = assert_true("invalid: {1, 2} share edge → False",
                not is_valid_invitation([1, 2], graph_v))
run("V5", r)


# STRESS / SCALABILITY – slightly larger graph
section("Scalability: Path graph with N=20 nodes")
n = 20
path20 = {i: [] for i in range(n)}
for i in range(n - 1):
    path20[i].append(i + 1)
    path20[i + 1].append(i)

size, lst = find_max_invitations_exact(path20)
r = assert_eq("exact path-20: size = 10", size, 10)
run("SCALE-exact", r)
r = assert_true("exact path-20: valid", is_valid_invitation(lst, path20))
run("SCALE-exact-valid", r)

size, lst = find_max_invitations_greedy(path20)
r = assert_true("greedy path-20: size ≥ 9", size >= 9)
run("SCALE-greedy", r)
r = assert_true("greedy path-20: valid", is_valid_invitation(lst, path20))
run("SCALE-greedy-valid", r)



# SUMMARY

section("SUMMARY")
passed = sum(1 for _, p in results if p)
total = len(results)
print(f"\n  {passed}/{total} tests passed\n")
if passed == total:
    print(f"  {PASS} All tests passed!")
else:
    failed = [lbl for lbl, p in results if not p]
    print(f"  {FAIL} Failed: {failed}")
