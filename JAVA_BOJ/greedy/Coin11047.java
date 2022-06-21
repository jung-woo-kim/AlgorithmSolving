package greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Coin11047 {
    static int[] coin;
    static int total;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        st = new StringTokenizer(br.readLine()," ");

        int N = Integer.parseInt(st.nextToken());
        total = Integer.parseInt(st.nextToken());
        int answer = 0;

        coin = new int[N];

        for (int i = 0; i < N; i++){
            coin[i] = Integer.parseInt(br.readLine());
        }

        for (int i = N-1; i >= 0; i--){
            int a = total / coin[i];
            answer += a;

            total = total - a * coin[i];
        }
        sb.append(answer);
        System.out.println(sb);

    }
}
