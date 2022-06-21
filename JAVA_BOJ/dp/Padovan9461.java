package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Padovan9461 {

    public static long[] P;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        P = new long[101];

        int T = Integer.parseInt(br.readLine());


        P[1] = 1;
        P[2] = 1;
        P[3] = 1;
        P[4] = 2;
        P[5] = 2;

        for (int i = 0; i < T; i++){
            int N = Integer.parseInt(br.readLine());

            sb.append(p(N)).append('\n');
        }

        System.out.println(sb);

    }

    static long p(int N){
        if (P[N] == 0){
            P[N] = p(N-2) + p(N-3);
        }
        return P[N];
    }
}
