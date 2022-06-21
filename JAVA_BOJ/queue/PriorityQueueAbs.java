package queue;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;

public class PriorityQueueAbs {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        java.util.PriorityQueue<Integer> pr = new java.util.PriorityQueue<>(100000, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {

                int abs1 = Math.abs(o1);
                int abs2 = Math.abs(o2);

                if(abs1 == abs2) return o1 > o2 ? 1 : -1;

                return abs1 - abs2;

            }
        });

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
