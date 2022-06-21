package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ11057 {

    static Integer[][] dp;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        dp = new Integer[1001][10];


        for (int i = 0; i < 10; i++){
            dp[1][i] = 1;
        }
        int sum = 0;

        for (int i = 0; i < 10; i++){
            sum += recur(N,i);
        }
        System.out.println(sum % 10007);

    }

    static int recur(int n,int val){
        if (dp[n][val] == null){
            dp[n][val] = 0;
            for (int i = 0; i <= val; i++){
                dp[n][val] += recur(n-1,i);
                dp[n][val] %= 10007;
            }
        }
        return dp[n][val] % 10007;
    }

}
