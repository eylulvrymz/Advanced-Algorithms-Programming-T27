import java.util.List;

public class Main {

    static void separator(String label) {
        System.out.println("\n========== " + label + " ==========");
    }

    public static void main(String[] args) {

        separator("Basic enqueue + display");

        EngagementPriorityQueue pq = new EngagementPriorityQueue();
        Post p1 = new Post(1, 10, "Morning run", 1000L, 20, 5, 2);
        Post p2 = new Post(2, 11, "Beach sunset", 1100L, 40, 10, 5);
        Post p3 = new Post(3, 12, "Coffee time", 900L, 5, 1, 0);
        Post p4 = new Post(4, 13, "New recipe", 800L, 12, 3, 1);

        pq.enqueue(p1);
        pq.enqueue(p2);
        pq.enqueue(p3);
        pq.enqueue(p4);

        System.out.println("Queue after 4 inserts:");
        pq.display();
        System.out.println("Size: " + pq.size());

        separator("peekMax and dequeueMax");

        System.out.println("Peek max: " + pq.peekMax());
        Post removed = pq.dequeueMax();
        System.out.println("Dequeued: " + removed);
        System.out.println("Queue after dequeue:");
        pq.display();

        separator("updateScore");

        System.out.println("Before update:");
        pq.display();
        pq.updateScore(3, 30, 8, 4);
        System.out.println("After giving post3 more engagement:");
        pq.display();

        separator("getTopK");

        EngagementPriorityQueue pq2 = new EngagementPriorityQueue();
        pq2.enqueue(new Post(10, 1, "Post A", 500L, 80, 20, 10));
        pq2.enqueue(new Post(11, 2, "Post B", 600L, 30, 5, 2));
        pq2.enqueue(new Post(12, 3, "Post C", 700L, 10, 2, 1));
        pq2.enqueue(new Post(13, 4, "Post D", 800L, 5, 1, 0));

        System.out.println("Full queue:");
        pq2.display();
        List<Post> top2 = pq2.getTopK(2);
        System.out.print("Top 2: ");
        for (Post p : top2) System.out.print(p + " ");
        System.out.println();

        separator("decayOlderThan");

        System.out.println("Before decay (threshold timestamp=650):");
        pq2.display();
        pq2.decayOlderThan(650L);
        System.out.println("After decay (posts with timestamp < 650 lose 20%):");
        pq2.display();

        separator("Edge cases");

        EngagementPriorityQueue emptyPQ = new EngagementPriorityQueue();
        System.out.println("dequeueMax on empty: " + emptyPQ.dequeueMax());
        System.out.println("peekMax on empty: " + emptyPQ.peekMax());
        System.out.println("getTopK(5) on empty: " + emptyPQ.getTopK(5));

        EngagementPriorityQueue singlePQ = new EngagementPriorityQueue();
        Post solo = new Post(99, 1, "Lonely post", 100L, 3, 1, 0);
        singlePQ.enqueue(solo);
        System.out.println("Single node queue peek: " + singlePQ.peekMax());
        System.out.println("Dequeue it: " + singlePQ.dequeueMax());
        System.out.println("Is empty now? " + singlePQ.isEmpty());

        EngagementPriorityQueue samePQ = new EngagementPriorityQueue();
        Post sameA = new Post(20, 1, "Same score A", 200L, 10, 0, 0);
        Post sameB = new Post(21, 2, "Same score B", 300L, 10, 0, 0);
        samePQ.enqueue(sameA);
        samePQ.enqueue(sameB);
        System.out.println("Two posts with same score (10):");
        samePQ.display();

        EngagementPriorityQueue kPQ = new EngagementPriorityQueue();
        kPQ.enqueue(new Post(30, 1, "Only post", 100L, 5, 2, 1));
        System.out.println("getTopK(10) on queue with 1 element: " + kPQ.getTopK(10));

        separator("DualPriorityQueue bonus");

        DualPriorityQueue dpq = new DualPriorityQueue();
        dpq.enqueue(new Post(50, 1, "Viral banger", 100L, 50, 30, 20));
        dpq.enqueue(new Post(51, 2, "Chill post", 200L, 5, 2, 1));
        dpq.enqueue(new Post(52, 3, "Another viral", 300L, 60, 25, 15));
        dpq.enqueue(new Post(53, 4, "Normal stuff", 400L, 8, 3, 0));

        System.out.println("Initial state:");
        dpq.display();

        System.out.println("\nDequeuing 3 times (70% chance viral):");
        for (int i = 0; i < 3; i++) {
            Post got = dpq.dequeue();
            System.out.println("Got: " + got);
        }

        separator("Done");
    }
}