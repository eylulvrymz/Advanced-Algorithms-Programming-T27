# ============================================================
#  LAB 5 – Exercise 2: Tree Traversals for Content Processing
# ============================================================

class CategoryNode:
    def __init__(self, category_id, name, post_count):
        self.category_id = category_id
        self.name        = name
        self.post_count  = post_count
        self.left        = None
        self.right       = None


# ─────────────────────────────────────────
#  PART A – In-order Traversals
# ─────────────────────────────────────────

def in_order_collect(node):
    """Return a list of category names in in-order sequence."""
    if node is None:
        return []

    left_result  = in_order_collect(node.left)
    right_result = in_order_collect(node.right)

    return left_result + [node.name] + right_result


class AccumulateState:
    def __init__(self):
        self.running_total = 0

def in_order_accumulate_posts(node, state):
    """Accumulate post counts in in-order, storing running total in state."""
    if node is None:
        return

    in_order_accumulate_posts(node.left, state)
    state.running_total += node.post_count
    in_order_accumulate_posts(node.right, state)


class KthState:
    def __init__(self):
        self.counter = 0
        self.found   = False

def in_order_find_kth(node, k, state):
    """Find the k-th node (1-indexed) in in-order sequence."""
    if node is None or state.found:
        return None

    # Search left subtree first
    result = in_order_find_kth(node.left, k, state)
    if result is not None:
        return result

    # Process current node
    state.counter += 1
    if state.counter == k:
        state.found = True
        return node

    # Search right subtree
    return in_order_find_kth(node.right, k, state)


# ─────────────────────────────────────────
#  PART B – Pre-order Traversals
# ─────────────────────────────────────────

def pre_order_export(node, depth=0):
    """Return a formatted, indented string of the tree (root → left → right)."""
    if node is None:
        return ""

    indent        = "  " * depth
    line          = f"{indent}{node.name}({node.post_count})"
    left_content  = pre_order_export(node.left,  depth + 1)
    right_content = pre_order_export(node.right, depth + 1)

    result = line + "\n"
    if left_content:
        result += left_content
    if right_content:
        result += right_content
    return result


def pre_order_copy(node):
    """Create a deep copy of the tree using pre-order traversal."""
    if node is None:
        return None

    new_node       = CategoryNode(node.category_id, node.name, node.post_count)
    new_node.left  = pre_order_copy(node.left)
    new_node.right = pre_order_copy(node.right)

    return new_node


def pre_order_serialize(node):
    """Serialize tree to a pipe-separated string (pre-order)."""
    if node is None:
        return ""

    # Serialize current node first (root before children)
    result = f"{node.name}({node.post_count})"

    left_str  = pre_order_serialize(node.left)
    right_str = pre_order_serialize(node.right)

    if left_str:
        result = result + " | " + left_str

    if right_str:
        result = result + " | " + right_str

    return result


# ─────────────────────────────────────────
#  PART C – Post-order Traversals
# ─────────────────────────────────────────

def post_order_total_posts(node):
    """Compute total posts in a category including all its subcategories."""
    if node is None:
        return 0

    left_total  = post_order_total_posts(node.left)
    right_total = post_order_total_posts(node.right)

    return node.post_count + left_total + right_total


def post_order_collect_leaves(node, leaf_list):
    """Collect all leaf category names (post-order)."""
    if node is None:
        return

    post_order_collect_leaves(node.left,  leaf_list)
    post_order_collect_leaves(node.right, leaf_list)

    if node.left is None and node.right is None:
        leaf_list.append(node.name)


class DepthState:
    def __init__(self):
        self.total_depth = 0
        self.leaf_count  = 0

def post_order_average_depth(node, current_depth, state):
    """Calculate average depth of all leaf nodes (post-order)."""
    if node is None:
        return

    post_order_average_depth(node.left,  current_depth + 1, state)
    post_order_average_depth(node.right, current_depth + 1, state)

    if node.left is None and node.right is None:
        state.total_depth += current_depth
        state.leaf_count  += 1

# Caller computes: average = state.total_depth / state.leaf_count


def find_most_popular_category(node):
    """Return the node with the highest post count."""
    if node is None:
        return None

    max_node = node

    left_max = find_most_popular_category(node.left)
    if left_max is not None and left_max.post_count > max_node.post_count:
        max_node = left_max

    right_max = find_most_popular_category(node.right)
    if right_max is not None and right_max.post_count > max_node.post_count:
        max_node = right_max

    return max_node


# ─────────────────────────────────────────
#  Helper – build the sample tree
# ─────────────────────────────────────────
#
#               Technology(150)
#              /               \
#      Programming(85)       Design(65)
#         /       \           /      \
#      Python(42) Java(30) UI/UX(38) Graphics(22)
#       /    \
#  Django(18) Flask(12)

def build_sample_tree():
    technology  = CategoryNode(1, "Technology",  150)
    programming = CategoryNode(2, "Programming",  85)
    design      = CategoryNode(3, "Design",       65)
    python      = CategoryNode(4, "Python",       42)
    java        = CategoryNode(5, "Java",         30)
    uiux        = CategoryNode(6, "UI/UX",        38)
    graphics    = CategoryNode(7, "Graphics",     22)
    django      = CategoryNode(8, "Django",       18)
    flask       = CategoryNode(9, "Flask",        12)

    technology.left   = programming
    technology.right  = design
    programming.left  = python
    programming.right = java
    design.left       = uiux
    design.right      = graphics
    python.left       = django
    python.right      = flask

    return technology


# ─────────────────────────────────────────
#  Demo
# ─────────────────────────────────────────

if __name__ == "__main__":
    root = build_sample_tree()

    print("=" * 55)
    print("PART A – In-order Traversals")
    print("=" * 55)

    names = in_order_collect(root)
    print("In-order collect:")
    print(" → ".join(names))

    state = AccumulateState()
    in_order_accumulate_posts(root, state)
    print(f"\nIn-order accumulated posts: {state.running_total}")

    kth_state = KthState()
    k = 3
    result = in_order_find_kth(root, k, kth_state)
    print(f"\n{k}-rd node in in-order: {result.name if result else 'Not found'}")

    print("\n" + "=" * 55)
    print("PART B – Pre-order Traversals")
    print("=" * 55)

    print("Pre-order export (formatted):")
    print(pre_order_export(root))

    copy_root = pre_order_copy(root)
    print(f"Pre-order copy root name: {copy_root.name} (deep copy ✓)")

    serialized = pre_order_serialize(root)
    print(f"\nPre-order serialized:\n{serialized}")

    print("\n" + "=" * 55)
    print("PART C – Post-order Traversals")
    print("=" * 55)

    total = post_order_total_posts(root)
    print(f"Total posts (entire tree): {total}")

    leaves = []
    post_order_collect_leaves(root, leaves)
    print(f"\nLeaf categories: {leaves}")

    depth_state = DepthState()
    post_order_average_depth(root, 0, depth_state)
    avg = depth_state.total_depth / depth_state.leaf_count
    print(f"\nAverage leaf depth: {avg:.2f}")

    popular = find_most_popular_category(root)
    print(f"\nMost popular category: {popular.name} ({popular.post_count} posts)")
