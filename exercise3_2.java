import java.util.*;

public class exercise3_2 {

    static class Comment {
        String text;
        List<Comment> replies = new ArrayList<>();
        Comment(String text) { this.text = text; }
    }

    enum State { STATE_START, STATE_REPLIES_DONE }

    static int getDepth(Comment comment, int d) {
        int max = d;
        for (Comment reply : comment.replies) {
            max = Math.max(max, getDepth(reply, d + 1));
        }
        return max;
    }

    static List<Comment> flatten_recursive(Comment comment) {
        List<Comment> result = new ArrayList<>();
        result.add(comment);
        for (Comment reply : comment.replies) {
            result.addAll(flatten_recursive(reply));
        }
        return result;
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

    static List<Comment> chooseApproach(Comment comment) {
        int depth = getDepth(comment, 0);
        if (depth < 1000) {
            System.out.println("Depth = " + depth + " → using recursive");
            return flatten_recursive(comment);
        } else {
            System.out.println("Depth = " + depth + " → using iterative");
            return flatten_iterative(comment);
        }
    }

    public static void main(String[] args) {
        Comment c1 = new Comment("Comment1");
        Comment r1 = new Comment("Reply1");
        Comment r2 = new Comment("Reply2");
        Comment sr1 = new Comment("SubReply1");
        r1.replies.add(sr1);
        c1.replies.add(r1);
        c1.replies.add(r2);

        List<Comment> result = chooseApproach(c1);
        System.out.println("Result: " + result.stream().map(c -> c.text).toList());
    }
}