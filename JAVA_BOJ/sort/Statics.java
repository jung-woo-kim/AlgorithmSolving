package sort;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Statics {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = Integer.parseInt(br.readLine());
        int[] array = new int[num];
        int[] sorted = new int[num];
        HashMap<Integer, Integer> ranking = new HashMap<Integer, Integer>();

        StringTokenizer st = new StringTokenizer(br.readLine()," ");

        for (int i = 0; i < num ; i++){
            array[i] = Integer.parseInt(st.nextToken());
            sorted[i] = array[i];
        }

        Arrays.sort(sorted);

        int rankNum = 1;

        for (int i = 0; i < num ; i++){
            if (!ranking.containsKey(sorted[i])){
                ranking.put(sorted[i],rankNum);
            }
            rankNum++;
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < num ; i++){
            int rank = ranking.get(array[i]);
            sb.append(rank).append(" ");

        }
        System.out.println(sb);

    }
}
