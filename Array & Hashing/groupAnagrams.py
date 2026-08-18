from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # creates a key which we look for with an empty list as value
        for s in strs:
            sortedS = "".join(sorted(s)) # returns an array of characters, join them to an empty string
            res[sortedS].append(s)
        return list(res.values())
            
if __name__ == "__main__":
    sol = Solution()
    strs = ["act","pots","tops","cat","stop","hat"]
    print(sol.groupAnagrams(strs))