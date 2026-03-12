# ============================================================
#  LAB 3 – Exercise 1: Simple Test Set
# ============================================================

from story_feed import (
    StoryNode, DoublyLinkedList,
    add_story, remove_story, move_forward, move_backward,
    jump_to, insert_after, track_view, most_viewed, reorder_by_views
)

# ── Create some stories ──────────────────────────────────────

s1 = StoryNode(1, 101, "Morning coffee",   1000)
s2 = StoryNode(2, 102, "Workout complete", 2000)
s3 = StoryNode(3, 103, "Sunset photo",     3000)

# ── Create the feed and add stories ─────────────────────────

feed = DoublyLinkedList()
add_story(feed, s1)
add_story(feed, s2)
add_story(feed, s3)

# ── TEST 1: Check the feed was built correctly ───────────────
print("TEST 1 - Feed structure")
print("Expected head : Story 1 →", feed.head.story_id == 1)
print("Expected tail : Story 3 →", feed.tail.story_id == 3)
print("Expected size : 3       →", feed.size == 3)

# ── TEST 2: Move forward ─────────────────────────────────────
print("\nTEST 2 - Move forward")
move_forward(feed)                          # now at Story 2
print("Expected current Story 2 →", feed.current.story_id == 2)
move_forward(feed)                          # now at Story 3
print("Expected current Story 3 →", feed.current.story_id == 3)
result = move_forward(feed)                 # already at last
print("Expected 'Already at last story' →", result == "Already at last story")

# ── TEST 3: Move backward ────────────────────────────────────
print("\nTEST 3 - Move backward")
move_backward(feed)                         # back to Story 2
print("Expected current Story 2 →", feed.current.story_id == 2)

# ── TEST 4: Jump to a story ──────────────────────────────────
print("\nTEST 4 - Jump to")
jump_to(feed, 1)
print("Expected current Story 1 →", feed.current.story_id == 1)
result = jump_to(feed, 99)                  # story that doesn't exist
print("Expected 'Story not found' →", result == "Story not found")

# ── TEST 5: Remove a story ───────────────────────────────────
print("\nTEST 5 - Remove story")
remove_story(feed, 2)
print("Expected size 2 →", feed.size == 2)
print("Expected Story1.next is Story3 →", feed.head.next.story_id == 3)

# ── TEST 6: Track views ──────────────────────────────────────
print("\nTEST 6 - Track views")
jump_to(feed, 1)
track_view(feed)
track_view(feed)
print("Expected Story1 views = 2 →", feed.current.views == 2)

jump_to(feed, 3)
track_view(feed)
print("Expected Story3 views = 1 →", feed.current.views == 1)

# ── TEST 7: Most viewed ──────────────────────────────────────
print("\nTEST 7 - Most viewed")
result = most_viewed(feed)
print("Expected most viewed is Story1 →", result.story_id == 1)

# ── TEST 8: Reorder by views ─────────────────────────────────
print("\nTEST 8 - Reorder by views")
reorder_by_views(feed)
print("Expected head is Story1 (2 views) →", feed.head.views == 2)
print("Expected tail is Story3 (1 view)  →", feed.tail.views == 1)

# ── TEST 9: Empty feed checks ────────────────────────────────
print("\nTEST 9 - Empty feed")
empty_feed = DoublyLinkedList()
print("Expected 'Feed is empty' on move_forward  →", move_forward(empty_feed)  == "Feed is empty")
print("Expected 'Feed is empty' on move_backward →", move_backward(empty_feed) == "Feed is empty")
print("Expected 'Story not found' on jump_to     →", jump_to(empty_feed, 1)    == "Story not found")
print("Expected 'Feed is empty' on most_viewed   →", most_viewed(empty_feed)   == "Feed is empty")
