// https://dmoj.ca/problem/art0
// https://dmoj.ca/submission/2038312

import java.util.*;
public class art0{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int n = Integer.parseInt(in.nextLine());
		for(int i=0;i<n;i++){
			String name = in.nextLine();
			for(int j=0;j<name.length();j++){
				if(name.charAt(j)=='a' || name.charAt(j)=='A') System.out.print("Hi! ");
				else if(name.charAt(j)=='e' || name.charAt(j)=='E') System.out.print("Bye! ");
				else if(name.charAt(j)=='i' || name.charAt(j)=='I') System.out.print("How are you? ");
				else if(name.charAt(j)=='o' || name.charAt(j)=='O') System.out.print("Follow me! ");
				else if(name.charAt(j)=='u' || name.charAt(j)=='U') System.out.print("Help! ");
				else if(Character.isDigit(name.charAt(j))) System.out.print("Yes! ");
			}
			System.out.println();
		}
	}
}
