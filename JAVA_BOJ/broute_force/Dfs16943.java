package broute_force;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Dfs16943 {

    public static int B;
    public static char[] arr;
    public static boolean[] visit;
    public static char[] A;
    public static int min;
    public static int ans;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine()," ");

        String Astr = st.nextToken();
        B = Integer.parseInt(st.nextToken());
        min = B;
        ans = -1;

        arr = new char[Astr.length()];
        visit = new boolean[Astr.length()];

        A = new char[Astr.length()];

        for (int i = 0; i < Astr.length(); i++){
            A[i] = Astr.charAt(i);
        }

        dfs(Astr.length(), Astr.length(), 0);
        sb.append(ans);
        System.out.println(sb);

    }

    public static void dfs(int N,int M,int depth){

        if (depth == M){
            if (arr[0] == '0'){
                return;
            }
            String str = new String(arr);

            int i = Integer.parseInt(str);

            if ((B-i) < min && (B-i) >= 0){
                min = B-i;
                ans = i;
            }

            return;
        }


        for (int i = 0; i < N; i++) {
            if (!visit[i]) {
                visit[i] = true;
                arr[depth] = A[i];



                dfs(N, M, depth + 1);
                visit[i] = false;
            }
        }
    }

}
