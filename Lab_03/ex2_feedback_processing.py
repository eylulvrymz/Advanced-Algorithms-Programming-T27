from ex2_Activity_Stack import ActivityStack
from ex2_Notification_queue import NotificationQueue

# FeedProcessor structure
class FeedProcessor:
    def __init__(self):
        self.recent_activities  = ActivityStack()
        self.notification_queue = NotificationQueue()
        self.processed_log      = NotificationQueue()

    def process_incoming(self):
        if self.notification_queue.is_empty():
            return
        notif = self.notification_queue.dequeue()
        self.recent_activities.push(notif.type, notif.message, notif.timestamp)

    def batch_process(self, k):
        i = 0
        while i < k and not self.notification_queue.is_empty():
            self.process_incoming()
            i += 1

    def clear_history(self):
        while not self.recent_activities.is_empty():
            item = self.recent_activities.pop()
            self.processed_log.enqueue(item.activity_type, item.activity_type, item.timestamp)

    def get_stats(self):
        return (self.recent_activities.size(),
                self.notification_queue.size(),
                self.processed_log.size())


# TESTS
if __name__ == "__main__":

    fp = FeedProcessor()

    print("STATS on fresh FeedProcessor")
    print(f"Stats: {fp.get_stats()}")

    print("\nENQUEUE 3 notifications")
    fp.notification_queue.enqueue("New follower", "follow",  3000)
    fp.notification_queue.enqueue("New like",     "like",    3001)
    fp.notification_queue.enqueue("New comment",  "comment", 3002)
    print(f"Stats: {fp.get_stats()}")

    print("\nPROCESS INCOMING once")
    fp.process_incoming()
    print(f"Stats: {fp.get_stats()}")
    print("Top of recent stack:")
    fp.recent_activities.display_recent(1)

    print("\nBATCH PROCESS 2")
    fp.batch_process(2)
    print(f"Stats: {fp.get_stats()}")
    print("Recent stack after batch:")
    fp.recent_activities.display_recent(5)

    print("\nCLEAR HISTORY")
    fp.clear_history()
    print(f"Stats: {fp.get_stats()}")

    print("\nPROCESS INCOMING on empty queue")
    fp2 = FeedProcessor()
    fp2.process_incoming()
    print(f"Stats: {fp2.get_stats()}")

    print("\nBATCH PROCESS k=0")
    fp3 = FeedProcessor()
    fp3.notification_queue.enqueue("msg1", "like", 4000)
    fp3.notification_queue.enqueue("msg2", "like", 4001)
    fp3.batch_process(0)
    print(f"Stats unchanged: {fp3.get_stats()}")

    print("\nBATCH PROCESS k > queue size")
    fp4 = FeedProcessor()
    fp4.notification_queue.enqueue("msg1", "like",   5000)
    fp4.notification_queue.enqueue("msg2", "follow", 5001)
    fp4.batch_process(10)
    print(f"Stats after batch 10 on 2 items: {fp4.get_stats()}")

    print("\nCLEAR HISTORY on empty stack")
    fp5 = FeedProcessor()
    fp5.clear_history()
    print(f"Stats unchanged: {fp5.get_stats()}")

    print("\nFULL PIPELINE enqueue > process > clear")
    fp6 = FeedProcessor()
    fp6.notification_queue.enqueue("New follower", "follow",  6000)
    fp6.notification_queue.enqueue("New like",     "like",    6001)
    fp6.notification_queue.enqueue("New comment",  "comment", 6002)
    fp6.batch_process(3)
    print(f"Stats after batch 3: {fp6.get_stats()}")
    fp6.clear_history()
    print(f"Stats after clear: {fp6.get_stats()}")

    print("\nFIFO in queue becomes LIFO in stack")
    fp7 = FeedProcessor()
    fp7.notification_queue.enqueue("A", "follow",  7000)
    fp7.notification_queue.enqueue("B", "like",    7001)
    fp7.notification_queue.enqueue("C", "comment", 7002)
    fp7.batch_process(3)
    print("Recent stack top to bottom:")
    fp7.recent_activities.display_recent(3)
