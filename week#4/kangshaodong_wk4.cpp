// week4: find the disappeared numbers
// @kangshaodong

#include <stdio.h>
#include <iostream>
#include <vector>
using std::vector;

class Solution {

public:

	Solution(){}

	vector<int> findDisappearedNumbers(vector<int>& nums) {
		for (int i=0; i<nums.size(); i++)
			idx.push_back(i+1);
		for (int i=0; i<nums.size(); i++)
			idx[nums[i]-1]=-1;
		for (vector<int>::iterator j=idx.begin(); j!=idx.end();)
		{
			if (-1 == *j)
			{
				j = idx.erase(j);
				continue;
			}
			else
				j++;
		}
		return idx;
	}

private:
	vector<int> idx;

};

void main()
{
	int inputs[8] = {4,3,2,7,8,2,3,1};
	vector<int> vi;
	for (int i=0; i<8; i++)
		vi.push_back(inputs[i]);
	Solution sl;
	vector<int> result = sl.findDisappearedNumbers(vi);

	std::cout << "The Input Array is: ";
	for (int j = 0; j < 8; j++)
	{
		std::cout << inputs[j] << " ";
	}
	std::cout << std::endl;

	std::cout << "The Disappeared Numbers are: ";
	for (int j = 0; j < result.size();j++)
		std::cout << result[j] << " ";
	std::cout << std::endl;

	system("pause");
}












