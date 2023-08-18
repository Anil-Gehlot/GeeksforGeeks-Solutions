class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
     #Function to find the leaders in the array.
    def leaders(self, A, n):
        leaders = []  # To store the leader elements
        max_right = A[n - 1]  # Initialize the maximum value from the right

         # The rightmost element is always a leader
        leaders.append(max_right)

        # Traverse the array from right to left
        for i in range(n - 2, -1, -1):
            if A[i] >= max_right:
                max_right = A[i]
                leaders.append(max_right)

        # Reverse the list to maintain the order of appearance
        leaders.reverse()
    
        return leaders


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends