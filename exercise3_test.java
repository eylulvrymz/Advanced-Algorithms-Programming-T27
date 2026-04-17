import java.util.ArrayList;
import java.util.List;

public class exercise3_test {

    static int passed = 0;
    static int failed = 0;

    public static void main(String[] args) {
        testMidpointDisplacementDepthZero();
        testMidpointDisplacementPointCount();
        testMidpointDisplacementRoughnessZero();
        testGenerateTerrainSize();
        testGenerateTerrainCornersAreZero();
        testGenerateTerrainRoughnessZero();
        testDetectArtifactsNone();
        testDetectArtifactsAll();
        testDetectArtifactsThreshold();

        System.out.println("\n=== Results: " + passed + " passed, " + failed + " failed ===");
    }

    static void assertTrue(String testName, boolean condition) {
        if (condition) {
            System.out.println("[PASS] " + testName);
            passed++;
        } else {
            System.out.println("[FAIL] " + testName);
            failed++;
        }
    }

    static void testMidpointDisplacementDepthZero() {
        List<double[]> points = new ArrayList<>();
        Exercise3.midpointDisplacement(0, 0, 8, 0, 1.0, 0, points);
        assertTrue("midpointDisplacement depth=0 adds no points", points.size() == 0);
    }

    static void testMidpointDisplacementPointCount() {
        List<double[]> points = new ArrayList<>();
        Exercise3.midpointDisplacement(0, 0, 8, 0, 1.0, 3, points);
        assertTrue("midpointDisplacement depth=3 adds 2^3 - 1 = 7 points", points.size() == 7);
    }

    static void testMidpointDisplacementRoughnessZero() {
        List<double[]> points = new ArrayList<>();
        Exercise3.midpointDisplacement(0, 0, 8, 0, 0.0, 3, points);
        boolean allYZero = points.stream().allMatch(p -> p[1] == 0.0);
        assertTrue("midpointDisplacement roughness=0 all y=0", allYZero);
    }

    static void testGenerateTerrainSize() {
        double[][] terrain = Exercise3.generateTerrain(8, 8, 1.0, 3);
        assertTrue("generateTerrain returns (height+1) x (width+1) grid",
                terrain.length == 9 && terrain[0].length == 9);
    }

    static void testGenerateTerrainCornersAreZero() {
        double[][] terrain = Exercise3.generateTerrain(8, 8, 1.0, 3);
        assertTrue("generateTerrain 4 corners are 0",
                terrain[0][0] == 0 && terrain[0][8] == 0 &&
                        terrain[8][0] == 0 && terrain[8][8] == 0);
    }

    static void testGenerateTerrainRoughnessZero() {
        double[][] terrain = Exercise3.generateTerrain(8, 8, 0.0, 3);
        boolean allZero = true;
        for (double[] row : terrain)
            for (double v : row)
                if (v != 0.0) { allZero = false; break; }
        assertTrue("generateTerrain roughness=0 all values are 0", allZero);
    }

    static void testDetectArtifactsNone() {
        double[][] flat = new double[4][4];
        List<int[]> result = Exercise3.detectArtifacts(flat, 0.5);
        assertTrue("detectArtifacts flat grid returns no artifacts", result.isEmpty());
    }

    static void testDetectArtifactsAll() {
        double[][] grid = {
                {0.0, 10.0},
                {10.0, 0.0}
        };
        List<int[]> result = Exercise3.detectArtifacts(grid, 0.5);
        assertTrue("detectArtifacts high contrast grid flags all cells", result.size() == 4);
    }

    static void testDetectArtifactsThreshold() {
        double[][] grid = {
                {0.0, 0.3, 0.0},
                {0.0, 5.0, 0.0},
                {0.0, 0.3, 0.0}
        };
        List<int[]> result = Exercise3.detectArtifacts(grid, 1.0);
        boolean centerFlagged = result.stream().anyMatch(c -> c[0] == 1 && c[1] == 1);
        assertTrue("detectArtifacts flags spike cell at center", centerFlagged);
    }
}