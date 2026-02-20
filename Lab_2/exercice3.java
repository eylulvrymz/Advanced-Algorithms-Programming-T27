import java.util.Arrays;

public class Exercise3 {

    // 计算两个用户向量的余弦相似度
    public static double cosineSimilarity(int[] userA, int[] userB) {
        double dot   = 0;
        double normA = 0;
        double normB = 0;

        for (int i = 0; i < userA.length; i++) {
            dot   += userA[i] * userB[i];
            normA += userA[i] * userA[i];
            normB += userB[i] * userB[i];
        }

        if (normA == 0 || normB == 0) return 0.0;
        return dot / (Math.sqrt(normA) * Math.sqrt(normB));
    }

    // 为目标用户推荐Top-K好友
    // alreadyFriends[i] = true 表示用户i已经是朋友
    public static void recommendTopK(int[][] matrix, boolean[] alreadyFriends,
                                     int targetUser, int k) {

        int U = matrix.length;

        // 用二维数组存
        double[] scores = new double[U];
        int[]    ids    = new int[U];

        for (int v = 0; v < U; v++) {
            ids[v] = v;
            if (v == targetUser || alreadyFriends[v]) {
                scores[v] = -1; // 排除自己和已有朋友
            } else {
                scores[v] = cosineSimilarity(matrix[targetUser], matrix[v]);
            }
        }

        // 简单选择排序，找出Top-K
        System.out.println("Top-" + k + " recommendations for User" + targetUser + ":");
        for (int i = 0; i < k; i++) {
            int    maxIdx   = 0;
            double maxScore = scores[0];
            for (int j = 1; j < U; j++) {
                if (scores[j] > maxScore) {
                    maxScore = scores[j];
                    maxIdx   = j;
                }
            }
            System.out.printf("  User%d  similarity=%.4f%n", ids[maxIdx], maxScore);
            scores[maxIdx] = -1; // 已经选出，标记为已用
        }
    }


    // interestNames 是兴趣名称数组
    public static void collaborativeFilter(int[][] matrix, int targetUser,
                                           String[] interestNames) {

        int U = matrix.length;
        int I = interestNames.length;

        System.out.println("\nCollaborative filtering for User" + targetUser + ":");

        for (int j = 0; j < I; j++) {

            if (matrix[targetUser][j] == 0) {
                double weightedSum = 0;
                double simSum      = 0;

                for (int v = 0; v < U; v++) {
                    if (v != targetUser && matrix[v][j] > 0) {
                        double sim = cosineSimilarity(matrix[targetUser], matrix[v]);
                        weightedSum += sim * matrix[v][j];
                        simSum      += sim;
                    }
                }

                if (simSum > 0) {
                    double predicted = weightedSum / simSum;
                    System.out.printf("  Interest '%s': predicted score=%.2f%n",
                            interestNames[j], predicted);
                }
            }
        }
    }

    public static void main(String[] args) {
        String[] interests = {"Music", "Sports", "Tech", "Fashion", "Travel", "Food"};

        int[][] matrix = {
                {10, 0, 8, 2, 5, 7},  // User0
                { 9, 1, 7, 3, 6, 8},  // User1
                { 2, 9, 1, 8, 3, 0},  // User2
                { 8, 2, 9, 1, 4, 6}   // User3（
        };

        // 打印两两相似度
        System.out.println("=== Pairwise Similarities ===");
        for (int i = 0; i < matrix.length; i++) {
            for (int j = i + 1; j < matrix.length; j++) {
                System.out.printf("Similarity(User%d, User%d) = %.4f%n",
                        i, j, cosineSimilarity(matrix[i], matrix[j]));
            }
        }


        boolean[] alreadyFriends = {false, false, false, false};
        System.out.println("\n=== Friend Recommendations ===");
        recommendTopK(matrix, alreadyFriends, 0, 2);

        // 协同过滤推荐
        collaborativeFilter(matrix, 0, interests);
    }
}