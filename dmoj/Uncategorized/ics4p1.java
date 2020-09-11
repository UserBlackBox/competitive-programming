// https://dmoj.ca/problem/ics4p1
// https://dmoj.ca/submission/3007419

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class ics4p1 {
    public static void main(String[] args){
        char[] chars = new char[0];
        try{
            BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
            chars = in.readLine().toCharArray();
            in.close();
        }catch(IOException e){}
        Arrays.sort(chars);
        combinations(chars,"");
    }

    public static void combinations(char[] chars, String assembled){
        if(assembled.length()==chars.length-1){
            for(char i:chars){
                if(assembled.indexOf(i)!=-1){
                    continue;
                }
                System.out.println(assembled+i);
            }
            return;
        }
        for(char i:chars){
            if(assembled.indexOf(i)!=-1){
                continue;
            }
            combinations(chars,assembled+i);
        }
    }
}

