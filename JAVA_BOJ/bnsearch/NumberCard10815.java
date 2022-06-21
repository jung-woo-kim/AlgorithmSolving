package bnsearch;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class NumberCard10815 {

    static int[] list;
    static int[] find;
    static int[] total;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        list = new int[N];
        st = new StringTokenizer(br.readLine()," ");

        for (int i = 0; i < N; i++){
            list[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(list);

        int M = Integer.parseInt(br.readLine());

        find = new int[M];
        total = new int[M];

        st = new StringTokenizer(br.readLine()," ");
        for (int i = 0; i < M; i++){
            find[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < M; i++){
            BNsearch(0,list.length-1, i);
            sb.append(total[i]).append(" ");
        }

        System.out.println(sb);

    }

    static void BNsearch(int low,int high,int idx){

        low = 0;
        high = list.length - 1;
        int mid = (low + high) / 2;

        while(low <= high) {

            if (list[mid] == find[idx]){
                total[idx]++;
                return;
            }
            else if (list[mid] > find[idx])
                high = mid - 1;
            else
                low = mid + 1;
            mid = (low + high) / 2;
        }
    }
}
