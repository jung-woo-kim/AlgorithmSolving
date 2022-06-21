package graph;

import java.io.*;
import java.util.*;

public class BOJ9466 {

    static int n, cnt;
    static int[] link;
    static boolean[] check, isSearchEnd;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        int t = Integer.parseInt(br.readLine());

        for(int test=0; test<t; test++) {
            n = Integer.parseInt(br.readLine());
            link = new int[n+1];
            check = new boolean[n+1];
            isSearchEnd = new boolean[n+1];

            st = new StringTokenizer(br.readLine());
            for(int i=1; i<n+1; i++) {
                int to = Integer.parseInt(st.nextToken());

                link[i]=to;
            }
            cnt =0;
            for(int i=1; i<n+1; i++) {
                dfs(i);
            }
            System.out.println(n-cnt);
        }

    }
    static void dfs(int pos) {
        check[pos] = true;
        int next = link[pos];
        if(!check[next]) {
            dfs(next);
        }else {
            if(!isSearchEnd[next]) { //배열을 하나 더 둬서 한바퀴 쭉 더 돌림 다음 번 돌릴땐? 이미 한번 돈 바퀴니 ㄴㄴ
                cnt++;
                while(next != pos) {
                    cnt++;
                    next = link[next];
                }
            }
        }
        isSearchEnd[pos] = true;
    }
}
