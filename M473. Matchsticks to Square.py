# I failed to solve this and used a submission from JINLIU0 and swing100 to code this. I was also introduced to @cache here and was pretty good to know that such thing like this exists!
# Since I did not solve by myself, I'm using more comments here to remember what is happening in each piece of code (trying to study!)

from functools import cache

class Solution:

    def makesquare(self, matchsticks) -> bool:

        num = len(matchsticks)
        side = sum(matchsticks) / 4

        # the sum of matchsticks should divisible by 4 (4 equal sides)
        if sum(matchsticks) % 4 != 0:
            return False
        

        matchsticks.sort(reverse = True)

        # Sorting descending and if the first matchstick is greater than the needed side for the square, return False 
        if matchsticks[0] > side:
            return False
        
        # @cache stores the function calls results and whenever the function is called with the same parameters it returns the result right away instead calculating everything again
        # Note: to use caching properly you cannot have any mutable data structure like Lists.  
        @cache
        def dfs(self, side1, side2, side3, side4, index) -> bool:

            # if I finished looking every matchstick, check if every side is equal 
            if index == num:
                return side1 == side2 == side3 == side4
            # if one of the sides was greater than the needed side
            if side < side1 or side < side2 or side < side3  or side < side4:
                return False 

            # this make a huge difference when using caches. Need some investigation. 
            sortingSides = [side1, side2, side3, side4] 
            sortingSides.sort()
            side1, side2, side3, side4 = sortingSides

            #backtracking. we add the index to every side
            return dfs(self, side1 + matchsticks[index], side2, side3, side4, index + 1) or dfs(self, side1, side2 + matchsticks[index], side3, side4, index + 1) or dfs(self, side1, side2, side3 + matchsticks[index], side4, index + 1) or dfs(self, side1, side2, side3, side4 + matchsticks[index], index + 1)
              
        return dfs(self, 0, 0, 0, 0 ,0)


tests = [[1,1,1,1,1,1,1,1,1,1,1,1], [2,2,4,4,4], [1,4,4,3,3], [5,5,5,5,4,4,4,4,3,3,3,3]]

for test in tests:
  
    print(Solution.makesquare(None, test))