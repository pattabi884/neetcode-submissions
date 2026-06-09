class Solution:
    def trap(self, height: list[int]) -> int:
        leftMax = []
        maximum = 0
        maxArea = 0
        rightMax = []
        for left in height:
            maximum = max(left, maximum)
            leftMax.append(maximum)
            
        maximum = 0
        print(leftMax)
        for right in range(len(height) - 1, -1, -1):
            maximum = max(height[right], maximum)
            rightMax.append(maximum)
        rightMax = rightMax[::-1]
        print(rightMax)
        for i in range(0, len(height) - 1, 1):
            h = height[i]
            area = min(leftMax[i], rightMax[i]) - h
            maxArea = area + maxArea
        print(maxArea)
        return maxArea

        
        
        
height_input = [0,2,0,3,1,0,1,3,2,1]
sol = Solution()
sol.trap(height_input)