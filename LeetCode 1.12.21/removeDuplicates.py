#Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #brute force solution
        #iterate through each element and check if the previous 
        #matches and remove duplicates
        x = 1
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return 1
        else:
            while x <= len(nums)-1:
                if nums[x-1] == nums[x]:
                    nums.remove(nums[x])
                else:
                    x += 1
               
        return len(nums)
               