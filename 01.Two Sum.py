def twoSum(nums, target):
    
    myHashMap = {}
        
    for i in range(len(nums)):
        complement = target - nums[i]
        
        if complement in myHashMap:
            return [myHashMap[complement], i]
        else:
            myHashMap[nums[i]] = i


test = [1,4,6,8,10,23,5,0]
target = 18

print(twoSum(test, 9))