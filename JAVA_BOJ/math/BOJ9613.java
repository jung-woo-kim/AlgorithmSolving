package math;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ9613 {
    static int N,M;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine()," ");
            M = Integer.parseInt(st.nextToken());

            int[] arr = new int[M];

            for (int j = 0; j < M; j++){
                arr[j] = Integer.parseInt(st.nextToken());
            }

            Long sum = 0L;

            for (int j = 0; j < M-1; j++){
                for (int k = j+1; k < M; k++){
                    sum += gcd(arr[j],arr[k]);
                }
            }

            if (M == 1){
                sum = (long) arr[0];
            }

            sb.append(sum).append("\n");

        }

        System.out.println(sb);

    }

    static int gcd(int a,int b){

        while(b != 0) {
            int r = a % b;

            a = b;
            b = r;

        }

        return a;

    }
}
