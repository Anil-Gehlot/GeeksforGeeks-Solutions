#User function Template for python3


class Solution:
    def missingNumber(self,array,n):
        # code here
        
        sum = 0 
        sum1 = 0
        
        for i in range(1, n+1):
            sum = sum + i
            
        for i in range(0, n-1):
            sum1 = sum1 + array[i]
            
        return sum-sum1
