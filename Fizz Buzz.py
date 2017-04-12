class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = range(1, n+1)
        for i in result:
          if not i % 3 and not i % 5:
            result[i-1] = "FizzBuzz"
          elif not i % 3:
            result[i-1] = "Fizz"
          elif not i % 5:
            result[i-1] = "Buzz"
          else:
            result[i-1] = str(i)
        return result
