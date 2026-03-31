from exercise2 import *

### Empty Tree ###
assert in_order_collect(None) == []
assert post_order_total_posts(None) == 0
assert find_most_popular_category(None) is None
assert pre_order_export(None) == ""
assert pre_order_serialize(None) == ""

### Single Node Tree ###
single = CategoryNode(1, "Tech", 50)
assert in_order_collect(single) == ["Tech"]
assert post_order_total_posts(single) == 50
assert find_most_popular_category(single).name == "Tech"
leaves = []
post_order_collect_leaves(single, leaves)
assert leaves == ["Tech"]

### Left-Skewed Tree ###
a = CategoryNode(1, "A", 10)
b = CategoryNode(2, "B", 20)
c = CategoryNode(3, "C", 30)
a.left = b
b.left = c
assert in_order_collect(a) == ["C", "B", "A"]
assert post_order_total_posts(a) == 60

### Right Skewed Tree ###
a = CategoryNode(1, "A", 10)
b = CategoryNode(2, "B", 20)
c = CategoryNode(3, "C", 30)
a.right = b
b.right = c
assert in_order_collect(a) == ["A", "B", "C"]
assert post_order_total_posts(a) == 60

### k out of bounds in in_order_find_kth ###
single = CategoryNode(1, "Tech", 50)
state = KthState()
assert in_order_find_kth(single, 99, state) is None  # k larger than tree size
state2 = KthState()
assert in_order_find_kth(single, 0, state2) is None  # k = 0, invalid

### All Nodes Have Equal Post Count ###
a = CategoryNode(1, "A", 100)
b = CategoryNode(2, "B", 100)
c = CategoryNode(3, "C", 100)
a.left = b
a.right = c
# Should return a valid node, not crash
result = find_most_popular_category(a)
assert result.post_count == 100
