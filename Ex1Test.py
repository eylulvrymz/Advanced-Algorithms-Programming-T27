from Exercise1 import UserBST

def run_tests():
    bst = UserBST()

    # 1. Core Operations: Insert, Find, and Inorder
    print("Testing Core Ops...")
    for uid, name, friends in [(10, "A", [5, 15]), (5, "B", [10]), (15, "C", [10, 20]), (20, "D", [15])]:
        bst.insert(uid, name, friends)

    assert bst.find(10).name == "A"
    assert bst.find(99) is None
    assert bst.inorder_traversal() == [5, 10, 15, 20]
    # Verify duplicates don't corrupt tree
    bst.insert(10, "Duplicate", [])
    assert bst.find(10).name == "A"

    # 2. Friend-of-Friend (FoF) Suggestions
    print("Testing FoF Logic...")
    # User 10 is friends with 5 and 15.
    # 15 is friends with 20. So 20 is a FoF for 10.
    suggestions = bst.suggest_friends(10)
    uids = [s[0] for s in suggestions]
    assert 20 in uids
    assert 10 not in uids and 5 not in uids  # Should not suggest self or direct friends

    # 3. BST Analytics (Height & Balance)
    print("Testing Analytics...")
    assert bst.get_height() == 2
    assert bst.is_balanced() is True
    assert bst.get_leaf_count() == 2  # Nodes 5 and 20 are leaves

    # 4. Deletion: The Two-Child Case
    print("Testing Deletion...")
    bst.delete(15)  # Node with child 20
    assert bst.find(15) is None
    assert bst.find(20) is not None  # Child should be promoted

    # 5. Worst-Case Scenario (Skewed Tree)
    print("Testing Skewed Tree...")
    skewed = UserBST()
    for i in range(1, 6):
        skewed.insert(i, str(i), [])
    assert skewed.get_height() == 4  # Sequential insertion creates a chain
    assert skewed.is_balanced() is False

    print("All Exercise 1 tests passed!")

if __name__ == "__main__":
    run_tests()
