package sort;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Bracket {

    public static Stack<Integer> stack;
    public static String[] line;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        StringTokenizer st;

        stack = new Stack<>();


        int N = Integer.parseInt(br.readLine());
        line = new String[N];

        for (int i = 0; i < N; i++){
            line[i] = br.readLine();
        }


        for (int i = 0; i < N; i++){

            boolean check = false;

            for (int j = 0; j < line[i].length(); j++){
                String value = String.valueOf(line[i].charAt(j));

                if (value.equals("(")){
                    stack.push(1);
                }else{
                    if (!stack.empty()){
                        stack.pop();
                    }
                    else{
                        System.out.println("No");
                        check =true;
                        break;
                    }
                }
            }
            if (!check){
                if (stack.empty()){
                    System.out.println("YES");
                }else{
                    System.out.println("No");
                    stack.clear();
                }
            }

        }


    }
}
