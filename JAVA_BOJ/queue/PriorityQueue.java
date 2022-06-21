package queue;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class PriorityQueue {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        java.util.PriorityQueue<Integer> pr = new java.util.PriorityQueue<>(Collections.reverseOrder());

        int n = Integer.parseInt(br.readLine());

        int[] list = new int[n];

        for (int i = 0; i < n; i++){
            list[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 0; i < n; i++){
            if (list[i] == 0){
                if (pr.isEmpty()){
                    System.out.println(0);
                }else{
                    System.out.println(pr.poll());
                }
            }else{
                pr.add(list[i]);
            }
        }
    }
}
