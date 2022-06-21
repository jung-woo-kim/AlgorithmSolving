package broute_force;

import java.util.Scanner;

public class BlackJack {

        public static void main(String[] args) {

            Scanner sc = new Scanner(System.in);

            int cardNum = Integer.parseInt(sc.next());
            int total = Integer.parseInt(sc.next());

            int temp = total;
            int answer = 0;

            int[] cardArray = new int[cardNum];

            for (int i = 0; i < cardNum; i++){
                cardArray[i] = Integer.parseInt(sc.next());
            }

            for (int i = 0; i < cardArray.length - 2; i++) {
                for (int j = i + 1; j < cardArray.length - 1; j++){
                    for (int k = j + 1;k < cardArray.length; k++){ //브루트포스

                        int sum = cardArray[i] + cardArray[j] + cardArray[k];

                        if (sum <= total){

                            if (total - sum < temp){
                                temp = total - sum;
                                answer = sum;
                            }

                        }

                    }
                }
            }
            System.out.println(answer);
        }
}
