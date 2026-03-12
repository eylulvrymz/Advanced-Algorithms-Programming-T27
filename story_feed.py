# ============================================================
#  LAB 3 – Exercise 1: Story Feed with Doubly Linked List
# ============================================================

# ── Data Structures ─────────────────────────────────────────

class StoryNode:
    def __init__(self, story_id, user_id, content_preview, timestamp):
        self.story_id        = story_id
        self.user_id         = user_id
        self.content_preview = content_preview
        self.timestamp       = timestamp
        self.views           = 0
        self.next            = None   # pointer to next node
        self.prev            = None   # pointer to previous node

    def __repr__(self):
        return f"[ID:{self.story_id} | '{self.content_preview}' | views:{self.views}]"


class DoublyLinkedList:
    def __init__(self):
        self.head    = None
        self.tail    = None
        self.current = None
        self.size    = 0

    # ── Core Operations ──────────────────────────────────────

    def add_story(self, node):
        """Add a story to the end of the feed (chronological order)."""
        node.next = None
        node.prev = None

        if self.head is None:
            self.head    = node
            self.tail    = node
            self.current = node
        else:
            node.prev       = self.tail
            self.tail.next  = node
            self.tail       = node

        self.size += 1

    def remove_story(self, story_id):
        """Delete a specific story from the feed by its ID."""
        temp = self.head

        while temp is not None:
            if temp.story_id == story_id:

                if temp.prev is not None:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next       # removing the head

                if temp.next is not None:
                    temp.next.prev = temp.prev
                else:
                    self.tail = temp.prev       # removing the tail

                if self.current == temp:
                    self.current = temp.next    # shift current if needed

                self.size -= 1
                print(f"Story {story_id} removed.")
                return

            temp = temp.next

        print("Story not found.")

    def move_forward(self):
        """Advance current to the next story and return it."""
        if self.current is None:
            return "Feed is empty"
        if self.current.next is None:
            return "Already at last story"

        self.current = self.current.next
        return self.current

    def move_backward(self):
        """Move current to the previous story and return it."""
        if self.current is None:
            return "Feed is empty"
        if self.current.prev is None:
            return "Already at first story"

        self.current = self.current.prev
        return self.current

    def jump_to(self, story_id):
        """Set current to a specific story by ID – O(n) search."""
        temp = self.head

        while temp is not None:
            if temp.story_id == story_id:
                self.current = temp
                return self.current
            temp = temp.next

        return "Story not found"

    def insert_after(self, current_id, new_story):
        """Insert new_story immediately after the story with current_id."""
        temp = self.head

        while temp is not None:
            if temp.story_id == current_id:

                new_story.next = temp.next
                new_story.prev = temp

                if temp.next is not None:
                    temp.next.prev = new_story
                else:
                    self.tail = new_story       # inserted at the end

                temp.next  = new_story
                self.size += 1
                return

            temp = temp.next

        print("Story not found.")

    def display_around_current(self, k):
        """Show k stories before and after the current story."""
        if self.current is None:
            print("No current story.")
            return

        # Collect up to k stories BEFORE current
        before_list = []
        before      = self.current.prev
        count       = 0
        while before is not None and count < k:
            before_list.append(before)
            before = before.prev
            count += 1
        before_list.reverse()          # show oldest first

        for story in before_list:
            print(f"  {story}")

        print(f"  >>> CURRENT: {self.current}")

        # Collect up to k stories AFTER current
        after = self.current.next
        count = 0
        while after is not None and count < k:
            print(f"  {after}")
            after  = after.next
            count += 1

    # ── Engagement Tracking ──────────────────────────────────

    def track_view(self):
        """Increment view count of the current story."""
        if self.current is None:
            print("No current story.")
            return

        self.current.views += 1

    def most_viewed(self):
        """Return the story with the highest view count (single traversal)."""
        if self.head is None:
            return "Feed is empty"

        max_node = self.head
        temp     = self.head.next

        while temp is not None:
            if temp.views > max_node.views:
                max_node = temp
            temp = temp.next

        return max_node

    def reorder_by_views(self):
        """Reorganise feed so most-viewed stories appear first (bubble sort)."""
        if self.head is None:
            return

        swapped = True

        while swapped:
            swapped = False
            temp    = self.head

            while temp.next is not None:
                if temp.views < temp.next.views:
                    # Swap data fields (not pointers)
                    temp.story_id,        temp.next.story_id        = temp.next.story_id,        temp.story_id
                    temp.user_id,         temp.next.user_id         = temp.next.user_id,         temp.user_id
                    temp.content_preview, temp.next.content_preview = temp.next.content_preview, temp.content_preview
                    temp.timestamp,       temp.next.timestamp       = temp.next.timestamp,       temp.timestamp
                    temp.views,           temp.next.views           = temp.next.views,           temp.views
                    swapped = True

                temp = temp.next

    # ── Display Helper ───────────────────────────────────────

    def display_all(self):
        """Print every story in the feed from head to tail."""
        temp = self.head
        print("Feed (head → tail):")
        while temp is not None:
            marker = " ◄ CURRENT" if temp == self.current else ""
            print(f"  {temp}{marker}")
            temp = temp.next
        print()


# ── Demo / Test ──────────────────────────────────────────────

if __name__ == "__main__":
    feed = DoublyLinkedList()

    # Add three stories
    s1 = StoryNode(1, 101, "Morning coffee",   1000)
    s2 = StoryNode(2, 102, "Workout complete", 2000)
    s3 = StoryNode(3, 103, "Sunset photo",     3000)

    feed.add_story(s1)
    feed.add_story(s2)
    feed.add_story(s3)

    print("=== Initial feed ===")
    feed.display_all()

    # Navigate
    print("=== Move forward ===")
    print(" →", feed.move_forward())
    print(" →", feed.move_forward())
    print(" →", feed.move_forward())   # already at last
    print()

    # Track views
    print("=== Tracking views ===")
    feed.jump_to(2)
    feed.track_view()
    feed.track_view()          # Story2 viewed twice

    feed.jump_to(3)
    feed.track_view()          # Story3 viewed once

    feed.display_all()

    # Most viewed
    print("=== Most viewed ===")
    print(" →", feed.most_viewed())
    print()

    # Reorder
    print("=== After reorder_by_views ===")
    feed.reorder_by_views()
    feed.display_all()

    # Insert after
    print("=== Insert after Story1 ===")
    s4 = StoryNode(4, 104, "New story inserted", 1500)
    feed.jump_to(1)             # current = Story1 (after reorder, now tail)
    feed.insert_after(1, s4)
    feed.display_all()

    # Display around current
    print("=== Display 1 around current (Story1) ===")
    feed.display_around_current(1)
    print()

    # Remove a story
    print("=== Remove Story3 ===")
    feed.remove_story(3)
    feed.display_all()
