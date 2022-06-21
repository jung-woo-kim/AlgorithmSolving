package broute_force;

import java.util.Scanner;

public class Bulk {

        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            int PeopleNum = Integer.parseInt(sc.next());

            int[][] PeopleArray = new int[PeopleNum][2];
            int[] answerArray = new int[PeopleNum];

            for (int i = 0; i < PeopleNum; i++){
                PeopleArray[i][0] = Integer.parseInt(sc.next());
                PeopleArray[i][1] = Integer.parseInt(sc.next());
            }

            for (int i = 0; i < PeopleNum; i++){

                int grade = 1;

                for (int j = 0; j < PeopleNum; j++){
                    if (i != j){

                        if (PeopleArray[i][0] < PeopleArray[j][0] && PeopleArray[i][1] < PeopleArray[j][1]){
                            grade += 1;
                        }

                    }
                }
                answerArray[i] = grade;

            }

            for (int i = 0; i < PeopleNum; i++){
                System.out.print(answerArray[i]+" ");
            }

        }

}
