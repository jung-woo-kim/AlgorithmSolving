package sort;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class BOJ11651 {

    static int [][] arr;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        arr = new int[N][2];

        for (int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine()," ");
            arr[i][1] = Integer.parseInt(st.nextToken());
            arr[i][0] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr, new Comparator<int[]>(

        ) {
            @Override
            public int compare(int[] o1, int[] o2) {
                if(o1[0] == o2[0]) {		// 첫번째 원소가 같다면 두 번째 원소끼리 비교
                    return o1[1] - o2[1];
                }
                else {
                    return o1[0] - o2[0];
                }
            }
        });
        for(int i = 0; i < N; i++) {
            System.out.println(arr[i][1] + " " + arr[i][0]);
        }

    }
}
