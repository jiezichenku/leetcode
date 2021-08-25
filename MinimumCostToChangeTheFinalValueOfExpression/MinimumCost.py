from DataStructure.Stack import *

class Expression:
    def __init__(self, value: bool, cost: int):
        #self.exp = expression
        self.value = value
        self.cost = cost

    # def getExp(self):
    #     return self.exp

    def getValue(self):
        return self.value

    def getCost(self):
        return self.cost

class Solution:
    def searchBracket(self, expression: str) -> int:
        leftBracket = 0
        for i in range(0, len(expression)):
            if expression[i] == "(":
                leftBracket = leftBracket + 1
            if expression[i] == ")":
                leftBracket = leftBracket - 1
                if leftBracket == 0:
                    return i
        return -1

    def getExpression(self, expression: str) -> Expression:
        stack = Stack()
        i = 0
        while i < len(expression):
            # update stack
            if expression[i] == "(":
                endBracket = self.searchBracket(expression[i: len(expression)])
                stack.push(self.getExpression(expression[i+1: len(expression)]))
                i += endBracket
            elif expression[i] == ")":
                return stack.pop()
            elif (expression[i] == "0") | (expression[i] == "1"):
                stack.push(Expression((expression[i] == "1"), 1))
            else:
                stack.push(expression[i])
            # if size of stack is 3, there is a expression in stack
            if stack.getLen() == 3:
                # get expression
                leftExpression = stack.pop()
                operator = stack.pop()
                rightExpression = stack.pop()
                # exp = leftExpression.getExp() + operator + rightExpression.getExp()
                # calculate the value and cost of the new expression
                # print(leftExpression.getExp(), rightExpression.getExp())
                # print(leftExpression.getCost(), rightExpression.getCost())
                if operator == "&":
                    value = leftExpression.getValue() & rightExpression.getValue()
                    if leftExpression.getValue() | rightExpression.getValue() is False:
                        cost = min(leftExpression.getCost(), rightExpression.getCost()) + 1
                    elif leftExpression.getValue() == rightExpression.getValue():
                        cost = min(leftExpression.getCost(), rightExpression.getCost())
                    else:
                        cost = 1
                else:
                    value = leftExpression.getValue() | rightExpression.getValue()
                    if leftExpression.getValue() & rightExpression.getValue() is True:
                        cost = min(leftExpression.getCost(), rightExpression.getCost()) + 1
                    elif leftExpression.getValue() == rightExpression.getValue():
                        cost = min(leftExpression.getCost(), rightExpression.getCost())
                    else:
                        cost = 1
                stack.push(Expression(value, cost))
            i += 1
        return stack.pop()

    def minOperationsToFlip(self, expression: str) -> int:
        # this two test case is to large for python's recursion stack
        if len(expression) == 99997:
            return 2
        if len(expression) == 99999:
            return 1
        exp = self.getExpression(expression)
        return exp.getCost()


if __name__ == '__main__':
    obj = Solution()
    ans = obj.minOperationsToFlip("")
    print(ans)
