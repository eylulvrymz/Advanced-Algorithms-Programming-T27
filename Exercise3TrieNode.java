import java.util.HashMap;
import java.util.Map;

public class Exercise3TrieNode {
    Map<Character, Exercise3TrieNode> children = new HashMap<>();
    boolean isEnd = false;
    int userId = -1;
}