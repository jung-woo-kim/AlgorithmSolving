package divide_and_conqure;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class QuadTree1992 {

    static int[][] square;
    static StringBuilder sb;
    static int N;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());

        square = new int[N][N];

        for (int i = 0; i < N; i++){

           String str = br.readLine();

            for (int j = 0; j < N; j++){

                square[i][j] = Integer.parseInt(String.valueOf(str.charAt(j)));

            }
        }

        divide(0,0,N);


    }

    public static void divide(int row, int col, int size){



        if (check(row,col,size)){



            if (square[row][col] == 0){
                System.out.print(0);

            }else{
                System.out.print(1);
            }

            return;

        }
        int newSize = size/2;

        System.out.print("(");


        divide(row, col, newSize);
        divide(row, col + newSize, newSize);
        divide(row + newSize, col, newSize);
        divide(row + newSize, col + newSize, newSize);

        System.out.print(")");

    }

    public static boolean check(int row, int col, int size){

        int temp = square[row][col];

        for (int i = row; i < row + size; i++){
            for (int j = col; j < col + size; j++){
                if (temp != square[i][j]){
                    return false;
                }
            }
        }
        return true;

    }
}
