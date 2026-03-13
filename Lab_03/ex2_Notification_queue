# NotifNode structure
class NotifNode:
    def __init__(self, message, notif_type, timestamp):
        self.message   = message
        self.type      = notif_type
        self.timestamp = timestamp
        self.next      = None

# NotificationQueue structure
class NotificationQueue:
    def __init__(self):
        self.front = None
        self.rear  = None
        self.count = 0

    def enqueue(self, message, notif_type, timestamp):
        node       = NotifNode(message, notif_type, timestamp)
        node.next  = None
        if self.rear is not None:
            self.rear.next = node
        else:
            self.front = node
        self.rear   = node
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        node       = self.front
        self.front = node.next
        if self.front is None:
            self.rear = None
        self.count -= 1
        return node

    def front_peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front

    def is_empty(self):
        return self.front is None

    def size(self):
        return self.count

    def display_pending(self):
        current = self.front
        while current is not None:
            print(f"  [{current.type}] {current.message} time={current.timestamp}")
            current = current.next

    def priority_enqueue(self, message, notif_type, timestamp):
        node       = NotifNode(message, notif_type, timestamp)
        node.next  = self.front
        self.front = node
        if self.rear is None:
            self.rear = node
        self.count += 1


# TESTS
if __name__ == "__main__":

    q = NotificationQueue()

    print("ENQUEUE 3 notifications")
    q.enqueue("New follower", "follow",  2000)
    q.enqueue("New like",     "like",    2001)
    q.enqueue("New comment",  "comment", 2002)
    print(f"Size: {q.size()}")

    print("\nDISPLAY all pending")
    q.display_pending()

    print("\nPEEK front")
    print(f"Front: [{q.front_peek().type}] {q.front_peek().message}")

    print("\nFIFO order check (dequeue all)")
    print(f"dequeue 1: {q.dequeue().message}")
    print(f"dequeue 2: {q.dequeue().message}")
    print(f"dequeue 3: {q.dequeue().message}")
    print(f"Size after all dequeued: {q.size()}")

    print("\nDEQUEUE on empty queue")
    try:
        q.dequeue()
    except IndexError as e:
        print(f"Caught: {e}")

    print("\nPEEK on empty queue")
    try:
        q.front_peek()
    except IndexError as e:
        print(f"Caught: {e}")

    print("\nIS_EMPTY check")
    print(f"Queue is empty: {q.is_empty()}")
    q.enqueue("New follower", "follow", 3000)
    print(f"Queue is empty after enqueue: {q.is_empty()}")

    print("\nPRIORITY ENQUEUE on non-empty queue")
    q.enqueue("New like", "like", 3001)
    q.enqueue("New comment", "comment", 3002)
    q.priority_enqueue("URGENT alert", "urgent", 3003)
    print("Queue after priority enqueue:")
    q.display_pending()

    print("\nPRIORITY ENQUEUE on empty queue")
    q2 = NotificationQueue()
    q2.priority_enqueue("Urgent only", "urgent", 4000)
    print(f"front=rear check: {q2.front == q2.rear}")
    print(f"Size: {q2.size()}")

    print("\nMULTIPLE PRIORITY ENQUEUES (last urgent = first out)")
    q3 = NotificationQueue()
    q3.priority_enqueue("Urgent X", "urgent", 5000)
    q3.priority_enqueue("Urgent Y", "urgent", 5001)
    q3.priority_enqueue("Urgent Z", "urgent", 5002)
    print(f"dequeue 1: {q3.dequeue().message}")
    print(f"dequeue 2: {q3.dequeue().message}")
    print(f"dequeue 3: {q3.dequeue().message}")

    print("\nSINGLE enqueue then dequeue (front=rear=None after)")
    q4 = NotificationQueue()
    q4.enqueue("Only one", "like", 6000)
    print(f"front=rear before dequeue: {q4.front == q4.rear}")
    q4.dequeue()
    print(f"front is None: {q4.front is None}")
    print(f"rear is None: {q4.rear is None}")

    print("\nSIZE stays accurate through enqueue/dequeue/priority")
    q5 = NotificationQueue()
    q5.enqueue("A", "like",    7000)
    q5.enqueue("B", "follow",  7001)
    q5.enqueue("C", "comment", 7002)
    print(f"Size after 3 enqueues: {q5.size()}")
    q5.dequeue()
    print(f"Size after 1 dequeue: {q5.size()}")
    q5.priority_enqueue("D", "urgent", 7003)
    print(f"Size after priority enqueue: {q5.size()}")

    print("\nALL 4 notification types in queue")
    q6 = NotificationQueue()
    q6.enqueue("msg1", "follow",  8000)
    q6.enqueue("msg2", "like",    8001)
    q6.enqueue("msg3", "comment", 8002)
    q6.enqueue("msg4", "urgent",  8003)
    print("All pending:")
    q6.display_pending()
    print("\nDISPLAY PENDING on empty queue")
    q7 = NotificationQueue()
    q7.display_pending()
    print("nothing printed above is correct")

    print("\nALTERNATING enqueue and dequeue")
    q8 = NotificationQueue()
    q8.enqueue("msg1", "like", 9000)
    print(f"dequeue: {q8.dequeue().message}")
    q8.enqueue("msg2", "follow", 9001)
    print(f"dequeue: {q8.dequeue().message}")
    q8.enqueue("msg3", "comment", 9002)
    print(f"dequeue: {q8.dequeue().message}")
    print(f"Size after alternating: {q8.size()}")
    print(f"front is None: {q8.front is None}")
    print(f"rear is None: {q8.rear is None}")
