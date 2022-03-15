# Using Hash Map method
# Analysis
"""
Time Complexity: O(n) -> In worst case, we have to go through every element
Space Complexity: O(n) -> In worst case, we have to store all values in the hash map
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Create dictionary
        seen = {}
        
        # Enumerate loop through input list, iterate through each element
        for i, value in enumerate(nums):
            
            # Check if required number is present
            remaining = target - nums[i]
            
            # if found the remaining (that is already in seen)
            # return two index of that numbers
            if remaining in seen:
                return [i, seen[remaining]]
            
            # Add value as hash map key, i as value
            seen[value] = i