import numpy

import numpy
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        square = {}
        # search restrict to square root of c
        root = numpy.sqrt(c)
        for i in range(0, int(root)+1):
            # store {c - i^2 : i} in dictionary
            i2 = i**2
            if square.get(i2) is None:
                if c-i2 != i2:
                    square[c-i2] = i
                else:
                    return True
            # i^2 in dictionary means i^2 + value(i^2) = c
            else:
                return True
        return False


if __name__ == '__main__':
    obj = Solution()
    obj.exhaustion()
    #ans = obj.judgeSquareSum(0)
    #print(ans)


