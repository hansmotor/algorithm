#include <iostream>
#include <algorithm>
using namespace std;
#define MAX 500
 int v[MAX];

int fun(int n , int m)
	{
		if (n<0) return 0;  
		if (n == 0) return 1;  
		if (m<0) return 0;
		return fun(n,m-1)+fun(n-v[m],m);
	}

void main()
{	
	int a[MAX];
	int i;
	cout<<"Input the denominations..."<<endl;
	for (i=0;;i++)
	{
		cin>>a[i];
		if (getchar()=='\n')
			break;
	}
	std::sort(a,a+i+1);
	cout<<"Denominations in ascending order is:"<<endl;
	for(int j=0;j<i+1;j++)
	{	v[j]=a[j];
		cout<<" "<<a[j];cout<<endl; //get the denominations	
	}

	int amount=0;
	cout<<"Please input the amount varied in [0,5000]:"<<endl;
	cin>>amount;
	if (amount>5000||amount<0)
		cout<<"Warning! The amount should be in range of [0,5000]¡£ "<<endl;
	else
		cout<<"The number of combinations is :\n"<<fun(amount,i)<<endl;
		
}