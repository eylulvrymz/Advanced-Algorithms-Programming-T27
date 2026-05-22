import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

public class exercise3test {

    private Map<Integer, List<Integer>> buildGraph(int[][] edges, int n) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 1; i <= n; i++) graph.put(i, new ArrayList<>());
        for (int[] e : edges) {
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }
        return graph;
    }

    @Test
    void testCountCrossEdges_basic() {
        Map<Integer, List<Integer>> graph = buildGraph(new int[][]{{1,2},{2,3},{3,4}}, 4);
        List<Integer> groupA = Arrays.asList(1, 2);
        List<Integer> groupB = Arrays.asList(3, 4);
        assertEquals(1, exercise3.countCrossEdges(groupA, groupB, graph));
    }

    @Test
    void testCountCrossEdges_noCrossEdges() {
        Map<Integer, List<Integer>> graph = buildGraph(new int[][]{{1,2},{3,4}}, 4);
        List<Integer> groupA = Arrays.asList(1, 2);
        List<Integer> groupB = Arrays.asList(3, 4);
        assertEquals(0, exercise3.countCrossEdges(groupA, groupB, graph));
    }

    @Test
    void testCountCrossEdges_allCross() {
        Map<Integer, List<Integer>> graph = buildGraph(new int[][]{{1,3},{1,4},{2,3},{2,4}}, 4);
        List<Integer> groupA = Arrays.asList(1, 2);
        List<Integer> groupB = Arrays.asList(3, 4);
        assertEquals(4, exercise3.countCrossEdges(groupA, groupB, graph));
    }

    @Test
    void testGreedy_balanceRespected() {
        Map<Integer, List<Integer>> graph = buildGraph(
                new int[][]{{1,2},{1,3},{2,3},{3,4},{4,5},{4,6},{5,6}}, 6);
        Object[] result = exercise3.findBalancedPartitionGreedy(graph);
        List<Integer> groupA = (List<Integer>) result[1];
        List<Integer> groupB = (List<Integer>) result[2];
        int n = graph.size();
        int minSize = (int) Math.ceil(0.4 * n);
        assertTrue(groupA.size() >= minSize);
        assertTrue(groupB.size() >= minSize);
    }

    @Test
    void testGreedy_crossEdgesNonNegative() {
        Map<Integer, List<Integer>> graph = buildGraph(
                new int[][]{{1,2},{2,3},{3,4},{4,5},{5,6},{6,1}}, 6);
        Object[] result = exercise3.findBalancedPartitionGreedy(graph);
        int cross = (int) result[0];
        assertTrue(cross >= 0);
    }

    @Test
    void testGreedy_allNodesAssigned() {
        Map<Integer, List<Integer>> graph = buildGraph(
                new int[][]{{1,2},{3,4},{5,6},{7,8},{9,10}}, 10);
        Object[] result = exercise3.findBalancedPartitionGreedy(graph);
        List<Integer> groupA = (List<Integer>) result[1];
        List<Integer> groupB = (List<Integer>) result[2];
        Set<Integer> all = new HashSet<>(groupA);
        all.addAll(groupB);
        assertEquals(graph.keySet(), all);
    }

    @Test
    void testLocalSearch_betterOrEqualThanSingleGreedy() {
        Map<Integer, List<Integer>> graph = buildGraph(
                new int[][]{{1,2},{1,3},{2,3},{3,4},{4,5},{4,6},{5,6}}, 6);
        Object[] single = exercise3.findBalancedPartitionGreedy(graph);
        Object[] multi = exercise3.findBalancedPartitionLocalSearch(graph, 20);
        assertTrue((int) multi[0] <= (int) single[0]);
    }

    @Test
    void testLocalSearch_emptyGraph() {
        Map<Integer, List<Integer>> graph = buildGraph(new int[][]{}, 6);
        for (int i = 1; i <= 6; i++) graph.put(i, new ArrayList<>());
        Object[] result = exercise3.findBalancedPartitionLocalSearch(graph, 10);
        assertEquals(0, (int) result[0]);
    }

    @Test
    void testLocalSearch_singleIteration() {
        Map<Integer, List<Integer>> graph = buildGraph(
                new int[][]{{1,2},{2,3},{3,4},{4,5}}, 5);
        Object[] result = exercise3.findBalancedPartitionLocalSearch(graph, 1);
        assertNotNull(result[1]);
        assertNotNull(result[2]);
    }
}