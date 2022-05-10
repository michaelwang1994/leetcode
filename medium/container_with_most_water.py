"""
Link: https://leetcode.com/problems/container-with-most-water/
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l_i = 0
        r_i = len(height) - 1

        max_area = 0
        while l_i < r_i:
            l_h = height[l_i]
            r_h = height[r_i]
            curr_area = min(l_h, r_h) * (r_i - l_i)
            max_area = max(max_area, curr_area)
            if r_h < l_h:
                r_i -= 1
            else:
                l_i += 1
        return max_area