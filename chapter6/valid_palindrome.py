# First Solution
import collections


class Solution1(object):
    def isPalindrome(self, s):
        strs = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True


# Second Solution
import re


class Solution2(object):
    def isPalindrome(self, s):
        s = s.lower()

        s = re.sub("[^a-z0-9]", "", s)

        return s == s[::-1]
