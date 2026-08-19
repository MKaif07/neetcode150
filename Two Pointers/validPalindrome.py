class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''
        for c in s:
            if c.isalnum():
                cleaned += c.lower()
        return cleaned == cleaned[::-1]
            
if __name__ == "__main__":
    sol = Solution()
    s = "Was it a car or a cat I saw?"
    print(sol.isPalindrome(s))