'''
Using HashMap

Approach
- Tranverse the array
- Create a hashmap mapping diff of target and curr no. with curr idx
- Check if new no matches the difference stored as key in hashmap
- If matches, return current idx and mapped value of difference 
- Else keep adding values to dictionary

Complexity Analysis
- Time - 0(n)
- Space - O(n)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        for idx in range(len(nums)):
            if nums[idx] not in di:
                req = target - nums[idx]
                di[req] = idx
            else:
                return [di[nums[idx]], idx]
        #incase no such pair exists return []
        return []