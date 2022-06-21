package graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ10451 {

    static int N,M;
    static int[][] checked;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++){

            int total = 0;

            M = Integer.parseInt(br.readLine());

            st = new StringTokenizer(br.readLine()," ");

            checked = new int[M+1][M+1];
            visited = new boolean[M+1];

            for (int j = 1; j <= M; j++){
                checked[j][Integer.parseInt(st.nextToken())] = 1;
            }

            for (int j = 1; j <= M; j++){
                if (!visited[j]){

                    total++;

                    dfs(j);
                }
            }

            sb.append(total).append("\n");


        }
        System.out.println(sb);

    }

    static void dfs(int x){

        visited[x] = true;

        for (int i = 1; i <= M; i++){
            if (!visited[i] && checked[x][i] == 1){

                dfs(i);
            }
        }
    }

}
