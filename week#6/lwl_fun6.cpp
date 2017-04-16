#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct pixel
{
	int x;
	int y;
};
vector<pixel> m_path;

class Solution
{
public:
	//边界判断
	bool rightpath(int i, int j, int m, int n)
	{
		if ((j+1) < n && j >= 0)
			return true;
		else if((j+1) >= n || j < 0)
			return false;
		else
			return false;
	}
	bool leftpath(int i, int j, int m, int n)
	{
		if ((j-1) >= 0 && j < n)
			return true;
		else if((j-1) < 0 || j >=n)
			return false;
		else
			return false;
	}
	bool downpath(int i, int j, int m, int n)
	{
		if ((i+1) < m && i >= 0)
			return true;
		else if((i+1) >= m || i < 0)
			return false;
		else
			return false;
	}
	bool uppath(int i, int j, int m, int n)
	{
		if ((i-1) >=0 && i < m)
			return true;
		else if((i-1) < 0 || i >=m)
			return false;
		else
			return false;
	}

	int longestIncreasingPath(vector<vector<int>>& matrix)
	{
		if (matrix.size() == 0)
			return 0;
		int m = matrix.size();    //row
		int n = matrix[0].size(); //column
		int longest = 0;
		int ret;
		int record[4] = {0, 0, 0, 0};

		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
				ret = findlongpath(matrix, i, j, m, n, record);
				if (ret > longest)
				{
					longest = ret;
					int pathsize = m_path.size();
					cout << "Path: " ;
					for (int k = 0; k < pathsize-1; k++)
					{
						cout << matrix[m_path.at(k).x][m_path.at(k).y] << "->";
					}
					cout << matrix[m_path.at(pathsize-1).x][m_path.at(pathsize-1).y];
					cout << endl;
				}
				m_path.clear();
			}
		}
		return longest;
	}

	int findlongpath(vector<vector<int>>& matrix, int i, int j, int m, int n, int *record)
	{
		int pathright,pathleft,pathdown,pathup;
		if (rightpath(i, j, m, n) && matrix[i][j+1]>matrix[i][j])
		{
			pathright = matrix[i][j];
			pixel temp;
			temp.x = i, temp.y = j;
			m_path.push_back(temp);
			pathright += findlongpath(matrix, i, j+1, m, n, record);
		}
		else
			pathright = matrix[i][j];

		if (leftpath(i, j, m, n) && matrix[i][j-1]>matrix[i][j])
		{
			pathleft = matrix[i][j];
			pixel temp;
			temp.x = i, temp.y = j;
			m_path.push_back(temp);
			pathleft += findlongpath(matrix, i, j-1, m, n, record);
		}
		else
			pathleft = matrix[i][j];

		if (downpath(i, j, m, n) && matrix[i+1][j]>matrix[i][j])
		{
			pathdown = matrix[i][j];
			pixel temp;
			temp.x = i, temp.y = j;
			m_path.push_back(temp);
			pathdown += findlongpath(matrix, i+1, j, m, n, record);
		}
		else
			pathdown = matrix[i][j];

		if (uppath(i, j, m, n) && matrix[i-1][j]>matrix[i][j])
		{
			pathup = matrix[i][j];
			pixel temp;
			temp.x = i, temp.y = j;
			m_path.push_back(temp);
			pathup += findlongpath(matrix, i-1, j, m, n, record);
		}
		else
			pathup = matrix[i][j];

		int ret = max(pathright, max(pathleft, max(pathdown, pathup)));

		if (pathright == pathleft && pathleft == pathdown && pathdown == pathup) //无路可走
		{
			pixel temp;
			temp.x = i, temp.y = j;
			m_path.push_back(temp);
		}

		return ret;
	}
};

int main()
{
	vector<vector<int>> matrix;
	vector<int> test;
	test.push_back(9);
	test.push_back(9);
	test.push_back(4);
	matrix.push_back(test);
	test.clear();
	test.push_back(6);
	test.push_back(6);
	test.push_back(8);
	matrix.push_back(test);
	test.clear();
	test.push_back(2);
	test.push_back(1);
	test.push_back(1);
	matrix.push_back(test);
	test.clear();
	
	cout << "Below is the input array:" << endl;
	for (int i = 0 ; i < matrix.size(); i++)
	{
		for (int j = 0; j < matrix[i].size();j++)
		{
			cout << matrix[i][j] << " ";
		}
		cout << endl;
	}

	Solution mysol;
	int ret = mysol.longestIncreasingPath(matrix);
	cout << "The longest increasing path is: " << ret <<endl;

	while (true)
	{

	}
	return 0;
}
