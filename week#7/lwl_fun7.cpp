#include <iostream>

using namespace std;

struct ListNode
{
	int val;
	ListNode *next;
	ListNode (int x) : val(x), next(NULL){}
};

class Solution
{
public:
	ListNode *partition (ListNode *head, int x)
	{
		ListNode p = ListNode(0);
		ListNode *pHead = &p;
		ListNode q = ListNode(0);
		ListNode *qHead = &q;

		while (head != NULL)
		{
			if (head->val < x)
			{
				pHead->next = head;
				pHead = pHead->next;
			}
			else
			{
				qHead->next = head;
				qHead = qHead->next;
			}
			head = head->next;
		}
		pHead->next = q.next;
		qHead->next = NULL;
		return p.next;
	}
};

int main()
{
	ListNode n1 = ListNode(1);
	ListNode n2 = ListNode(4);
	ListNode n3 = ListNode(3);
	ListNode n4 = ListNode(2);
	ListNode n5 = ListNode(5);
	ListNode n6 = ListNode(2);
	n1.next = &n2; n2.next = &n3; n3.next = &n4; n4.next = &n5; n5.next = &n6;

	Solution test;
	ListNode *p = test.partition(&n1, 3);
	while (p != NULL)
	{
		cout << p->val << " ";
		p = p->next;
	}
	cout << endl;
	return 0;

}
