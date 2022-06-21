package dfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class DFS1182 {

    public static int N;
    public static int S;
    public static int[] num;
    public static int[] arr;
    public static boolean[] visited;
    public static int total = 0;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        st = new StringTokenizer(br.readLine()," ");

        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());

        arr = new int[N];
        num = new int[N];
        visited = new boolean[N];

        st = new StringTokenizer(br.readLine()," ");


        for (int i = 0; i < N; i++){
            num[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i <= N; i++){
            dfs(0,N,i,0);

        }
        sb.append(total);
        System.out.println(sb);
    }

    public static void dfs(int start, int N, int M, int depth){

        if (depth == M){
            int sum = 0;

            for (int val : arr){
                sum += val;
            }

            if (sum == S){
                total++;
            }
            return;
        }


        for (int i = start; i < N; i++){
            if (!visited[i]){
                visited[i] = true;
                arr[depth] = num[i];
                dfs(i,N,M,depth+1);
                visited[i] = false;
            }
        }
    }
}
