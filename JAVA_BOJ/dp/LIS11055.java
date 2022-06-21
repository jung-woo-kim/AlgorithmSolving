package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class LIS11055 {

    static Integer[] dp;
    static Integer[] arr;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine()," ");


        dp = new Integer[N+1];
        arr = new Integer[N+1];

        for (int i = 1; i <= N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int max = Integer.MIN_VALUE;


        for (int i = 1; i <= N; i++){
            if (max < recur(i)){
                max = recur(i);
            }
        }

        System.out.println(max);

    }

    static int recur(int n){
        if (dp[n] == null){

            dp[n] = arr[n];

            for (int i = 1; i <= n; i++){

                if (arr[i]<arr[n]){
                    dp[n] = Math.max(dp[n],recur(i) + arr[n]);
                }

            }

        }

        return dp[n];
    }

}
