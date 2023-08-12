class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        
        total = 0
        
        # To find the total sum of given array
        for i in A:
            total = total + i
            
        left_sum = 0
        # right_sum = 0
        
        for i in range(0, len(A)):
            right_sum = total - left_sum - A[i]
            
            if (left_sum == right_sum):
                return i+1
            else:
                left_sum = left_sum + A[i]
        
        return -1

