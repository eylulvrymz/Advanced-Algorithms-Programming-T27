import java.util.*;

public class exercise3 {

    static int countCrossEdges(List<Integer> groupA, List<Integer> groupB, Map<Integer, List<Integer>> graph) {
        Set<Integer> setB = new HashSet<>(groupB);
        int count = 0;
        for (int u : groupA)
            for (int v : graph.getOrDefault(u, Collections.emptyList()))
                if (setB.contains(v)) count++;
        return count;
    }

    static Object[] findBalancedPartitionGreedy(Map<Integer, List<Integer>> graph) {
        List<Integer> nodes = new ArrayList<>(graph.keySet());
        Collections.shuffle(nodes);
        int n = nodes.size();
        int minSize = (int) Math.ceil(0.4 * n);

        List<Integer> groupA = new ArrayList<>(nodes.subList(0, n / 2));
        List<Integer> groupB = new ArrayList<>(nodes.subList(n / 2, n));
        int bestCross = countCrossEdges(groupA, groupB, graph);
        boolean improved = true;

        while (improved) {
            improved = false;
            List<Integer> all = new ArrayList<>(groupA);
            all.addAll(groupB);
            for (int u : all) {
                List<Integer> newA = new ArrayList<>(groupA);
                List<Integer> newB = new ArrayList<>(groupB);
                if (groupA.contains(u)) { newA.remove((Integer) u); newB.add(u); }
                else { newB.remove((Integer) u); newA.add(u); }

                if (newA.size() < minSize || newB.size() < minSize) continue;

                int newCross = countCrossEdges(newA, newB, graph);
                if (newCross < bestCross) {
                    groupA = newA;
                    groupB = newB;
                    bestCross = newCross;
                    improved = true;
                    break;
                }
            }
        }
        return new Object[]{bestCross, groupA, groupB};
    }

    static Object[] findBalancedPartitionLocalSearch(Map<Integer, List<Integer>> graph, int iterations) {
        int bestCross = Integer.MAX_VALUE;
        List<Integer> bestA = null, bestB = null;

        for (int i = 0; i < iterations; i++) {
            Object[] result = findBalancedPartitionGreedy(graph);
            int cross = (int) result[0];
            if (cross < bestCross) {
                bestCross = cross;
                bestA = (List<Integer>) result[1];
                bestB = (List<Integer>) result[2];
            }
        }
        return new Object[]{bestCross, bestA, bestB};
    }

    public static void main(String[] args) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 1; i <= 6; i++) graph.put(i, new ArrayList<>());
        int[][] edges = {{1,2},{1,3},{2,3},{3,4},{4,5},{4,6},{5,6}};
        for (int[] e : edges) {
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }

        Object[] result = findBalancedPartitionLocalSearch(graph, 20);
        System.out.println("Cross edges: " + result[0]);
        System.out.println("Group A: " + result[1]);
        System.out.println("Group B: " + result[2]);
    }
}