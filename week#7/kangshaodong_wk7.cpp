// week7: list partition
// kangshaodong

#include <stdio.h>
#include <stdlib.h>

void pseudo_bubble_sort(int a[], int n, int split);

void main()
{
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

	system("pause");
}

//pseudo_bubble_sort
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
