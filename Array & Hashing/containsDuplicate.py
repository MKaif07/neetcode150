class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,3]
    print(sol.hasDuplicate(nums))
        