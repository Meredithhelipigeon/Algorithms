class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        r = len(height) - 1
        l = 0
        while r-l>0:
            if height[l] < height[r]:
                area = height[l] * (r - l)
            else:
                area = height[r] * (r - l)
            if area > res:
                res = area
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return res
