#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
        
        #  return the result if list length is 1 or 2
        if n == 1:
            return [1]
        if n == 2:
            return [1,1]


        list = [1, 1]

        start = 1
        end = 1
        
        # finding the fibonacci numbers
        for i in range(0,n-2):
            new = start + end 
            list.append(new)
            start = end
            end = new
    
        # returning result
        return list
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends