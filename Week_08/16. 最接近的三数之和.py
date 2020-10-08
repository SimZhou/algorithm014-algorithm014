# https://leetcode-cn.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        _min = float('inf')
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                candidate = nums[i] + nums[l] + nums[r]
                if abs(candidate - target) < _min: 
                    _min = abs(candidate - target)
                    _minP = candidate
                if candidate < target: 
                    l += 1
                    continue
                elif candidate > target:
                    r -= 1
                    continue
                elif candidate == target:
                    return candidate
        return _minP