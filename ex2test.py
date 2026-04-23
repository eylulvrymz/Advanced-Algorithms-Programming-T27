import time
import pytest
from Exercise2 import TrendingHeap



# =========================================================================== #
#  Helpers                                                                     #
# =========================================================================== #

def make_heap(*entries):
    """
    Shorthand: make_heap((post_id, likes), ...) -> TrendingHeap
    Timestamp is set to current time automatically.
    """
    h = TrendingHeap()
    for post_id, likes in entries:
        h.push(post_id, likes, time.time())
    return h


# =========================================================================== #
#  1. Empty heap edge cases                                                    #
# =========================================================================== #

class TestEmptyHeap:

    def test_pop_max_on_empty_returns_none(self):
        # Popping from an empty heap should not crash, just return None
        h = TrendingHeap()
        assert h.pop_max() is None

    def test_peek_max_on_empty_returns_none(self):
        h = TrendingHeap()
        assert h.peek_max() is None

    def test_get_top_k_on_empty_returns_empty_list(self):
        h = TrendingHeap()
        result = h.get_top_k(5)
        assert result == []

    def test_is_valid_heap_on_empty_returns_true(self):
        # An empty heap trivially satisfies the heap property
        h = TrendingHeap()
        assert h.is_valid_heap() is True

    def test_get_height_on_empty_returns_zero(self):
        h = TrendingHeap()
        assert h.get_height() == 0

    def test_size_on_empty_is_zero(self):
        h = TrendingHeap()
        assert h.size() == 0

    def test_update_likes_on_empty_does_not_crash(self):
        # post_id not in pos -> should silently return
        h = TrendingHeap()
        h.update_likes(999, 500, time.time())   # must not raise
        assert h.size() == 0

    def test_get_level_order_on_empty_returns_empty(self):
        h = TrendingHeap()
        assert h.get_level_order() == []


# =========================================================================== #
#  2. Single-element heap                                                      #
# =========================================================================== #

class TestSingleElement:

    def test_push_then_peek(self):
        h = make_heap((1, 42))
        entry = h.peek_max()
        assert entry["post_id"] == 1
        assert entry["likes"] == 42

    def test_push_then_pop(self):
        h = make_heap((1, 42))
        entry = h.pop_max()
        assert entry["post_id"] == 1
        assert h.size() == 0

    def test_heap_valid_after_single_push(self):
        h = make_heap((7, 100))
        assert h.is_valid_heap() is True

    def test_height_is_one_for_single_element(self):
        h = make_heap((1, 10))
        assert h.get_height() == 1

    def test_update_to_higher_value(self):
        h = make_heap((1, 50))
        h.update_likes(1, 200, time.time())
        assert h.peek_max()["likes"] == 200
        assert h.is_valid_heap()

    def test_update_to_lower_value(self):
        h = make_heap((1, 50))
        h.update_likes(1, 10, time.time())
        assert h.peek_max()["likes"] == 10
        assert h.is_valid_heap()

    def test_update_to_same_value(self):
        h = make_heap((1, 50))
        h.update_likes(1, 50, time.time())
        assert h.peek_max()["likes"] == 50
        assert h.is_valid_heap()


# =========================================================================== #
#  3. get_top_k – k larger than heap size (mentioned explicitly in the lab)   #
# =========================================================================== #

class TestGetTopKBoundaries:

    def test_k_larger_than_heap_returns_all(self):
        # Lab edge case: get_top_k(1000) when only 50 posts exist
        h = TrendingHeap()
        for pid in range(1, 51):                 # 50 posts
            h.push(pid, pid * 10, time.time())

        result = h.get_top_k(1000)
        assert len(result) == 50                 # must return only 50

    def test_k_equals_heap_size(self):
        h = make_heap((1, 10), (2, 20), (3, 30))
        result = h.get_top_k(3)
        assert len(result) == 3

    def test_k_zero_returns_empty(self):
        h = make_heap((1, 100), (2, 200))
        result = h.get_top_k(0)
        assert result == []

    def test_top_k_order_is_descending(self):
        h = make_heap((1, 100), (2, 500), (3, 300), (4, 200), (5, 400))
        result = h.get_top_k(5)
        likes = [e["likes"] for e in result]
        assert likes == sorted(likes, reverse=True)

    def test_get_top_k_does_not_modify_heap(self):
        # get_top_k must be non-destructive
        h = make_heap((1, 100), (2, 500), (3, 300))
        size_before = h.size()
        h.get_top_k(3)
        assert h.size() == size_before
        assert h.peek_max()["likes"] == 500

    def test_k_one_returns_only_max(self):
        h = make_heap((1, 10), (2, 999), (3, 42))
        result = h.get_top_k(1)
        assert len(result) == 1
        assert result[0]["likes"] == 999


# =========================================================================== #
#  4. update_likes – non-existent post_id                                     #
# =========================================================================== #

class TestUpdateLikesEdgeCases:

    def test_update_nonexistent_post_is_ignored(self):
        h = make_heap((1, 100), (2, 200))
        h.update_likes(999, 9999, time.time())  # post 999 does not exist
        assert h.size() == 2
        assert h.is_valid_heap()

    def test_update_to_zero_likes(self):
        h = make_heap((1, 500), (2, 300), (3, 100))
        h.update_likes(1, 0, time.time())       # drop top post to 0
        assert h.peek_max()["likes"] == 300
        assert h.is_valid_heap()

    def test_update_makes_new_max(self):
        h = make_heap((1, 100), (2, 200), (3, 50))
        h.update_likes(3, 9999, time.time())    # post 3 becomes new max
        assert h.peek_max()["post_id"] == 3
        assert h.is_valid_heap()

    def test_update_preserves_pos_consistency(self):
        # After update, pos[post_id] must still point to the correct index
        h = make_heap((1, 100), (2, 200), (3, 300), (4, 400))
        h.update_likes(2, 9000, time.time())
        for pid, idx in h.pos.items():
            assert h.heap[idx]["post_id"] == pid


