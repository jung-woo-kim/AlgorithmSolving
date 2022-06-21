package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ2225 {

    static long[][] dp;
    static int k;
    static int total;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        dp = new long[k+1][N+1];

        dp[1][0] = 1L;


        System.out.println(recur(k,N));

    }

    static Long recur(int k,int n){

        if(dp[k][n] > 0) return dp[k][n];
        if(n == 0 || k == 1) return dp[k][n] = 1L;




        for(int m=n; m >= 0; m--){
            dp[k][n] += recur(k-1, m);
            dp[k][n] %= 1000000000;
        }



        return dp[k][n];
    }
}
