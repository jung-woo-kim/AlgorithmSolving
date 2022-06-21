package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ11726 {

    static Integer[] dp;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        dp = new Integer[1001];

        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 3;

        System.out.println(dp(N));


    }

    static int dp(int n){
        if (dp[n] == null){
            dp[n] = (dp(n-1) + dp(n-2)) % 10007;
        }
        return dp[n];
    }
}
