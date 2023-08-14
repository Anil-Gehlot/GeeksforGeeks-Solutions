#User function Template for python3

class Solution:
	def singleNumber(self, nums):
		# Code here
		
		list1 = []
		dict1 = {}
		for i in nums:
		  #  if nums.count(i) < 2:
		  #      list1.append(i)
		  if i in dict1:
		      dict1[i] += 1
		  else :
		      dict1[i] = 1
		      
	   
	    for i in dict1:
	        if dict1[i]==1:
	            list1.append(i)
        list1.sort()
        return list1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends