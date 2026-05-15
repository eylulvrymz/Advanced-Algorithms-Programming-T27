import java.util.*;

public class exercise3 {

    static int[] maximize_reach(int budget, int[] costs, int[] influences) {
        int N = costs.length;
        int[][] dp = new int[N + 1][budget + 1];

        for (int i = 1; i <= N; i++)
            for (int b = 0; b <= budget; b++) {
                dp[i][b] = dp[i - 1][b];
                if (costs[i - 1] <= b)
                    dp[i][b] = Math.max(dp[i][b], dp[i - 1][b - costs[i - 1]] + influences[i - 1]);
            }

        List<Integer> selected = new ArrayList<>();
        int b = budget;
        for (int i = N; i >= 1; i--)
            if (dp[i][b] != dp[i - 1][b]) {
                selected.add(i - 1);
                b -= costs[i - 1];
            }

        System.out.println("Max influence (DP): " + dp[N][budget]);
        System.out.println("Selected users: " + selected);
        return new int[]{dp[N][budget]};
    }

    static boolean is_within_budget(List<Integer> selection, int[] costs, int budget) {
        int total = 0;
        for (int i : selection) total += costs[i];
        return total <= budget;
    }

    static void fast_alternative_strategy(int budget, int[] costs, int[] influences) {
        int N = costs.length;
        Integer[] idx = new Integer[N];
        for (int i = 0; i < N; i++) idx[i] = i;
        Arrays.sort(idx, (a, b) -> Double.compare((double) influences[b] / costs[b], (double) influences[a] / costs[a]));

        int total = 0, totalInf = 0;
        List<Integer> selected = new ArrayList<>();
        for (int i : idx)
            if (total + costs[i] <= budget) {
                selected.add(i);
                total += costs[i];
                totalInf += influences[i];
            }

        System.out.println("Max influence (Greedy): " + totalInf);
        System.out.println("Selected users: " + selected);
    }

    public static void main(String[] args) {
        int budget = 10;
        int[] costs     = {2, 3, 4, 5};
        int[] influences = {3, 4, 5, 6};

        System.out.println("=== DP ===");
        int[] result = maximize_reach(budget, costs, influences);

        System.out.println("\n=== Budget Check ===");
        List<Integer> sel = List.of(0, 1, 2);
        System.out.println("Within budget: " + is_within_budget(sel, costs, budget));

        System.out.println("\n=== Greedy ===");
        fast_alternative_strategy(budget, costs, influences);

        System.out.println("\n=== Counterexample ===");
        int[] c2 = {1, 5};
        int[] inf2 = {2, 6};
        System.out.println("-- DP --");
        maximize_reach(5, c2, inf2);
        System.out.println("-- Greedy --");
        fast_alternative_strategy(5, c2, inf2);
    }
}