class Solution:
    def containsDuplicate(self, nums) -> bool:
        
        hashMap = {nums[0]: True}
        
        for i in range(1, len(nums)):
            
            if nums[i] in hashMap:
                return True
            else:
                hashMap[nums[i]] = True
                
        return False

print(Solution.containsDuplicate(None, [1]))
        
        
        
        