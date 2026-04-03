import java.util.*;

public class Exercise3 {

    public static GeneralizedCategoryNode binary_to_generalized(BinaryNode root) {
        if (root == null) return null;
        GeneralizedCategoryNode gen = new GeneralizedCategoryNode(root.category_id, root.name, root.post_count);
        if (root.left  != null) { GeneralizedCategoryNode c = binary_to_generalized(root.left);  c.parent = gen; gen.children.add(c); }
        if (root.right != null) { GeneralizedCategoryNode c = binary_to_generalized(root.right); c.parent = gen; gen.children.add(c); }
        return gen;
    }

    public static BinaryNode generalized_to_binary(GeneralizedCategoryNode root) {
        if (root == null) return null;
        BinaryNode node = new BinaryNode(root.category_id, root.name, root.post_count);
        if (!root.children.isEmpty()) {
            node.left = generalized_to_binary(root.children.get(0));
            BinaryNode cur = node.left;
            for (int i = 1; i < root.children.size(); i++) { cur.right = generalized_to_binary(root.children.get(i)); cur = cur.right; }
        }
        return node;
    }

    public static List<String> pre_order_generalized(GeneralizedCategoryNode node) {
        List<String> res = new ArrayList<>();
        if (node == null) return res;
        res.add(node.name);
        for (GeneralizedCategoryNode c : node.children) res.addAll(pre_order_generalized(c));
        return res;
    }

    public static List<String> post_order_generalized(GeneralizedCategoryNode node) {
        List<String> res = new ArrayList<>();
        if (node == null) return res;
        for (GeneralizedCategoryNode c : node.children) res.addAll(post_order_generalized(c));
        res.add(node.name);
        return res;
    }

    public static List<String> level_order_generalized(GeneralizedCategoryNode node) {
        List<String> res = new ArrayList<>();
        if (node == null) return res;
        Queue<GeneralizedCategoryNode> q = new LinkedList<>();
        q.offer(node);
        while (!q.isEmpty()) {
            GeneralizedCategoryNode cur = q.poll();
            res.add(cur.name);
            for (GeneralizedCategoryNode c : cur.children) q.offer(c);
        }
        return res;
    }

    public static int calculate_fan_out(GeneralizedCategoryNode node) {
        if (node == null) return 0;
        int max = node.children.size();
        for (GeneralizedCategoryNode c : node.children) max = Math.max(max, calculate_fan_out(c));
        return max;
    }

    public static int calculate_height_generalized(GeneralizedCategoryNode node) {
        if (node == null || node.children.isEmpty()) return 0;
        int max = 0;
        for (GeneralizedCategoryNode c : node.children) max = Math.max(max, calculate_height_generalized(c));
        return 1 + max;
    }

    public static int count_nodes_generalized(GeneralizedCategoryNode node) {
        if (node == null) return 0;
        int count = 1;
        for (GeneralizedCategoryNode c : node.children) count += count_nodes_generalized(c);
        return count;
    }

    public static int count_leaves_generalized(GeneralizedCategoryNode node) {
        if (node == null) return 0;
        if (node.children.isEmpty()) return 1;
        int count = 0;
        for (GeneralizedCategoryNode c : node.children) count += count_leaves_generalized(c);
        return count;
    }

    public static double calculate_branching_factor(GeneralizedCategoryNode node) {
        int[] acc = {0, 0};
        branchingHelper(node, acc);
        return acc[1] == 0 ? 0.0 : (double) acc[0] / acc[1];
    }

    private static void branchingHelper(GeneralizedCategoryNode node, int[] acc) {
        if (node == null || node.children.isEmpty()) return;
        acc[0] += node.children.size();
        acc[1]++;
        for (GeneralizedCategoryNode c : node.children) branchingHelper(c, acc);
    }

    public static void main(String[] args) {
        GeneralizedCategoryNode root     = new GeneralizedCategoryNode(1,  "Technology",  0);
        GeneralizedCategoryNode prog     = new GeneralizedCategoryNode(2,  "Programming", 150);
        GeneralizedCategoryNode design   = new GeneralizedCategoryNode(3,  "Design",       80);
        GeneralizedCategoryNode business = new GeneralizedCategoryNode(4,  "Business",    200);
        GeneralizedCategoryNode python   = new GeneralizedCategoryNode(5,  "Python",      100);
        GeneralizedCategoryNode java_n   = new GeneralizedCategoryNode(6,  "Java",         50);
        GeneralizedCategoryNode uiux     = new GeneralizedCategoryNode(7,  "UI/UX",        60);
        GeneralizedCategoryNode graphics = new GeneralizedCategoryNode(8,  "Graphics",     20);
        GeneralizedCategoryNode finance  = new GeneralizedCategoryNode(9,  "Finance",      90);
        GeneralizedCategoryNode mkt      = new GeneralizedCategoryNode(10, "Marketing",    70);
        GeneralizedCategoryNode hr       = new GeneralizedCategoryNode(11, "HR",           40);
        GeneralizedCategoryNode django   = new GeneralizedCategoryNode(12, "Django",       30);
        GeneralizedCategoryNode flask    = new GeneralizedCategoryNode(13, "Flask",        25);

        root.children.addAll(Arrays.asList(prog, design, business));
        prog.children.addAll(Arrays.asList(python, java_n));
        python.children.addAll(Arrays.asList(django, flask));
        design.children.addAll(Arrays.asList(uiux, graphics));
        business.children.addAll(Arrays.asList(finance, mkt, hr));

        System.out.println("Pre-order    : " + pre_order_generalized(root));
        System.out.println("Post-order   : " + post_order_generalized(root));
        System.out.println("Level-order  : " + level_order_generalized(root));
        System.out.println("Fan-out      : " + calculate_fan_out(root));
        System.out.println("Height       : " + calculate_height_generalized(root));
        System.out.println("Node count   : " + count_nodes_generalized(root));
        System.out.println("Leaf count   : " + count_leaves_generalized(root));
        System.out.printf ("Branching    : %.2f%n", calculate_branching_factor(root));

        BinaryNode bin = new BinaryNode(2, "Programming", 150);
        bin.left  = new BinaryNode(5, "Python", 100);
        bin.right = new BinaryNode(3, "Design",  80);
        GeneralizedCategoryNode gen = binary_to_generalized(bin);
        System.out.println("bin→gen children: " + gen.children.stream().map(c -> c.name).toList());

        BinaryNode bRoot = generalized_to_binary(root);
        System.out.println("gen→bin left            : " + bRoot.left.name);
        System.out.println("gen→bin left.right      : " + bRoot.left.right.name);
        System.out.println("gen→bin left.right.right: " + bRoot.left.right.right.name);
    }
}