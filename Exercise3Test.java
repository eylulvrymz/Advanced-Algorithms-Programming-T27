import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class Exercise3Test {

    static int passed = 0;
    static int failed = 0;

    static void check(String name, boolean condition) {
        if (condition) {
            System.out.println("[PASS] " + name);
            passed++;
        } else {
            System.out.println("[FAIL] " + name);
            failed++;
        }
    }

    public static void main(String[] args) {
        testTrie();
        testSegmentTree();
        System.out.println("\n==========================");
        System.out.println("Results: " + passed + " passed, " + failed + " failed");
    }

    static void testTrie() {
        System.out.println("\n=== Trie Tests ===");
        Exercise3AutocompleteTrie trie = new Exercise3AutocompleteTrie();

        trie.insert("alice", 1);
        trie.insert("alice123", 2);
        trie.insert("alice456", 3);
        trie.insert("bob", 4);
        trie.insert("bobby", 5);
        trie.insert("bobcat", 6);

        check("search existing username", Integer.valueOf(1).equals(trie.search("alice")));
        check("search non-existing username", trie.search("xyz") == null);
        check("search partial prefix not a word", trie.search("ali") == null);

        check("startsWith existing prefix", trie.startsWith("ali"));
        check("startsWith full word", trie.startsWith("bob"));
        check("startsWith non-existing", !trie.startsWith("zzz"));

        List<String[]> results = trie.autocomplete("bob", 10);
        check("autocomplete 'bob' returns 3 results", results.size() == 3);

        List<String[]> limited = trie.autocomplete("alice", 2);
        check("autocomplete max_results=2 respected", limited.size() == 2);

        List<String[]> noMatch = trie.autocomplete("xyz", 10);
        check("autocomplete no match returns empty", noMatch.isEmpty());

        check("countWords after 6 inserts", trie.countWords() == 6);

        trie.insert("alice", 99);
        check("duplicate insert does not increase count", trie.countWords() == 6);

        check("getHeight >= longest word length", trie.getHeight() >= "alice456".length());
        check("getTotalNodes > 0", trie.getTotalNodes() > 0);

        trie.delete("alice123");
        check("delete reduces count", trie.countWords() == 5);
        check("deleted word not searchable", trie.search("alice123") == null);
        check("sibling still searchable after delete", trie.search("alice456") != null);

        trie.delete("nonexistent");
        check("delete non-existing does not crash", trie.countWords() == 5);

        Exercise3AutocompleteTrie largeTrie = new Exercise3AutocompleteTrie();
        for (int i = 0; i < 50000; i++) largeTrie.insert("user" + i, i);
        check("insert 50000 usernames", largeTrie.countWords() == 50000);
        List<String[]> bigSearch = largeTrie.autocomplete("user1", 10);
        check("autocomplete on 50000 usernames returns <= 10", bigSearch.size() <= 10);
    }

    static void testSegmentTree() {
        System.out.println("\n=== Segment Tree Tests ===");

        int[] activity = {10, 20, 30, 40, 50, 60, 70, 80};
        Exercise3SegmentTree seg = new Exercise3SegmentTree(activity);

        check("query full range", seg.query(0, 7) == 360);
        check("query single element", seg.query(3, 3) == 40);
        check("query subrange [2,5]", seg.query(2, 5) == 180);
        check("query first half [0,3]", seg.query(0, 3) == 100);
        check("query last half [4,7]", seg.query(4, 7) == 260);

        check("getRangeMax [0,7]", seg.getRangeMax(0, 7) == 80);
        check("getRangeMax [0,3]", seg.getRangeMax(0, 3) == 40);
        check("getRangeMin [0,7]", seg.getRangeMin(0, 7) == 10);
        check("getRangeMin [4,7]", seg.getRangeMin(4, 7) == 50);

        check("getTreeSize = 4n", seg.getTreeSize() == 32);
        check("getHeight > 0", seg.getHeight() > 0);

        int[] leaves = seg.getLeafValues();
        check("getLeafValues length correct", leaves.length == 8);
        check("getLeafValues values correct", Arrays.equals(leaves, activity));

        Random rand = new Random(42);
        int[] days = new int[30];
        for (int i = 0; i < 30; i++) days[i] = rand.nextInt(1001);
        Exercise3SegmentTree segLarge = new Exercise3SegmentTree(days);

        int manualSum = 0;
        for (int i = 23; i <= 29; i++) manualSum += days[i];
        check("7-day rolling total matches manual sum", segLarge.query(23, 29) == manualSum);

        int manualMax = Arrays.stream(days, 23, 30).max().getAsInt();
        check("getRangeMax matches manual max", segLarge.getRangeMax(23, 29) == manualMax);

        int manualMin = Arrays.stream(days, 23, 30).min().getAsInt();
        check("getRangeMin matches manual min", segLarge.getRangeMin(23, 29) == manualMin);

        int[] year = new int[365];
        Arrays.fill(year, 100);
        Exercise3SegmentTree yearSeg = new Exercise3SegmentTree(year);
        check("365-day full query", yearSeg.query(0, 364) == 36500);
        check("365-day tree size = 4*365", yearSeg.getTreeSize() == 1460);
    }
}