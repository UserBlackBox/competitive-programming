// https://dmoj.ca/problem/hkccc15j3
// https://dmoj.ca/submission/3036377

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class hkccc15j3{
    public static void main(String[] args){
        boolean[][] board = new boolean[0][0];
        int[][] queens = new int[0][2];
        int n = 0;
        int m = 0;
        int free = 0;
        try {
            BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
            String[] temp = in.readLine().split(" ");
            n = Integer.parseInt(temp[0]);
            m = Integer.parseInt(temp[1]);
            board = new boolean[n][n];
            queens = new int[m][2];
            free = n*n;
            for(int i=0;i<m;i++){
                temp = in.readLine().split(" ");
                queens[i][0] = Integer.parseInt(temp[0]);
                queens[i][1] = Integer.parseInt(temp[1]);
            }
        } catch (IOException e) {}
        for(int[] i:queens){
            int x = i[0]-1;
            int y = i[1]-1;
            if(!board[x][y]){
                board[x][y] = true;
                free--;
            }
            for(int j=1;j<n;j++){
                if(x+j>=0 && x+j<n && !board[x+j][y]){
                    board[x+j][y] = true;
                    free--;
                }
                if(x-j>=0 && x-j<n && !board[x-j][y]){
                    board[x-j][y] = true;
                    free--;
                }
                if(y+j>=0 && y+j<n && !board[x][y+j]){
                    board[x][y+j] = true;
                    free--;
                }
                if(y-j>=0 && y-j<n && !board[x][y-j]){
                    board[x][y-j] = true;
                    free--;
                }
                if(x-j>=0 && x-j<n && y-j>=0 && y-j<n && !board[x-j][y-j]){
                    board[x-j][y-j] = true;
                    free--;
                }
                if(x+j>=0 && x+j<n && y-j>=0 && y-j<n && !board[x+j][y-j]){
                    board[x+j][y-j] = true;
                    free--;
                }
                if(x+j>=0 && x+j<n && y+j>=0 && y+j<n && !board[x+j][y+j]){
                    board[x+j][y+j] = true;
                    free--;
                }
                if(x-j>=0 && x-j<n && y+j>=0 && y+j<n && !board[x-j][y+j]){
                    board[x-j][y+j] = true;
                    free--;
                }
            }
        }
        System.out.println(free);
    }
}