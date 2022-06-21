package divide_and_conqure;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class ColorPaper2630 {
    static int[][] square;
    static int white;
    static int blue;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        square = new int[N][N];

        for (int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine()," ");
            for (int j = 0; j < N; j++){
                square[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        divide(0,0,N);

        sb.append(white).append('\n').append(blue);
        System.out.println(sb);

    }

    static void divide(int row, int col, int size){

        if (colorCheck(row,col,size)){
            if (square[row][col] == 0){
                white++;
            }else{
                blue++;
            }
            return;
        }
        int newSize = size/2;

        divide(row, col, newSize);
        divide(row, col + newSize, newSize);
        divide(row + newSize, col, newSize);
        divide(row + newSize, col + newSize, newSize);

    }

    public static boolean colorCheck(int row, int col, int size) {

        int color = square[row][col];	// 첫 번째 원소를 기준으로 검사

        for(int i = row; i < row + size; i++) {
            for(int j = col; j < col + size; j++) {
                if(square[i][j] != color) {
                    return false;
                }
            }
        }

        return true;
    }
}
