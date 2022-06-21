package graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ1012 {

    static int T;

    static int[] dx ={0,0,1,-1};
    static int[] dy ={1,-1,0,0};

    static int[][] cabbage;
    static boolean[][] visited;
    static int total = 0;

    static int row;
    static int col;


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++){
            st = new StringTokenizer(br.readLine()," ");

            row = Integer.parseInt(st.nextToken());
            col = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());

            cabbage = new int[row][col];
            visited = new boolean[row][col];

            for (int j = 0; j < K; j++){
                st = new StringTokenizer(br.readLine()," ");

                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());

                cabbage[x][y] = 1;
            }

            for (int k = 0; k < col; k++){
                for (int j = 0; j< row; j++){
                    if (cabbage[j][k] == 1 && !visited[j][k]){
                        total++;
                        dfs(j,k);
                    }
                }
            }

            sb.append(total).append("\n");
            total = 0;

        }
        System.out.println(sb);

    }

    static void dfs(int x, int y){

        visited[x][y] = true;

        for (int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < row && ny >= 0 && ny < col){
                if (cabbage[nx][ny] == 1 && !visited[nx][ny]){
                    dfs(nx,ny);
                }
            }
        }
    }
}
