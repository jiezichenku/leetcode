import numpy

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        for i in range(size):
            print("i=", i)
            for j in range(i + 1, size):
                print(i, j)
                if nums[i] + nums[j] == target:
                    return [i, j]
        return[]

    def test(self):
        examples = {9: [2, 7, 11, 15], 6: [3, 2, 4], 0: [-3, 4, 3, 90]}
        for example in examples:
            ans = self.twoSum(examples[example], example)
            print(ans)


if __name__ == '__main__':
    obj = Solution()
    obj.test()
