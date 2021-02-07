class Solution:
	def magicIndex(self, arr):
		for i in range(len(arr)):
			if arr[i] == i:
				return i
		return -1

s = Solution()
output = s.magicIndex([-1, 1, 2, 3])
print(output)