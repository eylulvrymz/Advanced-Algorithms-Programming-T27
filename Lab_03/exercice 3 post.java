public class Post {
    int postId;
    int userId;
    String content;
    long timestamp;
    int likes;
    int comments;
    int shares;
    int engagementScore;
    Post next;

    public Post(int postId, int userId, String content, long timestamp, int likes, int comments, int shares) {
        this.postId = postId;
        this.userId = userId;
        this.content = content;
        this.timestamp = timestamp;
        this.likes = likes;
        this.comments = comments;
        this.shares = shares;
        this.engagementScore = computeScore(likes, comments, shares);
        this.next = null;
    }

    public static int computeScore(int likes, int comments, int shares) {
        return likes * 1 + comments * 2 + shares * 3;
    }

    @Override
    public String toString() {
        return "[Post" + postId + " | score:" + engagementScore + " | \"" + content + "\"]";
    }
}