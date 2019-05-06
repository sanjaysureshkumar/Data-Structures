#include <stdlib.h>
using namespace std;
int kadane(int a[],int n){
    int curMax,gMax,i;
    curMax=a[0];
    gMax=a[0];
    for(i=1;i<n;i++)
    {
        curMax=max(a[i],curMax+a[i]);
        gMax=max(curMax,gMax);
    }
    return gMax;
}
int main() {
	int t,n;
	cin>>t;
	while(t--)
	{
	    cin>>n;
	    int a[n];
	    for(int i=0;i<n;i++) 
	    cin>>a[i];
	   cout<<kadane(a,n)<<endl;
	}
	return 0;
}