# =========================================================================== #
#  5. Heap property – is_valid_heap                                            #
# =========================================================================== #

class TestHeapValidity:

    def test_valid_after_many_pushes(self):
        h = TrendingHeap()
        for i in range(200):
            h.push(i, i * 3, time.time())
        assert h.is_valid_heap()

    def test_valid_after_many_pops(self):
        h = TrendingHeap()
        for i in range(50):
            h.push(i, i * 7, time.time())
        for _ in range(25):
            h.pop_max()
        assert h.is_valid_heap()

    def test_valid_after_mixed_operations(self):
        h = TrendingHeap()
        for i in range(30):
            h.push(i, i * 5, time.time())
        for i in range(0, 30, 3):
            h.update_likes(i, i * 100, time.time())
        for _ in range(10):
            h.pop_max()
        assert h.is_valid_heap()

    def test_valid_after_decreasing_insertions(self):
        # Inserting in decreasing order stresses heapify_up less
        h = TrendingHeap()
        for i in range(100, 0, -1):
            h.push(i, i, time.time())
        assert h.is_valid_heap()
        assert h.peek_max()["likes"] == 100

    def test_valid_after_increasing_insertions(self):
        # Each push must bubble all the way up
        h = TrendingHeap()
        for i in range(1, 101):
            h.push(i, i, time.time())
        assert h.is_valid_heap()
        assert h.peek_max()["likes"] == 100


# =========================================================================== #
#  6. Duplicate likes                                                          #
# =========================================================================== #

class TestDuplicateLikes:

    def test_all_same_likes_heap_is_valid(self):
        h = TrendingHeap()
        for pid in range(1, 20):
            h.push(pid, 100, time.time())       # all have 100 likes
        assert h.is_valid_heap()

    def test_pop_all_same_likes(self):
        h = TrendingHeap()
        for pid in range(1, 6):
            h.push(pid, 50, time.time())
        popped = [h.pop_max()["likes"] for _ in range(5)]
        assert popped == [50, 50, 50, 50, 50]
        assert h.size() == 0

    def test_update_creates_duplicate_at_top(self):
        h = make_heap((1, 300), (2, 200), (3, 100))
        h.update_likes(3, 300, time.time())     # now two posts with 300 likes
        assert h.is_valid_heap()
        assert h.peek_max()["likes"] == 300


# =========================================================================== #
#  7. Pop until empty                                                          #
# =========================================================================== #

class TestPopUntilEmpty:

    def test_pop_all_elements_leaves_empty_heap(self):
        h = make_heap((1, 10), (2, 20), (3, 30), (4, 40), (5, 50))
        results = []
        while h.size() > 0:
            results.append(h.pop_max())
        assert h.size() == 0
        assert len(results) == 5

    def test_pop_order_is_descending(self):
        h = make_heap((1, 15), (2, 95), (3, 40), (4, 70), (5, 5))
        likes = []
        while h.size() > 0:
            likes.append(h.pop_max()["likes"])
        assert likes == sorted(likes, reverse=True)

    def test_pop_after_empty_still_returns_none(self):
        h = make_heap((1, 10))
        h.pop_max()
        assert h.pop_max() is None             # second pop on now-empty heap
        assert h.pop_max() is None             # third pop

    def test_pos_is_empty_after_popping_all(self):
        h = make_heap((1, 10), (2, 20))
        h.pop_max()
        h.pop_max()
        assert h.pos == {}


# =========================================================================== #
#  8. Analytics – height and level order                                       #
# =========================================================================== #

class TestAnalytics:

    def test_height_grows_logarithmically(self):
        import math
        h = TrendingHeap()
        for i in range(1, 17):                 # 16 elements -> height 4
            h.push(i, i, time.time())
        assert h.get_height() == math.floor(math.log2(16)) + 1

    def test_level_order_first_element_is_max(self):
        h = make_heap((1, 10), (2, 50), (3, 30), (4, 5))
        levels = h.get_level_order()
        assert levels[0][0]["likes"] == 50     # root must be the max

    def test_level_order_total_elements(self):
        h = TrendingHeap()
        for i in range(1, 8):                  # 7 elements
            h.push(i, i * 10, time.time())
        levels = h.get_level_order()
        total = sum(len(lvl) for lvl in levels)
        assert total == 7


# =========================================================================== #
#  Run summary when executed directly                                          #
# =========================================================================== #

if __name__ == "__main__":
    import sys
    # Simple runner without pytest for quick manual checks
    tests = [
        TestEmptyHeap,
        TestSingleElement,
        TestGetTopKBoundaries,
        TestUpdateLikesEdgeCases,
        TestHeapValidity,
        TestDuplicateLikes,
        TestPopUntilEmpty,
        TestAnalytics,
    ]

    passed = 0
    failed = 0

    for cls in tests:
        instance = cls()
        methods  = [m for m in dir(cls) if m.startswith("test_")]
        print(f"\n{'='*60}")
        print(f"  {cls.__name__}  ({len(methods)} tests)")
        print(f"{'='*60}")
        for method in methods:
            try:
                getattr(instance, method)()
                print(f"  PASS  {method}")
                passed += 1
            except Exception as e:
                print(f"  FAIL  {method}")
                print(f"        {type(e).__name__}: {e}")
                failed += 1

    print(f"\n{'='*60}")
    print(f"  Results: {passed} passed, {failed} failed")
    print(f"{'='*60}")
    sys.exit(0 if failed == 0 else 1)