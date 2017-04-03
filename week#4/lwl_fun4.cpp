#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

class MySolution
{
public:
	MySolution(){cout<<"-------------Test-------------\n";};
	~MySolution(){};

	vector<int> findDisappearedNumbers(vector<int>& nums)
	{
		int n = nums.size();
		vector<int> res;
		int *count = new int [n+1] ();  //新建一个数组统计个数
		for(int i=0; i<n; i++)
		{
			count[nums[i]] = count[nums[i]] + 1;
		}
		bool isrecnt = false;
		for(int i=1; i<=n; i++)
		{
			if(count[i]==0)
			{
				res.push_back(i);
			}
			if (count[i]>1)
			{
				isrecnt = true;
			}
		}
		if (isrecnt)
			return res;
		else
		{
			res.clear();
			return res;
		}
	}
private:

};

int main()
{
	vector<int> mResult;
	vector<int> mInput;
	mInput.push_back(4);
	mInput.push_back(3);
	mInput.push_back(2);
	mInput.push_back(7);
	mInput.push_back(8);
	mInput.push_back(2);
	mInput.push_back(2);
	mInput.push_back(3);
	MySolution m_findnum;
	mResult = m_findnum.findDisappearedNumbers(mInput) ;
	if (mResult.empty())
	{
		cout<<"Error"<<endl;
		return 0;
	}
	cout<<"Disappear Number: ";
  vector<int>::iterator it;
	for(it=mResult.begin();it!=mResult.end();it++)
		cout<<*it<<" ";
	cout<<endl;
	return 0;
}

