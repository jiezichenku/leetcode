class Solution:
    def getComplex(self, num: str) -> list:
        comp = num.split("+")
        real = int(comp[0])
        if len(comp) == 2:
            tmp = comp[1].split("i")
            imaginary = int(tmp[0])
        else:
            imaginary = 0
        return [real, imaginary]

    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        complex1 = self.getComplex(num1)
        complex2 = self.getComplex(num2)
        # real equals real1 * real2 - imaginary1 * imaginary2
        resultReal = complex1[0] * complex2[0] - complex1[1] * complex2[1]
        # imaginary equals real1 * imaginary2 + real2 * imaginary1
        resultImaginary = complex1[0] * complex2[1] + complex1[1] * complex2[0]
        ret = ""+str(resultReal)+"+"+str(resultImaginary)+"i"
        return ret


if __name__ == '__main__':
    obj = Solution()
    num1 = "1+-1i"
    num2 = "1+-1i"
    ans = obj.complexNumberMultiply(num1, num2)
    print(ans)
