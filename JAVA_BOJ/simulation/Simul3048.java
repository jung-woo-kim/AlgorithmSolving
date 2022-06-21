package simulation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Simul3048 {
    private static int N, M;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        char[] ant = new char[N + M];
        int[] antDistance = new int[N + M];

        String antSt = br.readLine();

        int temp = 0;

        for (int i = antSt.length() - 1; i >= 0; i--){
            ant[temp] = antSt.charAt(i);
            antDistance[temp] = 0;
            temp++;
        }


        antSt = br.readLine();

        for (int i = N; i < N + M; i++){
            ant[i] = antSt.charAt(i-N);
            antDistance[i] = 1;
        }

        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++){
            for (int i = 0; i < ant.length - 1; i++){
                if (antDistance[i] != antDistance[i+1]){
                    swap(antDistance,i,i+1);
                    swapChar(ant,i,i+1);

                    i++;
                }
            }
        }
        sb.append(ant);
        System.out.println(ant);

    }

    public static void swap(int[] arr,int i,int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void swapChar(char[] arr,int i,int j) {
        char temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

}
