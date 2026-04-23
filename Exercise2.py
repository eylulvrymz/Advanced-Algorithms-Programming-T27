import math
import random
import time


class TrendingHeap:
    def __init__(self):
        self.heap = []          # list of dicts: {likes, post_id, timestamp}
        self.pos  = {}          # pos[post_id] -> index in heap

    # ------------------------------------------------------------------ #
    #  Internal helpers                                                    #
    # ------------------------------------------------------------------ #

    def _swap(self, i, j):
        self.pos[self.heap[i]["post_id"]] = j
        self.pos[self.heap[j]["post_id"]] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i]["likes"] > self.heap[parent]["likes"]:
                self._swap(i, parent)
                i = parent
            else:
                break

    def _heapify_down(self, i):
        n       = len(self.heap)
        largest = i
        left    = 2 * i + 1
        right   = 2 * i + 2

        if left < n and self.heap[left]["likes"] > self.heap[largest]["likes"]:
            largest = left
        if right < n and self.heap[right]["likes"] > self.heap[largest]["likes"]:
            largest = right

        if largest != i:
            self._swap(i, largest)
            self._heapify_down(largest)

    # ------------------------------------------------------------------ #
    #  Core heap operations                                                #
    # ------------------------------------------------------------------ #

    def push(self, post_id, likes, timestamp):
        """Insert a new post into the heap."""
        entry = {"likes": likes, "post_id": post_id, "timestamp": timestamp}
        self.heap.append(entry)
        self.pos[post_id] = len(self.heap) - 1
        self._heapify_up(len(self.heap) - 1)

    def pop_max(self):
        """Remove and return the post with the most likes."""
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)
        max_entry = self.heap.pop()
        del self.pos[max_entry["post_id"]]
        if self.heap:
            self._heapify_down(0)
        return max_entry

    def peek_max(self):
        """Return the post with the most likes without removing it."""
        if not self.heap:
            return None
        return self.heap[0]

    def get_top_k(self, k):
        """
        Return the top-k posts by likes without modifying the original heap.
        Uses a temporary copy so the real heap is preserved.
        """
        # Deep-copy heap and pos into a temporary TrendingHeap
        tmp = TrendingHeap()
        tmp.heap = [entry.copy() for entry in self.heap]
        tmp.pos  = dict(self.pos)

        result = []
        i = 0
        while i < k and tmp.heap:
            result.append(tmp.pop_max())
            i += 1
        return result

    def update_likes(self, post_id, new_likes, timestamp):
        """Update the like count (and timestamp) of an existing post."""
        if post_id not in self.pos:
            return
        i         = self.pos[post_id]
        old_likes = self.heap[i]["likes"]
        self.heap[i]["likes"]     = new_likes
        self.heap[i]["timestamp"] = timestamp

        if new_likes > old_likes:
            self._heapify_up(i)
        else:
            self._heapify_down(i)

    def size(self):
        return len(self.heap)

    # ------------------------------------------------------------------ #
    #  Heap analytics                                                      #
    # ------------------------------------------------------------------ #

    def is_valid_heap(self):
        """Verify the max-heap property holds for every node."""
        for i in range(1, len(self.heap)):
            parent = (i - 1) // 2
            if self.heap[i]["likes"] > self.heap[parent]["likes"]:
                return False
        return True

    def get_height(self):
        """Height of the binary heap (number of levels)."""
        if not self.heap:
            return 0
        return math.floor(math.log2(len(self.heap))) + 1

    def get_level_order(self):
        """
        Return the heap level by level.
        Each element of the returned list is one level (a list of entries).
        """
        result      = []
        level_start = 0
        n           = len(self.heap)

        while level_start < n:
            level_end = min(2 * level_start + 2, n - 1)
            result.append(self.heap[level_start : level_end + 1])
            level_start = level_end + 1

        return result

    # ------------------------------------------------------------------ #
    #  Simulation                                                          #
    # ------------------------------------------------------------------ #

    def simulate_trending_feed(self):
        """
        - Seed the heap with 100 posts (random likes 0-1000).
        - Perform 10,000 like updates on random posts.
        - Print top-5 every 1,000 updates.
        - Report the average time per update_likes call.
        """
        trending = TrendingHeap()

        # ---- Setup: 100 initial posts --------------------------------- #
        for post_id in range(1, 101):
            likes     = random.randint(0, 1000)
            timestamp = time.time()
            trending.push(post_id, likes, timestamp)

        # ---- Simulation ----------------------------------------------- #
        total_time = 0.0
        updates    = 0

        for _ in range(10_000):
            post_id   = random.randint(1, 100)
            new_likes = random.randint(0, 10_000)
            timestamp = time.time()

            start = time.perf_counter()
            trending.update_likes(post_id, new_likes, timestamp)
            total_time += time.perf_counter() - start

            updates += 1

            if updates % 1000 == 0:
                print(f"\nAfter {updates} updates – Top 5 Trending Posts:")
                top5 = trending.get_top_k(5)
                for rank, entry in enumerate(top5, start=1):
                    print(
                        f"  Rank {rank} | post_id: {entry['post_id']:>3} | "
                        f"likes: {entry['likes']:>6} | "
                        f"timestamp: {entry['timestamp']:.4f}"
                    )

        # ---- Report --------------------------------------------------- #
        avg_time = total_time / 10_000
        print(f"\nAverage time per update_likes operation: {avg_time:.8f} s")


# --------------------------------------------------------------------------- #
#  Entry point                                                                 #
# --------------------------------------------------------------------------- #

if __name__ == "__main__":
    heap = TrendingHeap()
    heap.simulate_trending_feed()

    # Quick sanity checks
    print("\n--- Sanity checks on a fresh heap ---")
    h = TrendingHeap()
    for pid, lk in [(1, 300), (2, 500), (3, 100), (4, 700), (5, 200)]:
        h.push(pid, lk, time.time())

    print("Heap valid?      ", h.is_valid_heap())
    print("Height:          ", h.get_height())
    print("Peek max:        ", h.peek_max())
    print("Top 3:           ", [(e["post_id"], e["likes"]) for e in h.get_top_k(3)])

    h.update_likes(3, 900, time.time())
    print("After updating post 3 to 900 likes:")
    print("  Peek max:      ", h.peek_max())
    print("  Heap valid?    ", h.is_valid_heap())

    print("Pop max:         ", h.pop_max())
    print("Heap valid after pop?", h.is_valid_heap())