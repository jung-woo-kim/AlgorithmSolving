package queue;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;

public class Card2 {

    public static LinkedList<Integer> qe = new LinkedList<Integer>();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i = 1; i <= n; i++){
            qe.addLast(i);

        }

        while (qe.size() != 1){
            qe.pop();
            qe.addLast(qe.pop());

        }

        System.out.println(qe.pop());
    }

}
