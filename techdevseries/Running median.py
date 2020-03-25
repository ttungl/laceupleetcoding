# Running median

# Given a stream of numbers, compute the median for each new element.

# input = [2,1,4,7,2,0,5] 
# return output = [2, 1.5, 2, 3.0, 2, 2, 2]


class Solution:
	def __init__(self):
		self.res = []

	def _find_median(self, arr):
		ans = 0
		arr.sort()
		n = len(arr)
		if n==0:
			return
		if n==1:
			return arr[0]
		if n%2==0:
			ans = (arr[n//2 - 1] + arr[n//2])/2
		else:
			ans = arr[n//2]
		return ans 

	def running_median(self, stream):
		for i in range(1, len(stream)+1):
			ans = self._find_median(stream[:i])
			self.res.append(ans)
		return self.res

stream = [2,1,4,7,2,0,5]
runmed = Solution()
print(runmed.running_median(stream))
# [2, 1.5, 2, 3.0, 2, 2, 2]