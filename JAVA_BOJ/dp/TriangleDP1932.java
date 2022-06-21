package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class TriangleDP1932 {

    public static Integer[][] dp;
    public static Integer[][] list;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        dp = new Integer[N][N];
        list = new Integer[N][N];

        for (int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine()," ");
            int j = 0;
            while (st.hasMoreTokens()){
                list[i][j] =Integer.parseInt(st.nextToken());
                j++;
            }
        }
        dp[N-1] = list[N-1];

        sb.append(triangle(0,0));
        System.out.println(sb);
    }

    public static int triangle(int a,int b){

        if (dp[a][b] == null){
            dp[a][b] = Math.max(triangle(a+1,b),triangle(a+1,b+1)) +list[a][b];
        }

        return dp[a][b];

    }
}
