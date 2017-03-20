#include <stdio.h>
#include <iostream>

bool CalculateLoop(int *num, int *t_array, int i, int n)
{
	int tmp;
	int checkcount = n + 1;
	if (t_array[i] > 0)
	{
		tmp = (num[i] + t_array[i])%n;
		while (checkcount--)
		{
			if (t_array[tmp] > 0)
			{
				tmp = (num[tmp] + t_array[tmp])%n;
			}
			else
				return false;

			if (num[tmp] == num[i])
				return true;
			else if (t_array[tmp] < 0)
				return false;
		}
	}
	else if (t_array[i] < 0)
	{
		tmp = (num[i] - t_array[i])%n;
		while (checkcount--)
		{
			if (t_array[tmp] < 0)
			{
				tmp = (num[tmp] - t_array[tmp])%n;
			}
			else
				return false;

			if (num[tmp] == num[i])
				return true;
			else if (t_array[tmp] < 0)
				return false;
		}
	}
	else
		return false;

}

void main()
{
	int n = 0;
	printf("Please enter the length of array:");
	scanf("%d",&n);

	int *my_array = new int[n];
	int *num = new int [n];
	printf("\nPlease enter the array:");
	for(int i = 0; i < n; i++)
	{
		scanf("%d",&my_array[i]);
		num[i] = i;
	}

	printf("\n---------Start calculate-------\n");
	bool ret = false;
	int count = 0;

	for (int i = 0; i < n; i++)
	{
		if (my_array[i] > 0)
		{
			if(i == (num[i] + my_array[i])%n)
			{
				ret = false;
				continue;
			}
		}
		else if (my_array[i] < 0)
		{
			if(i == (num[i] - my_array[i])%n)
			{
				ret = false;
				continue;
			}
		}

		ret = CalculateLoop(num, my_array, i, n);
		if (ret)
		{
			count++;
			printf("Index from %d.\n",i);
		}
	}


	if (count > 0)
		printf("There are %d loop in the array.\n" , count);
	else
		printf("There is no loop.\n");

}
