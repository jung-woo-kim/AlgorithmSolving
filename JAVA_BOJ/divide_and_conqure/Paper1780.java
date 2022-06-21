package divide_and_conqure;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Paper1780 {
    static int[][] square;
    static int one;
    static int zero;
    static int minone;

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

        sb.append(minone).append('\n').append(zero).append('\n').append(one);
        System.out.println(sb);

    }

    static void divide(int row, int col, int size){

        if (colorCheck(row,col,size)){
            if (square[row][col] == 0){
                zero++;
            }else if(square[row][col] == 1){
                one++;
            }else{
                minone++;
            }
            return;
        }
        int newSize = size/3;

        divide(row, col, newSize);
        divide(row, col + newSize, newSize);
        divide(row, col + newSize + newSize, newSize);

        divide(row + newSize, col, newSize);
        divide(row + newSize, col + newSize, newSize);
        divide(row + newSize, col + newSize + newSize, newSize);

        divide(row + newSize + newSize, col, newSize);
        divide(row + newSize + newSize, col + newSize, newSize);
        divide(row + newSize + newSize, col + newSize + newSize, newSize);

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
