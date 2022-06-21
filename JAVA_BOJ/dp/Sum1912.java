package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Sum1912 {

    static int N;
    static int[] list;
    static int max;
    static Integer[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());

        list = new int[N];
        dp = new Integer[N];

        st = new StringTokenizer(br.readLine()," ");

        for (int i = 0; i < N; i++){
            list[i] = Integer.parseInt(st.nextToken());
        }

        dp[0] = list[0];
        max = list[0];

        sum(N-1);
        sb.append(max);

        System.out.println(sb);

    }

    static int sum(int n){

        if (dp[n] == null){
            dp[n] = Math.max(sum(n-1) + list[n],list[n]);

            max = Math.max(dp[n],max);
        }


        return dp[n];
    }
}
