// weeks-ssx.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <stdio.h>
#include <cstdlib>  
#include <vector>
#include <string>
using namespace std;

//week3-------------------
class DecodeWay 
{

public:
	vector<char> code;
public:
	int WayDecoding(const string &str) 
	{
		if (str.empty() || str[0] == '0') 
			return 0;
		if (str.size()==1) 
			return 1;
		int left = 0;
		int result = 1;
		for (size_t i = 1; i <= str.size(); i++) 
		{
			if (str[i-1] == '0') 
				result = 0;
			if (i < 2 || !(str[i - 2] == '1' ||(str[i - 2] == '2' && str[i - 1] <= '6')))
				left = 0;
			int tmp = result;
			result = left + result;
			left = tmp;
		}
		return result;
	}
};

int _tmain(int argc, _TCHAR* argv[])
{
	DecodeWay m_decodeway;
    int temp =m_decodeway.WayDecoding("12") ;
	printf("-----------------------------\r\n");
	printf("结果：%d\r\n",temp);
	printf("-----------------------------\r\n");

	return 0;
}

