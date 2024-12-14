class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic={}
        for num in nums:
            if num in dic:
                return True
            else:
                dic[num]=1
        return False

# Time complexity: O(n)
# Space complexity: O(n)
# https://leetcode.com/problems/contains-duplicate/description/