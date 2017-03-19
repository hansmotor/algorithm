// week2: loop detection 
// @kangshaodong

#include "stdio.h"
#include "math.h"

int arr[50], flag[50], len, loopCnt=0, loopStartIndex[50];

void main()
{
	int checkloop(int j);
	int i=0, elem;
	char c;

	printf("Input Array: ");
	while(1)
	{
		scanf("%d",&elem);
		c=getchar();
		arr[i++]=elem;
		if(c=='\n')
			break;
	}
	len = i;

	for(i=0; i<len; i++)
	{
		flag[i] = checkloop(i);
	}
	printf("%d loop(s) are found",loopCnt);
	if(loopCnt > 0)
	{
		for(int n=0; n<loopCnt; n++)
		{
			int k = loopStartIndex[n];
			do 
			{
				(k == loopStartIndex[n]) ? printf(":\nIndex: [%d]",k) : printf(" -> [%d]",k);
				k = k + arr[k];
				while (k < 0)
					k = k + len;
				k = k % len;
			} while (k != loopStartIndex[n]);
		}
	}

	getchar();
}

int checkloop(int j)
{
	if(-1==flag[j])
		return -1;
	else
	{
		if (1==flag[j])
		{
			loopCnt = loopCnt + 1;
			loopStartIndex[loopCnt-1] = j;
			return -1;
		} 
		else
		{
			if (0 == (arr[j] % len))
			{
				flag[j] = -1;
				return -1;
			} 
			else
			{
				flag[j] = 1;
				int k = j + arr[j];
				while (k < 0)
					k = k + len;
				flag[j] = checkloop(k % len);
				return flag[j];
			}
		}
	}
}
