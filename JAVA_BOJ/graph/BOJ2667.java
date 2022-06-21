package graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ2667 {

    private static final int[] dx = {0,0,1,-1};
    private static final int[] dy = {1,-1,0,0};

    static int N,M;
    private static final int[] aparts = new int[25*25];
    static int[][] map;
    static boolean[][] visited;

    static int apartIdx = 0;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());

        map = new int[N][N];
        visited = new boolean[N][N];


        for (int i = 0; i < N; i++){
            String str = br.readLine();

            for (int j = 0; j < N; j++){
                map[i][j] = str.charAt(j) - '0';
            }
        }
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if(map[i][j] == 1 && !visited[i][j]){
                    apartIdx++;
                    dfs(i,j);
                }
            }
        }
        Arrays.sort(aparts);
        System.out.println(apartIdx);

        for(int i=0; i<aparts.length; i++){
            if(aparts[i] != 0){
                System.out.println(aparts[i]);
            }
        }

    }
    static void dfs(int x,int y){
        visited[x][y] = true;
        aparts[apartIdx]++;

        for (int i = 0 ; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx >=0 && ny >=0 && nx < N && ny < N){
                if(map[nx][ny] == 1 && !visited[nx][ny]){
                    dfs(nx,ny);
                }
            }
        }
    }
}
