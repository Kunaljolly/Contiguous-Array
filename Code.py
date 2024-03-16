class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_length = 0
        count_dict = {0: -1}  # Initialize count dictionary with count 0 at index -1
        
        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1
                
            if count in count_dict:  # If running count already exists in dictionary
                max_length = max(max_length, i - count_dict[count])
            else:
                count_dict[count] = i
        
        return max_length
