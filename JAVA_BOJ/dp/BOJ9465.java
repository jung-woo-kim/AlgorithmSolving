package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ9465 {

    static Integer[][] dp;
    static Integer[][] arr;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());

        dp = new Integer[2][100001];
        arr = new Integer[2][100001];

        for (int k =0; k < t; k++){

            int N = Integer.parseInt(br.readLine());


            for (int i = 0; i < 2; i++){
                String[] line = br.readLine().split(" ");
                for (int j = 1; j <= N; j++){
                    arr[i][j] = Integer.parseInt(line[j-1]);
                    dp[i][j] = null;
                }
            }

            dp[0][1] = arr [0][1];
            dp[1][1] = arr [1][1];

            if (N>1){
                dp[0][2] = arr[1][1] + arr[0][2];
                dp[1][2] = arr[0][1] + arr[1][2];
            }




            sb.append(Math.max(recur(N,0),recur(N,1))).append('\n');
        }

        System.out.println(sb);

    }

    static int recur(int n, int val){
        if (dp[val][n] == null){
            if (val == 0){
                dp[val][n] = Math.max(recur(n-1,1),Math.max(recur(n-2,0),recur(n-2,1)))+arr[val][n];
            }else{
                dp[val][n] = Math.max(recur(n-1,0),Math.max(recur(n-2,0),recur(n-2,1)))+arr[val][n];
            }

        }
        return dp[val][n];
    }

}
