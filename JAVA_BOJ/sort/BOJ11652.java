package sort;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Objects;
import java.util.StringTokenizer;

public class BOJ11652 {
    static int N,M;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());

        Long[] arr = new Long[N];

        for (int i = 0; i < N; i++){
            arr[i] = Long.parseLong(br.readLine());
        }

        Arrays.sort(arr);

        int max = 0;
        int cnt = 1;
        int idx = 0;

        for (int i = 1; i < N; i++){
            if (Objects.equals(arr[i], arr[i - 1])){
                cnt++;
            }else{
                cnt = 1;
            }

            if (max < cnt){
                max = cnt;
                idx = i;
            }
        }

        sb.append(arr[idx]);
        System.out.println(sb);

    }
}
