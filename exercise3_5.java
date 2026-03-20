import java.util.*;

public class exercise3_5 {

    enum State { STATE_START, STATE_REPLIES_DONE }

    static final int MAX_DEPTH = 500;
    static final int MAX_COMMENTS = 10000;

    static class Comment {
        String text;
        List<Comment> replies = new ArrayList<>();
        Comment(String text) { this.text = text; }
    }

    static int getDepth(Comment comment, int d) {
        int max = d;
        for (Comment reply : comment.replies) {
            max = Math.max(max, getDepth(reply, d + 1));
        }
        return max;
    }

    static Comment truncateTree(Comment comment, int maxDepth) {
        Comment truncated = new Comment(comment.text);
        if (maxDepth == 0) return truncated;
        for (Comment reply : comment.replies) {
            truncated.replies.add(truncateTree(reply, maxDepth - 1));
        }
        return truncated;
    }

    static List<Comment> flatten_iterative(Comment comment) {
        List<Comment> result = new ArrayList<>();
        Deque<Object[]> stack = new ArrayDeque<>();
        stack.push(new Object[]{comment, State.STATE_START});
        while (!stack.isEmpty()) {
            Object[] top = stack.pop();
            Comment current = (Comment) top[0];
            State state = (State) top[1];
            if (state == State.STATE_START) {
                result.add(current);
                stack.push(new Object[]{current, State.STATE_REPLIES_DONE});
                for (int i = current.replies.size() - 1; i >= 0; i--) {
                    stack.push(new Object[]{current.replies.get(i), State.STATE_START});
                }
            }
        }
        return result;
    }

    static List<Comment> handleProductionRequest(Comment comment) {
        if (getDepth(comment, 0) > MAX_DEPTH) {
            System.out.println("Tree too deep, truncating at " + MAX_DEPTH);
            comment = truncateTree(comment, MAX_DEPTH);
        }
        List<Comment> result = flatten_iterative(comment);
        if (result.size() > MAX_COMMENTS) {
            System.out.println("Too many comments, truncating at " + MAX_COMMENTS);
            return result.subList(0, MAX_COMMENTS);
        }
        return result;
    }

    public static void main(String[] args) {
        Comment c1 = new Comment("Comment1");
        Comment r1 = new Comment("Reply1");
        Comment r2 = new Comment("Reply2");
        Comment sr1 = new Comment("SubReply1");
        r1.replies.add(sr1);
        c1.replies.add(r1);
        c1.replies.add(r2);

        List<Comment> result = handleProductionRequest(c1);
        System.out.println("Result: " + result.stream().map(c -> c.text).toList());
    }
}