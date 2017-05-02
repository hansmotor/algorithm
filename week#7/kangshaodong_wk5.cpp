// week5: Find all unique triplets in the array which gives the sum of zero.
// kangshaodong

#include <stdio.h>
#include <stdlib.h>

void pseudo_bubble_sort(int a[], int n, int split);
//int combos(int amount, int arr[], int len, int num, int iter);

void main()
{
	//int amount, denom, arr[500], i=0, len, num=0, iter=0;
	int item, arr[500], i=0, len, splitnum;
	char c;

	printf("Input Array:");
	while(1)
	{
		scanf("%d",&item);
		c=getchar();
		arr[i++]=item;
		if(c=='\n'){
			break;
		}
	}
	len=i;

	printf("Input Split Number:");
	scanf("%d",&splitnum);

	pseudo_bubble_sort(arr, len, splitnum);

	printf("The List Partitioned:\n[");
	for (i=0; i<len; i++)
	{
		printf("%d ", arr[i]);
	}
	printf("]\n");
	//num = combos(amount,arr,len, num, iter);
	//printf("Output: %d combinations in total.",num);

	system("pause");
}

//bubble_sort
void pseudo_bubble_sort(int a[], int n, int split)
{
	int i, j, temp;
	for (j = 0; j < n - 1; j++)
		for (i = 0; i < n - 1 - j; i++)
		{
			if((a[i] >= split) && (a[i+1] < split))
			{
				temp = a[i];
				a[i] = a[i + 1];
				a[i + 1] = temp;
			}
		}
}

//print out combinations
/*int combos(int amount, int arr[], int len, int num, int iter)
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
}*/









