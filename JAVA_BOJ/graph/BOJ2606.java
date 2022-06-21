package graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ2606 {

    static int N,M;
    static boolean[] checked;
    static int[][] check;
    static int sum;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());

        check = new int[N+1][N+1];
        checked = new boolean[N+1];

        sum -= 1;

        for (int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine()," ");

            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            check[x][y] = check[y][x] = 1;
        }

        dfs(1);

        sb.append(sum);

        System.out.println(sb);

    }

    static void dfs(int i){

        checked[i] = true;
        sum++;

        for (int j = 1; j <= N; j++){
            if (!checked[j] && check[i][j] == 1){
                dfs(j);
            }
        }

    }
}
