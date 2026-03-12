**LAB 03 Explanation**

Eylül Safiye Varyemez : Exercise 1

**Exercise 1**

We reperesented a single story using "StoryNode" (has an ID, content, views, and two pointers: next and prev)

We used "DoublyLinkedList" to hold the whole feed (tracks head, tail, current, and size)

In core operations we tried to manage the feed itself using functions

Feed Management: adding, removing, and inserting stories while always keeping the prev/next links consistent and updating head/tail when needed

Navigation: move_forward and move_backward simply shift the current pointer one step, while jump_to does a linear O(n) search through the list

Engagement: track_view increments the current story's counter, most_viewed finds the max in a single pass, and reorder_by_views applies a bubble sort by swapping data fields between nodes rather than rewiring pointers

The key reason we used a Doubly Linked List is the *prev* pointer, it lets us go backwards through the feed in O(1), which a regular singly linked list can't do.

**Complexity Analysis**
The doubly linked list trades a small amount of extra memory for significant performance gains. Backward navigation drops from O(n) to O(1), and node removal becomes O(1) since both neighbors are always directly reachable. This overhead is only worth it when bidirectional traversal is frequent, such as in story feeds, browser history, music playlists, or undo/redo systems. If navigation is one-directional, a singly linked list is the more memory-efficient choice.
