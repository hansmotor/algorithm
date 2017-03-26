#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


class Solution(object):

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.number = 0
        self.jie(s, [])
        return self.number

    def jie(self, target, result):
        if not target:
            if result:
                self.number += 1
            return

        zimu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        new_result = result[:]
        new_result.append(zimu[int(target[0]) - 1])
        self.jie(target[1:], new_result)
        if len(target) >= 2 and 0 < int(target[:2]) < 27:
            new_result = result[:]
            new_result.append(zimu[int(target[:2]) - 1])
            self.jie(target[2:], new_result)


if __name__ == "__main__":
    target = sys.argv[1]
    solution = Solution()
    print solution.numDecodings(target)
