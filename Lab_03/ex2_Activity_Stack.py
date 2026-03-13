# ActivityNode structure
class ActivityNode:
    def __init__(self, activity_type, target_id, timestamp):
        self.activity_type = activity_type
        self.target_id     = target_id
        self.timestamp     = timestamp
        self.next          = None

# ActivityStack structure
class ActivityStack:
    def __init__(self):
        self.top      = None
        self.undo_top = None
        self.count    = 0

    def push(self, activity_type, target_id, timestamp):
        node           = ActivityNode(activity_type, target_id, timestamp)
        node.next      = self.top
        self.top       = node
        self.count    += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        node       = self.top
        self.top   = node.next
        self.count -= 1
        return node

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.count

    def display_recent(self, n):
        if n <= 0:
            return
        current = self.top
        printed = 0
        while current is not None and printed < n:
            print(f"  [{current.activity_type}] target={current.target_id} time={current.timestamp}")
            current = current.next
            printed += 1

    def undo_last(self):
        if self.is_empty():
            raise IndexError("Nothing to undo")
        last = self.pop()
        self._push_undo(last)
        self._reverse_action(last)

    def _push_undo(self, node):
        node.next     = self.undo_top
        self.undo_top = node

    def _reverse_action(self, node):
        if node.activity_type == "like":
            print(f"  Unliked post {node.target_id}")
        elif node.activity_type == "comment":
            print(f"  Deleted comment on {node.target_id}")
        elif node.activity_type == "share":
            print(f"  Unshared post {node.target_id}")
        elif node.activity_type == "follow":
            print(f"  Unfollowed user {node.target_id}")


# TESTS
if __name__ == "__main__":

    s = ActivityStack()

    print(" PUSH 3 activities ")
    s.push("like",    101, 1000)
    s.push("comment", 102, 1001)
    s.push("share",   103, 1002)
    print(f"Size: {s.size()}")

    print("\n PEEK ")
    print(f"Top: [{s.peek().activity_type}] target={s.peek().target_id}")

    print("\n DISPLAY top 2 ")
    s.display_recent(2)

    print("\n DISPLAY with n=0 (should print nothing) ")
    s.display_recent(0)

    print("\n DISPLAY n > stack size (stack has 3, n=10) ")
    s.display_recent(10)  

    print("\n UNDO last (share) ")
    s.undo_last()
    print(f"Size after undo: {s.size()}")

    print("\n DISPLAY after undo ")
    s.display_recent(5)

    print("\n UNDO last (comment) ")
    s.undo_last()
    print(f"Size after undo: {s.size()}")

    print("\n UNDO last (like) ")
    s.undo_last()
    print(f"Size after undo: {s.size()}")

    print("\n  POP on empty stack ")
    try:
        s.pop()
    except IndexError as e:
        print(f"Caught: {e}")

    print("\n  UNDO on empty stack ")
    try:
        s.undo_last()
    except IndexError as e:
        print(f"Caught: {e}")

    print("\n PEEK on empty stack ")
    try:
        s.peek()
    except IndexError as e:
        print(f"Caught: {e}")

    print("\n IS_EMPTY check ")
    print(f"Stack is empty: {s.is_empty()}")  
    s.push("like", 200, 5000)
    print(f"Stack is empty after push: {s.is_empty()}")  

    print("\n UNDO follow action ")
    s2 = ActivityStack()
    s2.push("follow", 999, 3000)
    s2.undo_last()  
    print(f"Size after undo follow: {s2.size()}")

    print("\n UNDO stack is populated after undo ")
    s3 = ActivityStack()
    s3.push("like", 300, 4000)
    s3.undo_last()
    print(f"undo_top is not None: {s3.undo_top is not None}")  

    print("\n PUSH then undo then re-push ")
    s4 = ActivityStack()
    s4.push("like", 1, 1)
    s4.undo_last()
    print(f"Size after undo: {s4.size()}")   
    s4.push("share", 2, 2)
    print(f"Size after re-push: {s4.size()}")  
    print(f"Top is share: {s4.peek().activity_type}")  

    print("\n LIFO order check (all 4 activity types) ")
    s5 = ActivityStack()
    s5.push("like",    1, 1)
    s5.push("comment", 2, 2)
    s5.push("share",   3, 3)
    s5.push("follow",  4, 4)
    print(f"pop 1: {s5.pop().activity_type}")  
    print(f"pop 2: {s5.pop().activity_type}")  
    print(f"pop 3: {s5.pop().activity_type}")  
    print(f"pop 4: {s5.pop().activity_type}")  

    print("\n SIZE stays accurate through push/pop/undo ")
    s6 = ActivityStack()
    s6.push("like", 1, 1)
    s6.push("like", 2, 2)
    s6.push("like", 3, 3)
    print(f"Size after 3 pushes: {s6.size()}")   
    s6.pop()
    print(f"Size after 1 pop: {s6.size()}")       
    s6.undo_last()
    print(f"Size after undo: {s6.size()}")         
