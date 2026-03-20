import java.util.*;

public class exercise3_4 {

    enum State { STATE_START, STATE_REPLIES_DONE }

    static class Comment {
        String text;
        List<Comment> replies = new ArrayList<>();
        Comment(String text) { this.text = text; }
    }

    static List<Comment> withoutState(Comment comment) {
        List<Comment> result = new ArrayList<>();
        Deque<Comment> stack = new ArrayDeque<>();
        stack.push(comment);
        while (!stack.isEmpty()) {
            Comment current = stack.pop();
            result.add(current);
            for (Comment reply : current.replies) {
                stack.push(reply);
            }
        }
        return result;
    }

    static List<Comment> withState(Comment comment) {
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

    public static void main(String[] args) {
        Comment c1 = new Comment("Comment1");
        Comment r1 = new Comment("Reply1");
        Comment r2 = new Comment("Reply2");
        Comment sr1 = new Comment("SubReply1");
        r1.replies.add(sr1);
        c1.replies.add(r1);
        c1.replies.add(r2);

        System.out.println("without state: " + withoutState(c1).stream().map(c -> c.text).toList());
        System.out.println("with state:    " + withState(c1).stream().map(c -> c.text).toList());
    }
}