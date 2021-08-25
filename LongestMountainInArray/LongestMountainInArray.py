class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        if len(arr) < 3:
            return 0
        maxMountain = 0
        recentMountain = 0
        ascending = 0
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                ascending = 0
                recentMountain = 0
            elif arr[i] < arr[i-1]:
                if recentMountain > 0:
                    recentMountain += 1
                elif ascending > 0:
                    recentMountain = ascending + 1
                    ascending = 0
                if recentMountain > maxMountain:
                    maxMountain = recentMountain
            elif arr[i] > arr[i-1]:
                recentMountain = 0
                if ascending == 0:
                    ascending = 2
                else:
                    ascending += 1
        return maxMountain


if __name__ == '__main__':
    obj = Solution()
    ans = obj.longestMountain([9,8,7,6,5,4,3,2,1,0])
    print(ans)
