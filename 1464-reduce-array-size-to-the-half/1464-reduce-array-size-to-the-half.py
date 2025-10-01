from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        total = sum(counter.values())
        target = total / 2
        half = 0
        result = 0
        for c in counter.most_common():
            half += c[1]
            result += 1
    
            if half >= target:
                return result

        return result

