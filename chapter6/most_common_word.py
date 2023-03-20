import re
import collections


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        words = [
            word for word in re.sub(r"[^\w]", " ", paragraph.lower()).split() if word not in banned
        ]

        count = collections.defaultdict(int)

        for word in words:
            count[word] += 1

        return max(count, key=count.get)
