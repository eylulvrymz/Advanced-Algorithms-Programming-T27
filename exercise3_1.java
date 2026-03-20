import java.util.*;

public class exercise3_1 {

    enum State { STATE_START, STATE_REPLIES_DONE }

    static class Comment {
        String text;
        List<Comment> replies = new ArrayList<>();
        Comment(String text) { this.text = text; }
    }

    static int maxRecursiveDepth(Comment comment, int currentDepth) {
        int max = currentDepth;
        for (Comment reply : comment.replies) {
            max = Math.max(max, maxRecursiveDepth(reply, currentDepth + 1));
        }
        return max;
    }

    static int maxIterativeStackSize(Comment comment) {
        int maxSize = 0;
        Deque<Object[]> stack = new ArrayDeque<>();
        stack.push(new Object[]{comment, State.STATE_START});
        while (!stack.isEmpty()) {
            maxSize = Math.max(maxSize, stack.size());
            Object[] top = stack.pop();
            Comment current = (Comment) top[0];
            State state = (State) top[1];
            if (state == State.STATE_START) {
                stack.push(new Object[]{current, State.STATE_REPLIES_DONE});
                for (int i = current.replies.size() - 1; i >= 0; i--) {
                    stack.push(new Object[]{current.replies.get(i), State.STATE_START});
                }
            }
        }
        return maxSize;
    }

    public static void main(String[] args) {
        Comment c1 = new Comment("Comment1");
        Comment r1 = new Comment("Reply1");
        Comment r2 = new Comment("Reply2");
        Comment sr1 = new Comment("SubReply1");
        r1.replies.add(sr1);
        c1.replies.add(r1);
        c1.replies.add(r2);

        System.out.println("Max recursive depth (= stack size): " + maxRecursiveDepth(c1, 0));
        System.out.println("Max iterative stack size: " + maxIterativeStackSize(c1));
        // Recursive = O(d), Iterative = O(n)
    }
}