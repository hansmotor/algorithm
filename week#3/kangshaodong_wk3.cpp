// week3: decoding letters
// @kangshaodong

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <string.h>

char input[100], content[50];
char letters[27] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
int len, combcnt=0;

void main()
{
	void decode(int in_idx, int charcnt); 

	int i = 0, elem;
	char c;

	//Receive the input code(in numbers)
	printf("Input codes: ");
	scanf("%s",&input);
	len = strlen(input);

	//Compute all the combinations
	decode(0, 0);
	printf("There are %d decoding results.\n",combcnt);

	system("pause");
}

//Sub-function for decoding
void decode(int in_idx, int charcnt)
{
	if(len == in_idx)
	{
		printf("\n");
		combcnt += 1;
	}
	else
	{
		if(in_idx <= len-1)
		{
			char output[1];
			output[0] = input[in_idx];
			printf("%c", letters[atoi(output)-1]);
			charcnt += 1;
			in_idx += 1;
			decode(in_idx, charcnt);
		} 

		charcnt -= 1;
		in_idx -= 1;
		
		if(in_idx <= len-2)
		{
			char output1[2];
			output1[0] = input[in_idx];
			output1[1] = input[in_idx+1];
			int abc_idx = atoi(output1);
			if(abc_idx <= 26)
			{
				int tempcnt = charcnt;
				while(tempcnt-- > 0)
					printf("-");
				printf("%c",letters[abc_idx-1]);
				charcnt += 1;
				in_idx += 2;
				decode(in_idx, charcnt);
			}
		}
	}
	return;
}
