from collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        paragraph = re.sub("[^a-zA-Z]"," ", paragraph).lower()
        counter = Counter(paragraph.split())

        for most in counter.most_common():
            if most[0] not in banned:
                return most[0]
