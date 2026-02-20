public class Exercise4 {

    static boolean[][] matrix; //
    static int N;              // 用户总数

    public static void init(int n) {
        N = n;
        matrix = new boolean[N + 1][N + 1]; // 下标从1开始，所以+1
    }

    public static void follow(int follower, int followee) {
        matrix[follower][followee] = true;
    }

    public static void unfollow(int follower, int followee) {
        matrix[follower][followee] = false;
    }

    public static boolean isFollowing(int follower, int followee) {
        return matrix[follower][followee];
    }

    // 获取粉丝列表（谁关注了我）
    public static void getFollowers(int user) {
        System.out.print("Followers of User" + user + ": ");
        for (int i = 1; i <= N; i++) {
            if (matrix[i][user]) {  // i关注了user
                System.out.print("User" + i + " ");
            }
        }
        System.out.println();
    }

    // 获取关注列表（我关注了谁）
    public static void getFollowing(int user) {
        System.out.print("User" + user + " follows: ");
        for (int j = 1; j <= N; j++) {
            if (matrix[user][j]) {  // 第user行第j列 = user关注了j
                System.out.print("User" + j + " ");
            }
        }
        System.out.println();
    }

    // 找出所有互关对
    public static void findMutualFollows() {
        System.out.println("Mutual follow pairs:");
        for (int i = 1; i <= N; i++) {
            for (int j = i + 1; j <= N; j++) {
                if (matrix[i][j] && matrix[j][i]) {
                    System.out.println("  User" + i + " <-> User" + j);
                }
            }
        }
    }

    // 计算影响力分数
    public static double influenceScore(int user) {
        int followerCount  = 0;
        int followingCount = 0;

        for (int i = 1; i <= N; i++) {
            if (matrix[i][user]) followerCount++;   // 看列：谁关注了我
            if (matrix[user][i]) followingCount++;  // 看行：我关注了谁
        }

        return (double)(followerCount + followingCount) / N;
    }

    // 打印整个矩阵
    public static void printMatrix() {
        System.out.print("   ");
        for (int j = 1; j <= N; j++) System.out.print(" " + j);
        System.out.println();
        for (int i = 1; i <= N; i++) {
            System.out.print(i + ": ");
            for (int j = 1; j <= N; j++) {
                System.out.print(" " + (matrix[i][j] ? "T" : "F"));
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        init(3);

        // 构建题目例子
        follow(1, 2);  // User1 关注 User2
        follow(2, 1);  // User2 关注 User1
        follow(2, 3);  // User2 关注 User3

        System.out.println("=== Follow Matrix ===");
        printMatrix();

        System.out.println("\n=== Relationships ===");
        getFollowers(2);
        getFollowing(2);

        System.out.println("\n=== Mutual Follows ===");
        findMutualFollows();

        System.out.println("\n=== Influence Scores ===");
        for (int i = 1; i <= N; i++) {
            System.out.printf("User%d: %.4f%n", i, influenceScore(i));
        }


    }
}