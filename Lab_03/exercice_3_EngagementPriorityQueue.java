import java.util.ArrayList;
import java.util.List;

public class EngagementPriorityQueue {
    private Post head;
    private int size;

    public EngagementPriorityQueue() {
        this.head = null;
        this.size = 0;
    }

    public void enqueue(Post post) {
        post.engagementScore = Post.computeScore(post.likes, post.comments, post.shares);
        post.next = null;

        if (head == null || post.engagementScore > head.engagementScore) {
            post.next = head;
            head = post;
        } else {
            Post current = head;
            while (current.next != null && current.next.engagementScore >= post.engagementScore) {
                current = current.next;
            }
            post.next = current.next;
            current.next = post;
        }
        size++;
    }

    public Post dequeueMax() {
        if (head == null) return null;
        Post max = head;
        head = head.next;
        max.next = null;
        size--;
        return max;
    }

    public Post peekMax() {
        return head;
    }

    public boolean isEmpty() {
        return head == null;
    }

    public int size() {
        return size;
    }

    public void updateScore(int postId, int newLikes, int newComments, int newShares) {
        Post prev = null;
        Post current = head;

        while (current != null && current.postId != postId) {
            prev = current;
            current = current.next;
        }

        if (current == null) return;

        if (prev == null) {
            head = current.next;
        } else {
            prev.next = current.next;
        }
        size--;

        current.likes = newLikes;
        current.comments = newComments;
        current.shares = newShares;
        current.next = null;

        enqueue(current);
    }

    public void refreshAll() {
        List<Post> posts = new ArrayList<>();
        Post current = head;
        while (current != null) {
            posts.add(current);
            current = current.next;
        }

        head = null;
        size = 0;

        for (Post p : posts) {
            p.engagementScore = Post.computeScore(p.likes, p.comments, p.shares);
            p.next = null;
            enqueue(p);
        }
    }

    public List<Post> getTopK(int k) {
        List<Post> result = new ArrayList<>();
        Post current = head;
        int count = 0;
        while (current != null && count < k) {
            result.add(current);
            current = current.next;
            count++;
        }
        return result;
    }

    private void resort() {
        List<Post> posts = new ArrayList<>();
        Post current = head;
        while (current != null) {
            posts.add(current);
            current = current.next;
        }

        head = null;
        size = 0;

        for (Post p : posts) {
            p.next = null;
            Post tmp = p;
            if (head == null || tmp.engagementScore > head.engagementScore) {
                tmp.next = head;
                head = tmp;
            } else {
                Post cur = head;
                while (cur.next != null && cur.next.engagementScore >= tmp.engagementScore) {
                    cur = cur.next;
                }
                tmp.next = cur.next;
                cur.next = tmp;
            }
            size++;
        }
    }

    public void decayOlderThan(long timestamp) {
        Post current = head;
        while (current != null) {
            if (current.timestamp < timestamp) {
                current.engagementScore = (int) Math.floor(current.engagementScore * 0.8);
            }
            current = current.next;
        }
        resort();
    }

    public void display() {
        if (head == null) {
            System.out.println("Queue is empty");
            return;
        }
        Post current = head;
        StringBuilder sb = new StringBuilder();
        while (current != null) {
            sb.append(current);
            if (current.next != null) sb.append(" -> ");
            current = current.next;
        }
        System.out.println(sb);
    }
}