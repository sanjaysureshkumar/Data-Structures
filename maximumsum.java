
import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		//code
		int t,l,i;
		Scanner input=new Scanner(System.in);
		t=input.nextInt();
		for(l=0;l<t;l++)
		{
		    int n;
		    n=input.nextInt();
		    int dp[]=new int[n+1];
		    dp[0]=0;
		    dp[1]=1;
		    for(i=2;i<=n;i++)
		    {
		        dp[i]=Math.max(((dp[i/2])+(dp[i/3])+(dp[i/4])),i);
		    }
		    System.out.println(dp[n]);
		}
	}
}
