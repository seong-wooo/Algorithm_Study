from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for strr in strs:
            d[''.join((sorted(strr)))].append(strr)

        return d.values()
