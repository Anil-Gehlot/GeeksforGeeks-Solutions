#User function template for Python

class Solution:	
	def binarysearch(self, arr, n, k):
		# code here
		
		start = 0
		end = n-1
		
		
		
		while(start<=end):
		    
		    mid = (start+end)//2
		    
		    
		    if(k==arr[mid]):
		        return mid
		        
		    elif(k<arr[mid]):
		        end = mid-1
		        
		    elif(k>arr[mid]):
		        start=mid+1
		        
	    return -1
