package sort;

import java.util.*;

public class MergeSort {

    public static int[] src;
    public static int[] tmp;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int Num = Integer.parseInt(sc.next());

        src = new int[Num];
        tmp = new int[Num];

        for (int i = 0; i < Num; i++){
            src[i] = Integer.parseInt(sc.next());
        }
        merge(0,Num-1);

        for(int value : src) {
            sb.append(value).append('\n');
        }
        System.out.println(sb);
    }

    public static void merge(int left, int right){
        if (left < right){
            int mid = (left + right) / 2;
            merge(left,mid);
            merge(mid+1,right);

            int p = left;
            int q = mid + 1;
            int idx = p;

            while (p<=mid || q<=right){
                if (q>right || (p<=mid && src[p]<src[q])){
                    tmp[idx++] = src[p++];
                }else {
                    tmp[idx++] = src[q++];
                }
            }

            if (right + 1 - left >= 0) System.arraycopy(tmp, left, src, left, right + 1 - left);



        }
    }


}
