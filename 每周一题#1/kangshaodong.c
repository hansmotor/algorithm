#include <stdio.h>
#include <stdlib.h>

void bubble_sort(int a[], int n);
int combos(int amount, int arr[], int len, int num, int iter);

void main()
{
	int amount, denom, arr[500], i=0, len, num=0, iter=0;
	char c;

	printf("Input-amount:");
	scanf("%d",&amount);

	printf("Input-denomination:");
	while(1)
	{
		scanf("%d",&denom);
		c=getchar();
		arr[i++]=denom;
		if(c=='\n'){
			break;
		}
	}
	len=i;
	bubble_sort(arr,len);

	printf("Output-combinations:\n");
	num = combos(amount,arr,len, num, iter);
	printf("Output: %d combinations in total.",num);

	getchar();
}

//bubble_sort
void bubble_sort(int a[], int n)
{
	int i, j, temp;
	for (j = 0; j < n - 1; j++)
		for (i = 0; i < n - 1 - j; i++)
		{
			if(a[i] > a[i + 1])
			{
				temp = a[i];
				a[i] = a[i + 1];
				a[i + 1] = temp;
			}
		}
}

//print out combinations
int combos(int amount, int arr[], int len, int num, int iter)
{
	int i, j;
	int amount_less;
	iter++;
	for (i = 0; i <= amount/arr[len-1]; i++)
	{
		if(len>1)
		{
			if((i>0)&&(iter!=1))
			{
				for(j=1; j<=iter-1; j++)
				{
					printf("      ");
				}
			}
		}

		if(amount - i*arr[len-1] == 0)
		{
			printf("%dX%d\n",i,arr[len-1]);
			num++;
		}
		else
		{
			if(len>1)
			{
				printf("%dX%d + ",i,arr[len-1]);
				amount_less = amount - i * arr[len-1];
				num = combos(amount_less, arr, len-1, num, iter);
			}
		}
	}
	return num;
}
