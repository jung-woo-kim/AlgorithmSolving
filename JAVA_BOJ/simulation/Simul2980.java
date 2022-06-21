package simulation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Simul2980 {
    private static int N, M;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        int[] idxList = new int[M];
        int[] traffic = new int[M];
        int[] trafficRedTime = new int[M];
        int[] trafficGreenTime = new int[M];
        int time = 0;
        int now = 0;

        for (int i = 0; i < M; i++){
            traffic[i] = 0;
            trafficGreenTime[i] = 0;
            trafficRedTime[i] = 0;
        }

        for (int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            int idx = Integer.parseInt(st.nextToken());
            traffic[idx] = -1; //처음에 빨간불로 초기화
            trafficRedTime[idx] = Integer.parseInt(st.nextToken());
            trafficGreenTime[idx] = Integer.parseInt(st.nextToken());
        }

        while (true){
            time++;

            if (traffic[now] != 0){
                int temp = time % (trafficRedTime[now] + trafficGreenTime[now]);
                if (temp >= trafficRedTime[now]){
                    traffic[now] = 1;
                }else{
                    traffic[now] = -1;
                }
            }

            if (traffic[now] != -1){
                now++;
            }


            if (now == M){
                time++;
                sb.append(time);
                System.out.println(sb);
                break;
            }
        }
    }

}
