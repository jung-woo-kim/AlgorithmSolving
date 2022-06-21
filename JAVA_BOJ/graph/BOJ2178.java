package graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class BOJ2178 {

    static int N,M;

    private static final int[] dx = {0,0,1,-1};
    private static final int[] dy = {1,-1,0,0};

    static int[][] map;
    static boolean[][] visited;

    static int sum = 0;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");

        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[N][M];
        visited = new boolean[N][M];

        for (int i = 0; i < N; i++){
            String str = br.readLine();
            for (int j = 0; j < M; j++){
                map[i][j] = str.charAt(j) - '0';
            }
        }

        bfs(0,0);

        sb.append(map[N-1][M-1]);
        System.out.println(sb);
    }

    static void bfs(int x, int y){
        LinkedList<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{x, y});
        visited[x][y] = true;

        while (!queue.isEmpty()){
            int[] temp = queue.poll();

            for (int i = 0; i < 4; i++){

                int nx = temp[0] + dx[i];
                int ny = temp[1] + dy[i];

                if(nx >=0 && ny >=0 && nx < N && ny < M){
                    if(map[nx][ny] > 0 && !visited[nx][ny]){
                        queue.offer(new int[]{nx, ny});
                        visited[nx][ny] = true;

                        map[nx][ny] = map[temp[0]][temp[1]] + 1;
                    }
                }
            }
        }


    }

}
