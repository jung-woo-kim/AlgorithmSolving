package dfs;

import java.util.Scanner;

public class DFS2 {

    public static int[] arr;
    public static boolean[] visit;

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int N = in.nextInt();
        int M = in.nextInt();

        arr = new int[M];
        visit = new boolean[N];

        dfs(0, N,M,0);

    }

    public static void dfs(int start,int N,int M ,int depth) {

        if (depth == M) {
            for (int val : arr) {
                System.out.print(val + " ");
            }
            System.out.println();
            return;

        }

        for (int i = start; i < N; i++) {

            arr[depth] = i + 1;
            dfs(i+1, N, M, depth + 1);

        }
    }

}