package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class MakeOne1463 {

    public static Integer[] dp = new Integer[1000001];

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        dp[1] = 0;
        dp[2] = 1;

        int N = Integer.parseInt(br.readLine());

        sb.append(z(N));
        System.out.println(sb);
    }

    public static int z(int n){
        if (dp[n] == null){
            if (n % 6 == 0) {
                dp[n] = Math.min(z(n - 1), Math.min(z(n / 3), z(n / 2))) + 1;
            }
            // 3으로만 나눠지는 경우
            else if (n % 3 == 0) {
                dp[n] = Math.min(z(n / 3), z(n - 1)) + 1;
            }
            // 2로만 나눠지는 경우
            else if (n % 2 == 0) {
                dp[n] = Math.min(z(n / 2), z(n - 1)) + 1;
            }
            // 2와 3으로 나누어지지 않는 경우
            else {
                dp[n] = z(n - 1) + 1;
            }
        }
        return dp[n];
    }
}
