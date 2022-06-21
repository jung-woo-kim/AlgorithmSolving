package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ9095 {

    static Integer[] dp;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        dp = new Integer[12];

        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;

        int[] list = new int[N];

        for (int i = 0; i < N; i++){
            list[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 0; i < N; i++){
            sb.append(dp(list[i])).append('\n');
        }

        System.out.println(sb);

    }

    static int dp(int n){
        if (dp[n] == null){
            dp[n] = dp(n-1) + dp(n-2) + dp(n-3);
        }
        return dp[n];
    }
}
