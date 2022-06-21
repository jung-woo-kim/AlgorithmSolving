package graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ7576 {
    static int N,M;

    private static final int[] dx = {0,0,1,-1};
    private static final int[] dy = {1,-1,0,0};

    static int[][] map;
    static boolean[][] visited;

    static boolean check = true;
    static int sum = 0;

    static Queue<int[]> queue = new LinkedList<>();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");

        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[N][M];
        visited = new boolean[N][M];

        for (int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine()," ");
            for (int j = 0; j < N; j++){
                map[j][i] = Integer.parseInt(st.nextToken());

                if (map[j][i] == 1){
                    queue.offer(new int[]{j,i});
                }

            }
        }
        bfs();
        if (check){
            sb.append(sum-1);
        }else{
            sb.append(-1);
        }

        System.out.println(sb);

    }

    static void bfs(){

        while (!queue.isEmpty()){
            int[] temp = queue.poll();

            for (int i = 0; i < 4; i++){
                int nx = temp[0] + dx[i];
                int ny = temp[1] + dy[i];
                if(nx >=0 && ny >=0 && nx < N && ny < M){
                    if(map[nx][ny] == 0 && !visited[nx][ny]){
                        queue.offer(new int[]{nx, ny});
                        visited[nx][ny] = true;

                        map[nx][ny] = map[temp[0]][temp[1]] + 1;
                    }
                }
            }
        }

        for (int i = 0; i < N; i++){

            for (int j = 0; j < M; j++){
               if(map[i][j] == 0){
                   check = false;
                   break;
               }else{
                   sum = Math.max(sum,map[i][j]);
               }

            }
        }

    }

}
