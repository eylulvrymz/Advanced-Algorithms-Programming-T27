import java.util.*;

public class exercise3_3 {

    static class Comment {
        String text;
        List<Comment> replies = new ArrayList<>();
        Comment(String text) { this.text = text; }
    }

    static int countNormal(Comment comment) {
        int total = 1;
        for (Comment reply : comment.replies) {
            total += countNormal(reply);
        }
        return total;
    }

    static int countTail(Comment comment, int accumulator) {
        int total = accumulator + 1;
        for (Comment reply : comment.replies) {
            total = countTail(reply, total);
        }
        return total;
    }

    static int countLoop(Comment comment) {
        int count = 0;
        Deque<Comment> stack = new ArrayDeque<>();
        stack.push(comment);
        while (!stack.isEmpty()) {
            Comment current = stack.pop();
            count++;
            for (Comment reply : current.replies) {
                stack.push(reply);
            }
        }
        return count;
    }

    public static void main(String[] args) {
        Comment c1 = new Comment("Comment1");
        Comment r1 = new Comment("Reply1");
        Comment r2 = new Comment("Reply2");
        Comment sr1 = new Comment("SubReply1");
        r1.replies.add(sr1);
        c1.replies.add(r1);
        c1.replies.add(r2);

        System.out.println("countNormal: " + countNormal(c1));
        System.out.println("countTail:   " + countTail(c1, 0));
        System.out.println("countLoop:   " + countLoop(c1));
    }
}