package queue;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> q = new ArrayList<>();

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken())-1;


        for(int i = 1; i <= N; i++) {
            q.add(i);
        }

        StringBuilder sb = new StringBuilder();
        sb.append('<');

        int idx = 0;

        while(q.size() > 1) {

            idx += K;

            if (idx >= q.size()){
                idx %= q.size();
            }


            sb.append(q.remove(idx)).append(", ");;

        }

        // 마지막 원소 출력한 뒤 > 도 붙여준다.
        sb.append(q.remove(0)).append('>');
        System.out.println(sb);
    }

}