// week6-ssx.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <stdio.h>
#include <cstdlib>  
#include <vector>
#include <algorithm>
#include <string>
using namespace std;


class Solution 
{
public:
	int Dfs(vector<vector<int>>& matrix, vector<vector<int>>& record, int x, int y, int lastVal)
	{
		int mHeight = matrix.size();
		int mWidth  = matrix[0].size();
		if (x < 0 || y < 0 || x >=mHeight || y >=mWidth ) 
			return 0;
		if (matrix[x][y] > lastVal)
		{
			if (record[x][y] != 0) 
				return record[x][y]; 
			int left   =  Dfs(matrix, record, x + 1, y, matrix[x][y]) + 1;
			int right  =  Dfs(matrix, record, x - 1, y, matrix[x][y]) + 1;
			int top    =  Dfs(matrix, record, x, y + 1, matrix[x][y]) + 1;
			int bottom =  Dfs(matrix, record, x, y - 1, matrix[x][y]) + 1;
			record[x][y] = max(left, max(right, max(top, bottom)));
			return record[x][y];
		}
		return 0;
	}
	int LongestIncreasingPath(vector<vector<int>>& matrix) 
	{
		if (matrix.size() == 0) 
			return 0;
		vector<int> temp(matrix[0].size(), 0);
		vector<vector<int>> record(matrix.size(), temp);
		int longest = 0;
		for (int i = 0; i < matrix.size(); ++i)
			for (int j = 0; j < matrix[0].size(); ++j)
				longest = max(longest, Dfs(matrix, record, i, j, -1));
		return longest;
	}
};


int _tmain(int argc, _TCHAR* argv[])
{
	vector<vector<int>>mResult;
	vector<int>mInput1;
	vector<int>mInput2;
	vector<int>mInput3;
	mInput1.push_back(1);
	mInput1.push_back(0);
	mInput1.push_back(2);
	mInput2.push_back(2);
	mInput2.push_back(3);
	mInput2.push_back(5);
	mInput3.push_back(6);
	mInput3.push_back(9);
	mInput3.push_back(4);
	mResult.push_back(mInput1);
	mResult.push_back(mInput2);
	mResult.push_back(mInput3);
	Solution m_solution;
	//1 0 2
	//2 3 5
	//6 9 4
	//result 0 -1 -2 -3 -9
	int longth = m_solution.LongestIncreasingPath(mResult) ;

	printf("-------------LongestIncreasingPath = %d----------------\r\n",longth);

	return 0;
}