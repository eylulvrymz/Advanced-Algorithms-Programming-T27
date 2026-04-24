public class Exercise3SegmentTree {
    private final int[] sum, max, min;
    private final int n;

    public Exercise3SegmentTree(int[] arr) {
        n = arr.length;
        sum = new int[4 * n];
        max = new int[4 * n];
        min = new int[4 * n];
        build(arr, 1, 0, n - 1);
    }

    private void build(int[] arr, int v, int l, int r) {
        if (l == r) { sum[v] = max[v] = min[v] = arr[l]; return; }
        int m = (l + r) / 2;
        build(arr, 2 * v, l, m);
        build(arr, 2 * v + 1, m + 1, r);
        pushUp(v);
    }

    private void pushUp(int v) {
        sum[v] = sum[2 * v] + sum[2 * v + 1];
        max[v] = Math.max(max[2 * v], max[2 * v + 1]);
        min[v] = Math.min(min[2 * v], min[2 * v + 1]);
    }

    public int query(int l, int r) { return qSum(1, 0, n - 1, l, r); }
    private int qSum(int v, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) return 0;
        if (ql <= l && r <= qr) return sum[v];
        int m = (l + r) / 2;
        return qSum(2 * v, l, m, ql, qr) + qSum(2 * v + 1, m + 1, r, ql, qr);
    }

    public int getRangeMax(int l, int r) { return qMax(1, 0, n - 1, l, r); }
    private int qMax(int v, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) return Integer.MIN_VALUE;
        if (ql <= l && r <= qr) return max[v];
        int m = (l + r) / 2;
        return Math.max(qMax(2 * v, l, m, ql, qr), qMax(2 * v + 1, m + 1, r, ql, qr));
    }

    public int getRangeMin(int l, int r) { return qMin(1, 0, n - 1, l, r); }
    private int qMin(int v, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) return Integer.MAX_VALUE;
        if (ql <= l && r <= qr) return min[v];
        int m = (l + r) / 2;
        return Math.min(qMin(2 * v, l, m, ql, qr), qMin(2 * v + 1, m + 1, r, ql, qr));
    }

    public int getTreeSize() { return 4 * n; }
    public int getHeight() { return (int) Math.ceil(Math.log(n) / Math.log(2)) + 1; }

    public int[] getLeafValues() {
        int[] leaves = new int[n];
        collectLeaves(1, 0, n - 1, leaves);
        return leaves;
    }
    private void collectLeaves(int v, int l, int r, int[] leaves) {
        if (l == r) { leaves[l] = sum[v]; return; }
        int m = (l + r) / 2;
        collectLeaves(2 * v, l, m, leaves);
        collectLeaves(2 * v + 1, m + 1, r, leaves);
    }
}