# 1390. Four Divisors

# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.
# If there is no such integer in the array, return 0.

# Example 1:

# Input: nums = [21,4,7]
# Output: 32
# Explanation:
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The answer is the sum of divisors of 21 only.
 

# Constraints:

# 1 <= nums.length <= 10^4
# 1 <= nums[i] <= 10^5

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # sol 1:
        # time O(n*m*0.5) space O(n)
        ans = 0
        for num in nums:
            res = set()
            for i in range(1, floor(sqrt(num))+1):
                if num%i==0:
                    res.add(i) # divisor
                    res.add(num//i)  
                if len(res)>4:
                    break
            if len(res)==4:
                ans += sum(res)
        return ans
    
        # sol 2:
        # time O(n*m*0.5) space O(n)
        res = 0
        for num in nums:
        	ans = set()
        	for i in range(1, num+1):
        		if i*i > num: break
        		if num % i == 0:
        			ans.add(i)
        			ans.add(num//i)
        			if len(ans) > 4: break
        	if len(ans)==4:
        		res += sum(ans)
        return res

        
