class Solution:
    def fizzBuzz(n):
         """
        :type n: int
        :rtype: List[str]
        """
         ans = []
        
         n = int(n)
        
         for num in range(1, n+1):
            if num % 3 == 0 and num % 5 == 0:
                ans.append("FizzBuzz")
            elif num % 3 == 0:
                ans.append("Fizz")
            elif num % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(num))
                
         return ans

ret = Solution.fizzBuzz(100)


    

