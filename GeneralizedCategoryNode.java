import java.util.ArrayList;
import java.util.List;

class GeneralizedCategoryNode {
    int category_id;
    String name;
    int post_count;
    List<GeneralizedCategoryNode> children;
    GeneralizedCategoryNode parent;

    public GeneralizedCategoryNode(int category_id, String name, int post_count) {
        this.category_id = category_id;
        this.name = name;
        this.post_count = post_count;
        this.children = new ArrayList<>();
        this.parent = null;
    }
}

class BinaryNode {
    int category_id;
    String name;
    int post_count;
    BinaryNode left, right;

    public BinaryNode(int category_id, String name, int post_count) {
        this.category_id = category_id;
        this.name = name;
        this.post_count = post_count;
    }
}