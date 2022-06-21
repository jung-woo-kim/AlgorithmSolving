package simulation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ColRead10798 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String[] list = new String[5];

        int max = 0;

        for (int i = 0; i < 5; i++){
            list[i] = br.readLine();
            if (list[i].length() > max){
                max = list[i].length();
            }
        }
        for (int i = 0; i < max; i++){

            for (int j = 0; j < 5; j++){
                if (list[j].length() > i){
                    sb.append(list[j].charAt(i));
                }
            }
        }

        System.out.println(sb);
    }
}
