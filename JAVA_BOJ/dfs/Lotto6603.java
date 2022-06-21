package dfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Objects;
import java.util.StringTokenizer;

public class Lotto6603 {

    public static int[] arr;
    public static boolean[] visited;
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;




        LinkedList<int[]> list = new LinkedList<>();

        while (true){
            String str = br.readLine();

            if (Objects.equals(str, "0")){
                break;
            }

            st = new StringTokenizer(str," ");

            int N = Integer.parseInt(st.nextToken());
            int[] strList = new int[N];

            for (int i = 0; i < N; i++){
                strList[i] = Integer.parseInt(st.nextToken());
            }

            list.add(strList);
        }

        for (int[] S : list) {


            arr = new int[6];
            visited = new boolean[S.length];
            dfs(0,S, S.length, 6, 0);
            System.out.println();
        }

    }



    public static void dfs(int start, int[] S,int N, int M,int depth){

        if (depth == M){
            for (int val : arr){
                sb.append(val).append(" ");
            }
            System.out.println(sb);
            sb = new StringBuilder();
            return;
        }

        for (int i = start; i < N; i++){
            if (!visited[i]){
                visited[i] = true;
                arr[depth] = S[i];
                dfs(i,S,N,M,depth+1);
                visited[i] = false;
            }
        }
    }
}
