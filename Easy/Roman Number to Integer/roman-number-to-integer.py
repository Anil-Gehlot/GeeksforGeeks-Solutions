#User function Template for python3

class Solution:
#USer function Template fclaSS Solution:
    def romanToDecimal(Self, S): 
        
        # dictionary to fetch the integer value
        values ={
            'I':1,
            'V':5,
            'X':10,
            'L':50, 
            'C':100,
            'D':500,
            'M':1000
        }

        # replacing the of roman like 4, 9, 40, 90, 400 and 900
        S = S.replace("IV", "IIII")
        S = S.replace("IX", "VIIII")
        S = S.replace("XL", "XXXX")
        S = S.replace("XC", "LXXXX")
        S = S.replace("CD", "CCCC")
        S = S.replace("CM", "DCCCC")

        # containS the integer value of Roman
        Sum = 0
        
        # traverSing the given roman numberS
        for letter in S:
            
            # adding letterS integer value to Sum
            Sum += values[letter]
        
        # returning Sum  
        return Sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends