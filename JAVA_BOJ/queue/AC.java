package queue;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class AC {

    private static int N, M;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;



        N = Integer.parseInt(br.readLine());

        String[] orderList = new String[N];
        int[] sizeList = new int[N];
        String[] arrayList = new String[N];

        for (int i = 0; i < N; i++){
            orderList[i] = br.readLine();
            sizeList[i] = Integer.parseInt(br.readLine());
            arrayList[i] = br.readLine();
        }

        for (int i = 0; i < N; i++){

            LinkedList<Integer> list = new LinkedList<>();
            st = new StringTokenizer(arrayList[i], "[],");

            for (int j = 0; j < sizeList[i]; j++){
                list.add(Integer.parseInt(st.nextToken()));
            }


            boolean check = false;

            boolean isRight = true;

            for (int j = 0; j < orderList[i].length(); j++){

                switch (orderList[i].charAt(j)){
                    case 'R':
                        isRight = !isRight;
                        break;
                    case 'D':
                        if (isRight){
                            if (!list.isEmpty()){
                                list.removeFirst();
                            }else{
                                check = true;
                            }
                        }else{
                            if (!list.isEmpty()){
                                list.removeLast();
                            }else{
                                check = true;
                            }
                        }

                        break;
                }

            }
            StringBuilder sb = new StringBuilder();


            if (check){
                sb.append("error");
                System.out.println(sb);
            }else{
                makePrintString(list,isRight);
            }
        }

    }

    public static void makePrintString(LinkedList<Integer> deque, boolean isRight) {

        StringBuilder sb = new StringBuilder();

        sb.append('[');	// 여는 대괄호 먼저 StringBuilder에 저장

        if(deque.size() > 0) {	//만약 출력 할 원소가 한 개 이상일 경우

            if(isRight) {	// 정방향일경우

                sb.append(deque.pollFirst());	// 먼저 첫 번째 원소를 넘겨준다.

                // 그 다음 원소부터 반점을 먼저 넘겨준 후 덱의 원소를 하나씩 뽑아 넘긴다.
                while(!deque.isEmpty()) {
                    sb.append(',').append(deque.pollFirst());
                }
            }
            else {	// 역방향일경우
                sb.append(deque.pollLast());	// 먼저 뒤에서부터 첫 번째 원소를 넘겨준다.

                // 그 다음 원소부터 반점을 먼저 넘겨준 후 덱의 원소를 뒤에서부터 하나씩 뽑아 넘긴다.
                while(!deque.isEmpty()) {
                    sb.append(',').append(deque.pollLast());
                }
            }
        }

        sb.append(']');	// 닫는 대괄호 및 개행으로 마무리

        System.out.println(sb);
    }


}
