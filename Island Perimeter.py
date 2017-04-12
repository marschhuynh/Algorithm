class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x = [0, -1, 0, 1]
        y = [-1, 0, 1, 0]
        result = 0
        for i in range(len(grid)):
          for j in range(len(grid[0])):
            if grid[i][j] == 1:
              sum = 0
              for k in range(4):
                if (-1 < i + x[k] and i + x[k] < len(grid)) and (-1 < j + y[k] and j + y[k] < len(grid[0])):
                  if grid[i+x[k]][j+y[k]] == 0:
                    sum += 1
                else:
                  sum += 1
              result += sum
        return result

