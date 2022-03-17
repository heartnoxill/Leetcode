# Time complexity: O(n^2)
# Space complexity: O(1) -> constant space

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Initialize variables
        st = ''
        i = 0
        
        while True:
            # If loop more than number of characters of first element
            if i >= len(strs[0]):
                return st
            
            # Check the i character of first element
            curr_char = strs[0][i]
            
            # Loop in the second element and so on
            for s in strs[1:]:
                if i>=len(s) or s[i]!=curr_char:
                    return st
            
            # If not returned on both conditions, add that character to the st.
            st+=curr_char
            i+=1