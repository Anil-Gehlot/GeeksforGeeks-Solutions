import math

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        sum = 0
        # To assign -infinite to a variable 
        max_sum = -math.inf
        
        for i in arr:
            sum = sum+i
            max_sum = max(sum , max_sum)
            
            if (sum<0):
                sum = 0
        return max_sum


