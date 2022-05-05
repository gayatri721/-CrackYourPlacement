'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left_ptr = 0 # Left pointer initialize to left most index
        right_ptr = n - 1 # Right pointer initialize to right most index
        
        # Formula to calculate resultant water for particular selection of left and right pointer is
        # Water contained = minimum of left and right height multiplied by difference between right and left
        result = min(height[left_ptr],height[right_ptr]) * (right_ptr - left_ptr)
        
        while left_ptr <= right_ptr:
            # Move left pointer when left is smaller then right
            if height[left_ptr] < height[right_ptr]: 
                left_ptr += 1
            else:
                right_ptr -= 1
            result = max(result, min(height[left_ptr], height[right_ptr]) * (right_ptr - left_ptr))
            
        return result
