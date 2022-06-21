package broute_force;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class GoldMinSoo1527 {

    static long start,end,total;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine()," ");

        StringBuilder sb = new StringBuilder();

        start = Long.parseLong(st.nextToken());
        end = Long.parseLong(st.nextToken());

        total = 0;

        solve(4);
        solve(7);


        sb.append(total);

        System.out.println(sb);
    }

    public static void solve(long number){
        if (number > end)
            return;
        if (number >= start)
            total += 1;
        solve(number*10+4);
        solve(number*10+7);
    }
}
