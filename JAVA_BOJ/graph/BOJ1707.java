package graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ1707 {
    static int[][] check; //간선 연결상태
    static int[] checked; // 0 아직 안감 1 레드 2 블루
    static int n; //정점개수
    static int m; //간선개수
    static boolean answer = true;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int k = Integer.parseInt(br.readLine());

        for (int j = 0; j < k; j++){

            st = new StringTokenizer(br.readLine()," ");

            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());

            check = new int[n+1][n+1];
            checked = new int[n+1];


            for (int i = 0; i < m; i++){
                st = new StringTokenizer(br.readLine()," ");

                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());

                check[x][y] = check[y][x] = 1;
            }
            for (int m = 1; m <= n; m++ ){
                if (checked[m] == 0){
                    bfs(m);
                }
            }
            if (answer){
                System.out.println("YES");

            }else{
                System.out.println("NO");

            }
            answer = true;
        }

    }


    public static void bfs(int i) {
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.offer(i);
        checked[i] = 1;

        while(!queue.isEmpty()) {
            int temp = queue.poll();

            for(int j = 1; j <= n; j++) {

                if (check[temp][j] == 1){
                    if (checked[j] == 0){

                        if (checked[temp] == 1){
                            checked[j] = 2;
                        }else if(checked[temp] == 2){
                            checked[j] = 1;
                        }
                        queue.offer(j);

                    }else if(checked[j] == 1){
                        if (checked[temp] == 1){
                           answer = false;
                           return;
                        }
                    }else{
                        if (checked[temp] == 2){
                            answer = false;
                            return;
                        }
                    }
                }

            }
        }
    }
}
