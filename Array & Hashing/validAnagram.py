class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
        


if __name__ == "__main__":
    sol = Solution()
    s = "racecar"
    t = "carrace"
    print(sol.isAnagram(s, t))
        