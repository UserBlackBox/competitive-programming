// https://dmoj.ca/problem/dmopc17c1p1
// https://dmoj.ca/submission/2212443

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class dmopc17c1p1 {
    public static void main(String[] args) {
        try{
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            String temp = br.readLine();
            int r = Integer.parseInt(temp.split(" ")[0]);
            int c = Integer.parseInt(temp.split(" ")[1]);
            ArrayList<Integer[]> beings = new ArrayList<Integer[]>();
            for(int i=0;i<r;i++){
                temp = br.readLine();
                for(int j=0;j<c;j++){
                    if(temp.charAt(j)=='X'){
                        beings.add(new Integer[]{j+1,i+1});
                    }
                }
            }
            int q = Integer.parseInt(br.readLine());
            for(int i=0;i<q;i++){
                temp = br.readLine();
                int x = Integer.parseInt(temp.split(" ")[0]);
                int y = Integer.parseInt(temp.split(" ")[1]);
                boolean visible = false;
                for(Integer[] j:beings){
                    if(j[0] == x || j[1] == y){
                        visible = true;
                        break;
                    }
                }
                if(visible){
                    System.out.println('Y');
                }else{
                    System.out.println('N');
                }
            }
            br.close();
        }catch(IOException e){}
    }
}
