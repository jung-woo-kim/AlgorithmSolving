package sort;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Stack;

public class Zero {


    public static Stack<Integer> stack;


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        stack = new Stack<>();

        int N = Integer.parseInt(br.readLine());



        for (int i = 0; i < N; i++){

            int value = Integer.parseInt(br.readLine());

            if (value == 0){
                stack.pop();
            }
            else {
                stack.push(value);
            }

        }

        int total = 0;

        while (!stack.empty()){
            total += stack.pop();
        }

        sb.append(total);
        System.out.println(sb);

    }


}