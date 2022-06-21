package simulation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Objects;
import java.util.StringTokenizer;

public class Simul2490 {

    private static int N, M;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String[] list = new String[3];

        for (int i = 0; i < 3; i++){
            list[i] = br.readLine();

        }
        for (int i = 0; i < 3; i++){
            StringTokenizer st = new StringTokenizer(list[i]," ");

            int num = 0;
            for (int j = 0; j < 4; j++){
                if (Objects.equals(st.nextToken(), "1")){
                    num++;
                }
            }
            switch (num){
                case 0:
                    sb.append("D");
                    sb.append("\n");
                    break;
                case 1:
                    sb.append("C");
                    sb.append("\n");
                    break;
                case 2:
                    sb.append("B");
                    sb.append("\n");
                    break;
                case 3:
                    sb.append("A");
                    sb.append("\n");
                    break;
                case 4:
                    sb.append("E");
                    sb.append("\n");
                    break;
            }
        }
        System.out.println(sb);
    }
}