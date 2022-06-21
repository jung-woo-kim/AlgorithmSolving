package math;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ2609 {
    static int N,M;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");

        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        sb.append(gcd(N,M)).append("\n").append(lcm(N,M));
        System.out.println(sb);


    }
    static int gcd(int a, int b) {

        while(b != 0) {
            int r = a % b;

            a = b;
            b = r;
        }
        return a;
    }


    // 최소공배수 : Least Common mulitple
    static int lcm(int a, int b) {
        return a * b / gcd(a, b);
    }
}
