#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
	vector<vector<int>> threeSum(vector<int>& nums)
	{
		vector<vector<int>> res;
		sort(nums.begin(), nums.end());
		for(int i = 0; i < nums.size(); i++)
		{
			if(i > 0 && nums[i] == nums[i-1])  //去重复
				continue;
			twoSum(nums, res, i);
		}
		return res;
	}

	/*using 2-sum algorithm*/
	void twoSum(vector<int> &num, vector<vector<int>> &res, int targetIndex)
	{
		int i = targetIndex + 1;      //头指针
		int j = num.size()-1;         //尾指针

		while(i < j)
		{
			int sum = num[i] + num[j];
			if (sum == -num[targetIndex])
			{
				vector<int> v;
				v.push_back(num[targetIndex]);
				v.push_back(num[i]);
				v.push_back(num[j]);
				res.push_back(v);
				i++;
				j--;
				while(i < num.size() && num[i] == num[i-1])  //去重复
					i++;
				while(j >= 0 && num[j] == num[j+1])
					j--;
			}
			else if(sum < -num[targetIndex])
				i++;
			else if(sum > -num[targetIndex])
				j--;
		}
	}

};

int main()
{
	vector<int> mInput;
	mInput.push_back(-1);
	mInput.push_back(0);
	mInput.push_back(1);
	mInput.push_back(1);
	mInput.push_back(1);
	mInput.push_back(2);
	mInput.push_back(-1);
	mInput.push_back(-4);
	mInput.push_back(2);
	vector<vector<int>> res;
	Solution test;
	res = test.threeSum(mInput);
	for (int i = 0; i < res.size(); i++)
	{
		cout<<"Combination"<<i+1<<":  ";
		for (int j = 0; j < res[i].size(); j++)
			cout << res[i][j] << " ";
		cout << endl;
	}
	return 0;
}
