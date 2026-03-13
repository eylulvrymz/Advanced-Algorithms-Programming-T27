import java.util.Random;

public class DualPriorityQueue {
    private EngagementPriorityQueue viralQueue;
    private EngagementPriorityQueue normalQueue;
    private static final int VIRAL_THRESHOLD = 100;
    private static final double VIRAL_PROBABILITY = 0.7;
    private final Random random;

    public DualPriorityQueue() {
        this.viralQueue = new EngagementPriorityQueue();
        this.normalQueue = new EngagementPriorityQueue();
        this.random = new Random();
    }

    public void enqueue(Post post) {
        if (post.engagementScore > VIRAL_THRESHOLD) {
            viralQueue.enqueue(post);
        } else {
            normalQueue.enqueue(post);
        }
    }

    public Post dequeue() {
        if (viralQueue.isEmpty() && normalQueue.isEmpty()) return null;
        if (viralQueue.isEmpty()) return normalQueue.dequeueMax();
        if (normalQueue.isEmpty()) return viralQueue.dequeueMax();

        double r = random.nextDouble();
        if (r < VIRAL_PROBABILITY) {
            return viralQueue.dequeueMax();
        } else {
            return normalQueue.dequeueMax();
        }
    }

    public void display() {
        System.out.print("Viral queue : ");
        viralQueue.display();
        System.out.print("Normal queue: ");
        normalQueue.display();
    }
}