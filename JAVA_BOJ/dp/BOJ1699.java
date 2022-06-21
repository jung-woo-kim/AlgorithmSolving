package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ1699 {

    static Integer[] dp;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        dp = new Integer[N+1];

        System.out.println(recur(N));
    }

    static int recur(int n){
        if (dp[n] == null){
            dp[n] = n;
            for (int i = 1; i <= (int)Math.sqrt(n); i++){
                dp[n] = Math.min(recur(n-(i*i)) +1, dp[n]);
            }
        }
        return dp[n];
    }
}
