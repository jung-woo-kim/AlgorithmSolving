package divide_and_conqure;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Multiply1629 {
    static double A;
    static int B;
    static int C;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        st = new StringTokenizer(br.readLine()," ");

        A = Integer.parseInt(st.nextToken());

        B = Integer.parseInt(st.nextToken());

        C = Integer.parseInt(st.nextToken());

        sb.append((int) divide(A,B));

        System.out.println(sb);

    }

    static double divide(double A,int n){

        if (n == 0){
            return 1;
        }

        else if (n % 2 == 0){
            return divide(A*A% C,n/2) % C;
        }
        else{
            return A*divide(A*A% C,(n-1)/2) % C;
        }

    }

}
