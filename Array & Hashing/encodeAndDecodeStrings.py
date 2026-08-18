from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return ""
        newStrs = []
        for st in strs:
            newStrs.append(st)
            newStrs.append("$#%")
            
        return "".join(newStrs)


    def decode(self, s: str) -> List[str]:
        if not str: return []
        return s.split("$#%")[:-1]
    
    
if __name__ == "__main__":
    sol = Solution()
    
    strs = ["Hello","World"]
    result = sol.encode(strs)
    print(result)
    print(sol.decode(result))