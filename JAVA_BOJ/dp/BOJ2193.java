package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ2193 {

    static Long[][] dp;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        dp = new Long[91][2];

        dp[1][0] = 0L;
        dp[1][1] = 1L;

        dp[2][0] = 1L;
        dp[2][1] = 0L;

        Long sum = recur(N,0) + recur(N,1);

        System.out.println(sum);


    }

    static Long recur(int n, int val){

        if (dp[n][val] == null){
            if (val == 0){
                dp[n][val] = recur(n-1,1) + recur(n-1,0);
            }else{
                dp[n][val] = recur(n-1,0);
            }

        }
        return dp[n][val];

    }
}
