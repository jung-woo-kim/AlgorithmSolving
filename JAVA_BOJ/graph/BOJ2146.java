package graph;

import java.awt.*;
import java.io.*;
import java.util.*;

public class BOJ2146 {
    static int N,num=1,answer=987654321;
    static boolean[][] visit;
    static int[][] map;
    static int[][] dir = { {-1,0},{0,1},{1,0},{0,-1} };

    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        visit = new boolean[N][N];
        map = new int[N][N];

        for(int i=0;i<N;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0;j<N;j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        //섬 구분
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(!visit[i][j] && map[i][j] != 0){
                    Island_num(i,j);
                    num++;
                }
            }
        }
        //방문 초기화
        Init_visit();
        //다리만들기
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(!visit[i][j] && map[i][j] != 0){
                    Make_bridge(i,j,map[i][j]);
                    Init_visit();
                }
            }
        }
        System.out.println(answer);
    }
    public static void Island_num(int y, int x){
        Queue<Point>Q = new LinkedList<Point>();
        visit[y][x] = true;
        Q.offer(new Point(y,x));
        map[y][x] = num;

        while(!Q.isEmpty()){
            int ny = Q.peek().x;
            int nx = Q.peek().y;
            Q.poll();

            for(int i=0;i<4;i++){
                int my = ny + dir[i][0];
                int mx = nx + dir[i][1];

                if(my>=0 && mx>=0 && my<N && mx<N){
                    if(!visit[my][mx] && map[my][mx] == 1){
                        visit[my][mx] = true;
                        map[my][mx] = num;
                        Q.offer(new Point(my,mx));
                    }
                }
            }
        }
    }
    public static void Make_bridge(int y, int x, int start){
        Queue<pos_cnt>Q = new LinkedList<pos_cnt>();
        Q.offer(new pos_cnt(y,x,0));
        visit[y][x] = true;

        while(!Q.isEmpty()){
            int ny = Q.peek().y;
            int nx = Q.peek().x;
            int cnt = Q.peek().cnt;

            Q.poll();

            for(int i=0;i<4;i++){
                int my = ny + dir[i][0];
                int mx = nx + dir[i][1];

                if(my>=0 && mx>=0 && my<N && mx<N){
                    if(!visit[my][mx]){
                        if(map[my][mx] == 0){
                            visit[my][mx] = true;
                            Q.offer(new pos_cnt(my,mx,cnt+1));
                        }
                        else if(map[my][mx] != 0 && map[my][mx] != start){
                            answer = Math.min(answer, cnt);
                            Q.clear();
                            return;
                        }
                    }
                }
            }
        }
    }
    public static void Init_visit(){
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                visit[i][j] = false;
            }
        }
    }
}
class pos_cnt{
    int y;
    int x;
    int cnt;

    pos_cnt(int y, int x, int cnt){
        this.y = y;
        this.x = x;
        this.cnt = cnt;
    }
}
