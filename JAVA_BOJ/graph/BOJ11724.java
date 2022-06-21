package graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ11724 {
    static int N,M;

    static int[][] check;
    static boolean[] visited;

    static int graphNum = 0;


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");

        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        check = new int[N+1][N+1];
        visited = new boolean[N+1];

        for (int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine()," ");

            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            check[x][y] = check[y][x] = 1;

        }

        for (int i = 1; i <= N; i++){
            if (!visited[i]){
                graphNum++;
                dfs(i);
            }
        }

        System.out.println(graphNum);

    }

    static void dfs(int x){

        visited[x] = true;

        for (int i = 1; i <= N; i++){
            if (!visited[i] && check[x][i] == 1){
                dfs(i);
            }
        }

    }
}
