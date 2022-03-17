# Time complexity: O(n)
# Space complexity: O(1) -> constant

class Solution:
    def romanToInt(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        
        # Declare the meaning of Roman number
        d = {"I":1, "V":5, "X":10,"L":50, "C":100, "D":500, "M":1000}
        solution = 0
        
        for i in range(0, len(s)-1,1):
            # If element < next element -> IV -> [1][5] -> solution = -1 -> solution = -1+5 = -4
            if d[s[i]] < d[s[i+1]]:
                solution -= d[s[i]]
            else:
                solution += d[s[i]]
                
        solution += d[s[-1]]
        return solution