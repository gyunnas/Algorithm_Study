import collections


class Solution(object):
    def groupAnagrams(self, strs):
        anagram = collections.defaultdict(list)

        for word in strs:
            anagram["".join(sorted(word))].append(word)

        return anagram.values()
