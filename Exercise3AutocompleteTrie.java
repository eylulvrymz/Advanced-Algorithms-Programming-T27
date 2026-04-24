import java.util.ArrayList;
import java.util.List;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Exercise3AutocompleteTrie {
    private final Exercise3TrieNode root = new Exercise3TrieNode();
    private int count = 0;

    public void insert(String username, int userId) {
        Exercise3TrieNode cur = root;
        for (char c : username.toCharArray()) {
            cur.children.putIfAbsent(c, new Exercise3TrieNode());
            cur = cur.children.get(c);
        }
        if (!cur.isEnd) count++;
        cur.isEnd = true;
        cur.userId = userId;
    }

    public Integer search(String username) {
        Exercise3TrieNode cur = navigate(username);
        return (cur != null && cur.isEnd) ? cur.userId : null;
    }

    public boolean startsWith(String prefix) {
        return navigate(prefix) != null;
    }

    private Exercise3TrieNode navigate(String s) {
        Exercise3TrieNode cur = root;
        for (char c : s.toCharArray()) {
            if (!cur.children.containsKey(c)) return null;
            cur = cur.children.get(c);
        }
        return cur;
    }

    public List<String[]> autocomplete(String prefix, int maxResults) {
        List<String[]> res = new ArrayList<>();
        Exercise3TrieNode node = navigate(prefix);
        if (node != null) dfs(node, new StringBuilder(prefix), res, maxResults);
        return res;
    }

    private void dfs(Exercise3TrieNode node, StringBuilder sb, List<String[]> res, int max) {
        if (res.size() >= max) return;
        if (node.isEnd) res.add(new String[]{sb.toString(), String.valueOf(node.userId)});
        for (Map.Entry<Character, Exercise3TrieNode> e : node.children.entrySet()) {
            sb.append(e.getKey());
            dfs(e.getValue(), sb, res, max);
            sb.deleteCharAt(sb.length() - 1);
        }
    }

    public int countWords() { return count; }

    public int getHeight() { return height(root); }
    private int height(Exercise3TrieNode n) {
        return n.children.isEmpty() ? 0 : 1 + n.children.values().stream().mapToInt(this::height).max().orElse(0);
    }

    public int getTotalNodes() { return totalNodes(root); }
    private int totalNodes(Exercise3TrieNode n) {
        return 1 + n.children.values().stream().mapToInt(this::totalNodes).sum();
    }

    public boolean delete(String username) { return delete(root, username, 0); }
    private boolean delete(Exercise3TrieNode node, String s, int i) {
        if (i == s.length()) {
            if (!node.isEnd) return false;
            node.isEnd = false;
            count--;
            return node.children.isEmpty();
        }
        char c = s.charAt(i);
        if (!node.children.containsKey(c)) return false;
        if (delete(node.children.get(c), s, i + 1)) node.children.remove(c);
        return !node.isEnd && node.children.isEmpty();
    }
}