import java.util.*;

public class exercise3Test {

    static int testsPassed = 0;
    static int testsFailed = 0;

    static void check(String name, boolean condition) {
        if (condition) {
            System.out.println("[PASS] " + name);
            testsPassed++;
        } else {
            System.out.println("[FAIL] " + name);
            testsFailed++;
        }
    }

    static int[] runDP(int budget, int[] costs, int[] influences) {
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
        int totalCost = selected.stream().mapToInt(i -> costs[i]).sum();
        return new int[]{dp[N][budget], totalCost};
    }

    static boolean runBudgetCheck(List<Integer> selection, int[] costs, int budget) {
        int total = 0;
        for (int i : selection) total += costs[i];
        return total <= budget;
    }

    static int[] runGreedy(int budget, int[] costs, int[] influences) {
        int N = costs.length;
        Integer[] idx = new Integer[N];
        for (int i = 0; i < N; i++) idx[i] = i;
        Arrays.sort(idx, (a, c) -> Double.compare((double) influences[c] / costs[c], (double) influences[a] / costs[a]));
        int total = 0, totalInf = 0;
        for (int i : idx)
            if (total + costs[i] <= budget) {
                total += costs[i];
                totalInf += influences[i];
            }
        return new int[]{totalInf, total};
    }

    public static void main(String[] args) {
        System.out.println("========== exercise3 Tests ==========\n");

        System.out.println("--- maximize_reach (DP) ---");
        int[] r1 = runDP(10, new int[]{2, 3, 4, 5}, new int[]{3, 4, 5, 6});
        check("basic: max influence = 13", r1[0] == 13);
        check("basic: total cost <= 10", r1[1] <= 10);

        int[] r2 = runDP(0, new int[]{1, 2}, new int[]{3, 4});
        check("zero budget: influence = 0", r2[0] == 0);

        int[] r3 = runDP(100, new int[]{1, 2, 3}, new int[]{10, 20, 30});
        check("large budget: picks all", r3[0] == 60);

        int[] r4 = runDP(5, new int[]{1, 5}, new int[]{2, 6});
        check("counterexample: DP picks user1 (inf=6)", r4[0] == 6);

        int[] r5 = runDP(3, new int[]{4, 5}, new int[]{10, 20});
        check("no item fits: influence = 0", r5[0] == 0);

        int[] r6 = runDP(4, new int[]{4}, new int[]{7});
        check("single item fits exactly", r6[0] == 7);

        int[] r7 = runDP(3, new int[]{4}, new int[]{7});
        check("single item does not fit", r7[0] == 0);

        System.out.println("\n--- is_within_budget ---");
        int[] costs = {2, 3, 4, 5};
        check("within budget: [0,1] cost=5 <= 10", runBudgetCheck(List.of(0, 1), costs, 10));
        check("exactly at budget: [0,1,2,3] cost=14 <= 14", runBudgetCheck(List.of(0, 1, 2, 3), costs, 14));
        check("over budget: [0,1,2,3] cost=14 > 13", !runBudgetCheck(List.of(0, 1, 2, 3), costs, 13));
        check("empty selection: cost=0 <= 0", runBudgetCheck(new ArrayList<>(), costs, 0));

        System.out.println("\n--- fast_alternative_strategy (Greedy) ---");
        int[] g1 = runGreedy(10, new int[]{2, 3, 4, 5}, new int[]{3, 4, 5, 6});
        check("greedy result <= budget", g1[1] <= 10);
        check("greedy influence > 0", g1[0] > 0);

        int[] g2 = runGreedy(0, new int[]{1, 2}, new int[]{3, 4});
        check("zero budget greedy: influence = 0", g2[0] == 0);

        int[] g3 = runGreedy(5, new int[]{1, 5}, new int[]{2, 6});
        check("counterexample: greedy picks user0 (inf=2, suboptimal)", g3[0] == 2);

        int[] g4 = runGreedy(100, new int[]{1, 2, 3}, new int[]{10, 20, 30});
        check("large budget greedy: picks all (inf=60)", g4[0] == 60);

        System.out.println("\n--- DP vs Greedy comparison ---");
        int[] dp5 = runDP(5, new int[]{1, 5}, new int[]{2, 6});
        int[] gr5 = runGreedy(5, new int[]{1, 5}, new int[]{2, 6});
        check("DP >= Greedy on counterexample", dp5[0] >= gr5[0]);

        int[] dp6 = runDP(10, new int[]{2, 3, 4, 5}, new int[]{3, 4, 5, 6});
        int[] gr6 = runGreedy(10, new int[]{2, 3, 4, 5}, new int[]{3, 4, 5, 6});
        check("DP >= Greedy on basic case", dp6[0] >= gr6[0]);

        System.out.println("\n========== Results ==========");
        System.out.println("Passed: " + testsPassed);
        System.out.println("Failed: " + testsFailed);
        System.out.println("Total:  " + (testsPassed + testsFailed));
    }
}