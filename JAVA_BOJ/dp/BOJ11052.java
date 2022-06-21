package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ11052 {

    static int[] dp;
    static int[] card;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine()," ");

        dp = new int[N+1];
        card = new int[N+1];

        for (int i = 1; i <= N; i++){
            card[i] = Integer.parseInt(st.nextToken());
        }

        dp[1] = card[1];

        System.out.println(recur(N));

    }

    static int recur(int n){

        if (dp[n] > 0) return dp[n];

        int temp = card[n];

        for(int m=1; m <= n; m++){
            //이 문제의 요지는 반복문을 이렇게 돌릴 경우 결국 수의 합은 N으로 수렴렴된다는 것!
            int current = recur(n-m) + card[m];
            temp = Math.max(temp,current);
        }

        return dp[n]= temp;
    }
}
