from functools import cache

class Solution:

    def makesquare(self, matchsticks) -> bool:

        num = len(matchsticks)
        side = sum(matchsticks) / 4

        if sum(matchsticks) % 4 != 0:
            return False
        
        matchsticks.sort(reverse = True)

        if matchsticks[0] > side:
            return False
        
        @cache
        def dfs(self, side1, side2, side3, side4, index) -> bool:

            if side1 == side2 == side3 == side4 == side:
                return True
            if index > len(matchsticks) - 1:
                return False
            if side < side1 or side < side2 or side < side3  or side < side4:
                return False 

            sortingSides = [side1, side2, side3, side4] 
            sortingSides.sort()
            side1, side2, side3, side4 = sortingSides

            return dfs(self, side1 + matchsticks[index], side2, side3, side4, index + 1) or dfs(self, side1, side2 + matchsticks[index], side3, side4, index + 1) or dfs(self, side1, side2, side3 + matchsticks[index], side4, index + 1) or dfs(self, side1, side2, side3, side4 + matchsticks[index], index + 1)
              
        return dfs(self, 0, 0, 0, 0 ,0)


tests = [[1,1,1,1,1,1,1,1,1,1,1,1], [2,2,4,4,4], [1,4,4,3,3], [5,5,5,5,4,4,4,4,3,3,3,3]]

for test in tests:
  
    print(Solution.makesquare(None, test))