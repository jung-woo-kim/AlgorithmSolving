package dfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class GoodNum2661 {

    static int N;
    static String min;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());

        dfs("",0);



    }

    public static void dfs(String str,int n){

        if (n == N){
            System.out.println(str);
            System.exit(0);

            return;
        }


        for (int i = 1; i <= 3; i++){
            if (check(str + i)){
                dfs(str+i,n+1);
            }
        }
    }


    public static boolean check(String str){
        for(int i = 1; i <= str.length() / 2; i++) {
            String front = str.substring(str.length() -i * 2, str.length() - i);
            String back = str.substring(str.length() - i);
            if(front.equals(back)) return false;
        }
        return true;
    }

}
