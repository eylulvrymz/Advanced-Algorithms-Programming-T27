import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Exercise3 {

    private static final Random rand = new Random();

    public static void midpointDisplacement(double x1, double y1, double x2, double y2,
                                            double roughness, int depth, List<double[]> points) {
        if (depth == 0) return;

        double mx = (x1 + x2) / 2.0;
        double my = (y1 + y2) / 2.0 + roughness * (rand.nextDouble() * 2 - 1);

        midpointDisplacement(x1, y1, mx, my, roughness / 2, depth - 1, points);
        points.add(new double[]{mx, my});
        midpointDisplacement(mx, my, x2, y2, roughness / 2, depth - 1, points);
    }

    public static double[][] generateTerrain(int width, int height, double roughness, int depth) {
        double[][] grid = new double[height + 1][width + 1];
        diamondSquare(grid, 0, 0, width, height, roughness, depth);
        return grid;
    }

    private static void diamondSquare(double[][] grid, int x, int y, int w, int h,
                                      double roughness, int depth) {
        if (depth == 0 || w < 2 || h < 2) return;

        int mx = x + w / 2;
        int my = y + h / 2;

        grid[my][mx] = (grid[y][x] + grid[y][x + w] + grid[y + h][x] + grid[y + h][x + w]) / 4.0
                + roughness * (rand.nextDouble() * 2 - 1);

        grid[y][mx]     = (grid[y][x] + grid[y][x + w] + grid[my][mx]) / 3.0
                + roughness * (rand.nextDouble() * 2 - 1);
        grid[y + h][mx] = (grid[y + h][x] + grid[y + h][x + w] + grid[my][mx]) / 3.0
                + roughness * (rand.nextDouble() * 2 - 1);
        grid[my][x]     = (grid[y][x] + grid[y + h][x] + grid[my][mx]) / 3.0
                + roughness * (rand.nextDouble() * 2 - 1);
        grid[my][x + w] = (grid[y][x + w] + grid[y + h][x + w] + grid[my][mx]) / 3.0
                + roughness * (rand.nextDouble() * 2 - 1);

        double newRoughness = roughness / 2;
        diamondSquare(grid, x,  y,  w / 2, h / 2, newRoughness, depth - 1);
        diamondSquare(grid, mx, y,  w / 2, h / 2, newRoughness, depth - 1);
        diamondSquare(grid, x,  my, w / 2, h / 2, newRoughness, depth - 1);
        diamondSquare(grid, mx, my, w / 2, h / 2, newRoughness, depth - 1);
    }

    public static List<int[]> detectArtifacts(double[][] grid, double threshold) {
        List<int[]> suspicious = new ArrayList<>();
        int rows = grid.length;
        int cols = grid[0].length;
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                for (int[] d : dirs) {
                    int ni = i + d[0], nj = j + d[1];
                    if (ni >= 0 && ni < rows && nj >= 0 && nj < cols) {
                        if (Math.abs(grid[i][j] - grid[ni][nj]) > threshold) {
                            suspicious.add(new int[]{i, j});
                            break;
                        }
                    }
                }
            }
        }
        return suspicious;
    }

    public static void main(String[] args) {
        List<double[]> points = new ArrayList<>();
        points.add(new double[]{0, 0});
        midpointDisplacement(0, 0, 8, 0, 1.0, 3, points);
        points.add(new double[]{8, 0});
        System.out.println("Midpoint displacement points: " + points.size());

        double[][] terrain = generateTerrain(8, 8, 1.0, 3);
        System.out.println("Terrain size: " + terrain.length + "x" + terrain[0].length);

        List<int[]> artifacts = detectArtifacts(terrain, 0.5);
        System.out.println("Suspicious cells: " + artifacts.size());
    }
}