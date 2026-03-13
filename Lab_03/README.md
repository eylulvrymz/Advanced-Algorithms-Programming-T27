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
# Exercise 2 – Activity Feed Processing with Stacks and Queue
**Elenie Girma Wakjira**

## Goal
The goal of this exercise was to understand how stacks and queues work
and how to combine them to model different content processing patterns
in a social media app.



### Part A – Recent Activity Stack
A stack using a linked list to store user activities (like, comment,
share, follow). The most recent activity is always on top (LIFO).
We also added an undo feature that reverts the last action and saves
it to a separate undo stack.

### Part B – Notification Queue
A queue using a linked list to process notifications in the order
they arrive (FIFO). We also added a priority enqueue that inserts
urgent notifications directly at the front of the queue.

### Part C – Integrated Feed Processor
A FeedProcessor that combines both structures. Incoming notifications
are held in a queue, moved to the activity stack when processed, and
archived to a processed log queue when history is cleared.
## Complexity Analysis

All the core stack operations like push, pop and peek run in O(1)
because we only ever touch the top pointer. Same thing for the queue,
enqueue, dequeue and front are all O(1) since we maintain both front
and rear pointers so no traversal is needed. The only operations that
take longer are display_recent and display_pending which are O(n)
since they have to go through each node. For the FeedProcessor,
batch_process(k) runs in O(k) since it just calls process_incoming
k times, and clear_history is O(m) where m is however many items
are in the stack at that point. Everything else like get_stats and
process_incoming are O(1).






 
exercice 3
yan shen
# Exercise 3 – Priority Queue

This is exercise 3 of LAB3. It's a priority queue using a sorted linked list, posts with higher engagement scores go to the top.

Score = likes x1 + comments x2 + shares x3

To run it just do javac *.java then java Main.

One thing worth knowing: decayOlderThan uses resort() instead of refreshAll() because refreshAll recalculates scores from the original data and would just undo the decay. Took me a while to notice that one.
