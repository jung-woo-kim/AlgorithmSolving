package sort;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Objects;
import java.util.Stack;
import java.util.StringTokenizer;

public class BOJ10799 {
    static int N,M;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        String word = br.readLine(); //스트링 문자 POWER
        String[] list;


        list = word.split("");
        Stack<String> stack = new Stack<>();

        for (String s : list) {
            stack.push(s);
        }

        int stick = 0;
        int total = 0;
        boolean light = false;

        while (!stack.isEmpty()){
            String temp = stack.pop();

            if (Objects.equals(temp, "(")){
                stick--;
                if (light){
                    total+= stick;
                }
                else {
                    total += 1;
                }
                light = false;
            }else {
                stick++;
                light = true;
            }
        }


        sb.append(total);
        System.out.println(sb);

    }
}
