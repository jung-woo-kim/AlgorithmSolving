package bnsearch;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BNSearch {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine()," ");

        int idx = 0;

        while (st.hasMoreTokens()){
            arr[idx] = Integer.parseInt(st.nextToken());
            idx++;
        }
        Arrays.sort(arr);

        int M = Integer.parseInt(br.readLine());
        int[] find = new int[M];
        st = new StringTokenizer(br.readLine()," ");

        idx = 0;

        while (st.hasMoreTokens()){
            find[idx] = Integer.parseInt(st.nextToken());
            idx++;
        }

        for (int i = 0; i < M; i++){
            System.out.println(BSearch(arr,find[i]));
        }

    }


    static int BSearch(int[] arr, int target) {
        int low = 0;
        int high = arr.length - 1;
        int mid = (low + high) / 2;

        while(low <= high) {

            if (arr[mid] == target)
                return 1;
            else if (arr[mid] > target)
                high = mid - 1;
            else
                low = mid + 1;
            mid = (low + high) / 2;
        }
        return 0;
    }
}
