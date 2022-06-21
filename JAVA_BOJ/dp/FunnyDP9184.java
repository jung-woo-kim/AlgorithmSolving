package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class FunnyDP9184 {

    public static Integer[][][] list;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        list = new Integer[51][51][51];

        list[0][0][0] = 1;



        while (true){
            String str = br.readLine();

            st = new StringTokenizer(str," ");

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if (a == -1 && b == -1 && c == -1){
                break;
            }

            sb.append("w(").append(a).append(", ").append(b).append(", ").append(c).append(") = ").append(w(a,b,c)).append('\n');

        }
        System.out.println(sb);

    }

    public static int w(int a, int b, int c){
        if (a <= 0 || b <= 0 || c <= 0){
            return 1;
        }
        else if (a > 20 || b > 20 || c > 20){
            return w(20, 20, 20);
        }
        else if (a < b && b < c){
            if (list[a][b][c] == null){
                list[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c);
            }else{
                return list[a][b][c];
            }

        }else{
            if (list[a][b][c] == null){
                list[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1);
            }else{
                return list[a][b][c];
            }
        }
        return list[a][b][c];

    }

}
