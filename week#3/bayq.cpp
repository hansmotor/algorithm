#include<iostream>

#include <string>
using namespace std;

class Solution {
public:
	int numDecodings(string s) {
		int len = s.length();
		for (int i = 0; i < len + 2; i++) { num_cache[i] = -1; }
		return numDecodings(s, 0);
	}

	int numDecodings(string& s, int start) {
		int ls = s.length();
		if (ls == 0) { return 0; }
		int ret = 1;  // 前面是乘法过来的，当为空的时候，这里的返回值应该是1.
		if (start < ls) {
			int num1 = 0;
			int num2 = 0;
			if (numDecodings1(s, start) != 0) {
				if (num_cache[start + 1] != -1) {
					num1 = num_cache[start + 1];
				}
				else {
					num1 = numDecodings(s, start + 1);
					num_cache[start + 1] = num1;
				}
			}
			if (numDecodings2(s, start) != 0) {
				if (num_cache[start + 2] != -1) {
					num2 = num_cache[start + 2];
				}
				else {
					num2 = numDecodings(s, start + 2);
					num_cache[start + 2] = num2;
				}
			}
			ret = num1 + num2;
		}
		//cout << "num s=" << s << " start=" << start << " num=" << ret << endl;
		return ret;
	}

	int numDecodings1(string& s, int start) {
		int ret = 0;
		if (start < s.length()) {
			ret = s[start] == '0' ? 0 : 1;
		}
		//cout << "num1 s=" << s << " start=" << start << " num=" << ret << endl;
		return ret;
	}

	int numDecodings2(string& s, int start) {
		int ret = 0;
		if (start < s.length() - 1) {
			if (s[start] == '1' || s[start] == '2' && s[start + 1] < '7') { ret = 1; }
		}
		//cout << "num2 s=" << s << " start=" << start << " num=" << ret << endl;
		return ret;
	}
private:
	int num_cache[10240];
};
int main(void)
{
	cout << "输入数字串" << endl;
	string number_s;
	getline(cin, number_s);
	class Solution CPZ;
	//CPZ.numDecodings(number_s);
	cout << "种数为  " << CPZ.numDecodings(number_s)<<endl;


}
