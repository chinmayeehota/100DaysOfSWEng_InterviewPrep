class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #left array
        l_arr = []
        prev = 1
        for i in nums:
            l_arr.append(prev)
            prev *= i  
        #right array
        r_arr = []
        prev = 1
        for j in nums[::-1]:
            r_arr.append(prev)
            prev *= j
        return [a * b for a, b in zip(l_arr, r_arr[::-1])]