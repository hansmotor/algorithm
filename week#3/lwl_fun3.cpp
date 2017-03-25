#include <iostream>
#include <map>
#include <string>

using namespace std;

int cal_decode(string &s);

int main()
{
	map<int, char> enummap;
	enummap.insert(map<int, char>::value_type(1,'A'));
	enummap.insert(map<int, char>::value_type(2,'B'));
	enummap.insert(map<int, char>::value_type(3,'C'));
	enummap.insert(map<int, char>::value_type(4,'D'));
	enummap.insert(map<int, char>::value_type(5,'E'));
	enummap.insert(map<int, char>::value_type(6,'F'));
	enummap.insert(map<int, char>::value_type(7,'G'));
	enummap.insert(map<int, char>::value_type(8,'H'));
	enummap.insert(map<int, char>::value_type(9,'I'));
	enummap.insert(map<int, char>::value_type(10,'J'));
	enummap.insert(map<int, char>::value_type(11,'K'));
	enummap.insert(map<int, char>::value_type(12,'L'));
	enummap.insert(map<int, char>::value_type(13,'M'));
	enummap.insert(map<int, char>::value_type(14,'N'));
	enummap.insert(map<int, char>::value_type(15,'O'));
	enummap.insert(map<int, char>::value_type(16,'P'));
	enummap.insert(map<int, char>::value_type(17,'Q'));
	enummap.insert(map<int, char>::value_type(18,'R'));
	enummap.insert(map<int, char>::value_type(19,'S'));
	enummap.insert(map<int, char>::value_type(20,'T'));
	enummap.insert(map<int, char>::value_type(21,'U'));
	enummap.insert(map<int, char>::value_type(22,'V'));
	enummap.insert(map<int, char>::value_type(23,'W'));
	enummap.insert(map<int, char>::value_type(24,'X'));
	enummap.insert(map<int, char>::value_type(25,'Y'));
	enummap.insert(map<int, char>::value_type(26,'Z'));

	string s = "120";
	cout<<"code = "<<s<<endl;
	cout<<"way of decode = "<<cal_decode(s)<<endl;

	return 0;
}

int cal_decode(string &s)
{
	if (0 == s.length() || '0' == s[0])
		return 0;

	int *num = new int[s.length()] ();
	num[0] = 1;                         //1 ... 9
	if ((s[0] > '2' && s[1] != '0') || (s[0] < '3' && s[1] == '0'))      //27 37 10 20...
		num[1] = 1;
	else if((s[0] == '1' || (s[1] == '2' && s[1] <= '6')) && s[1] != 0)      //11 ... 26
		num[1] = 2;
	else                                //40 50...
		num[1] = 0;
	
	for (int i = 2; i < s.length(); i++)
	{
		if (s[i] == '0')
		{	
			if (s[i-1] == '1' || s[i-1] == '2')     //120 110 910...
			{
				num[i] = num[i-2];
			}
			else                       //190 130 530...
				num[i] = 0;
		}
		else if(s[i] != '0')
		{
			if(s[i-1] == '1' || (s[i-1] == '2' && s[i] < '7'))  //211 911...
			{
				num[i] = num[i-1] + num[i-2];
			}
			else
				num[i] = num[i-1];
		}
	}
	return num[s.length()-1];
}
