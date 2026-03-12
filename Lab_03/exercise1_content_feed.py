#Create a story node structure
class StoryNode:
    def __init__(self, story_id, user_id, content_preview, timestamp):
        self.story_id        = story_id
        self.user_id         = user_id
        self.content_preview = content_preview
        self.timestamp       = timestamp
        self.views           = 0
        self.next            = None
        self.prev            = None

    def __repr__(self):
        return f"[ID:{self.story_id} | '{self.content_preview}' | views:{self.views}]"

#Implement a DoublyLinkedList
class DoublyLinkedList:
    def __init__(self):
        self.head    = None
        self.tail    = None
        self.current = None
        self.size    = 0

#####Core Operations#####

def add_story(list, node):
    node.next = None
    node.prev = None

    if list.head is None:
        list.head    = node
        list.tail    = node
        list.current = node
    else:
        node.prev      = list.tail
        list.tail.next = node
        list.tail      = node

    list.size += 1


def remove_story(list, story_id):
    temp = list.head

    while temp is not None:
        if temp.story_id == story_id:

            if temp.prev is not None:
                temp.prev.next = temp.next
            else:
                list.head = temp.next       # removing head

            if temp.next is not None:
                temp.next.prev = temp.prev
            else:
                list.tail = temp.prev       # removing tail

            if list.current == temp:
                list.current = temp.next    # shift current if needed

            list.size -= 1
            print(f"Story {story_id} removed.")
            return

        temp = temp.next

    print("Story not found.")


def move_forward(list):
    if list.current is None:
        return "Feed is empty"
    if list.current.next is None:
        return "Already at last story"

    list.current = list.current.next
    return list.current


def move_backward(list):
    if list.current is None:
        return "Feed is empty"
    if list.current.prev is None:
        return "Already at first story"

    list.current = list.current.prev
    return list.current


def jump_to(list, story_id):
    temp = list.head

    while temp is not None:
        if temp.story_id == story_id:
            list.current = temp
            return list.current
        temp = temp.next

    return "Story not found"


def insert_after(list, current_id, new_story):
    temp = list.head

    while temp is not None:
        if temp.story_id == current_id:

            new_story.next = temp.next
            new_story.prev = temp

            if temp.next is not None:
                temp.next.prev = new_story
            else:
                list.tail = new_story       # inserted at the end

            temp.next  = new_story
            list.size += 1
            return

        temp = temp.next

    print("Story not found.")


def display_around_current(list, k):
    if list.current is None:
        print("No current story.")
        return

    # Collect up to k stories BEFORE current
    before_list = []
    before      = list.current.prev
    count       = 0
    while before is not None and count < k:
        before_list.append(before)
        before  = before.prev
        count  += 1
    before_list.reverse()

    for story in before_list:
        print(f"  {story}")

    print(f"  >>> CURRENT: {list.current}")

    # Collect up to k stories AFTER current
    after = list.current.next
    count = 0
    while after is not None and count < k:
        print(f"  {after}")
        after  = after.next
        count += 1


##### Engagement Tracking #####

def track_view(list):
    if list.current is None:
        print("No current story.")
        return

    list.current.views += 1


def most_viewed(list):
    if list.head is None:
        return "Feed is empty"

    max_node = list.head
    temp     = list.head.next

    while temp is not None:
        if temp.views > max_node.views:
            max_node = temp
        temp = temp.next

    return max_node


def reorder_by_views(list):
    if list.head is None:
        return

    swapped = True

    while swapped:
        swapped = False
        temp    = list.head

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


##### Display Helper #####

def display_all(list):
    temp = list.head
    print("Feed (head → tail):")
    while temp is not None:
        marker = " ◄ CURRENT" if temp == list.current else ""
        print(f"  {temp}{marker}")
        temp = temp.next
    print()


##### Demo / Test #####

if __name__ == "__main__":
    feed = DoublyLinkedList()

    s1 = StoryNode(1, 101, "Morning coffee",   1000)
    s2 = StoryNode(2, 102, "Workout complete", 2000)
    s3 = StoryNode(3, 103, "Sunset photo",     3000)

    add_story(feed, s1)
    add_story(feed, s2)
    add_story(feed, s3)

    print("=== Initial feed ===")
    display_all(feed)

    print("=== Move forward ===")
    print(" →", move_forward(feed))
    print(" →", move_forward(feed))
    print(" →", move_forward(feed))   # already at last
    print()

    print("=== Tracking views ===")
    jump_to(feed, 2)
    track_view(feed)
    track_view(feed)        # Story2 viewed twice

    jump_to(feed, 3)
    track_view(feed)        # Story3 viewed once

    display_all(feed)

    print("=== Most viewed ===")
    print(" →", most_viewed(feed))
    print()

    print("=== After reorder_by_views ===")
    reorder_by_views(feed)
    display_all(feed)

    print("=== Insert after Story1 ===")
    s4 = StoryNode(4, 104, "New story inserted", 1500)
    jump_to(feed, 1)
    insert_after(feed, 1, s4)
    display_all(feed)

    print("=== Display 1 around current (Story1) ===")
    display_around_current(feed, 1)
    print()

    print("=== Remove Story3 ===")
    remove_story(feed, 3)
    display_all(feed)
