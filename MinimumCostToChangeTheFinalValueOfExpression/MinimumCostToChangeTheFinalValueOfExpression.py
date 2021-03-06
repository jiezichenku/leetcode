from DataStructure.BinaryTree import *

global leftExpression
global operator
global root
global i

# This solution does not pass the pressure test
class Solution:
    def generateTree(self, expression: str) -> BinaryTree:
        leftExpression = None
        operator = None
        root = None
        i = 0
        while i < len(expression):
            if expression[i] == "1":
                i += 1
                if operator is None:
                    leftExpression = BinaryTree("1")
                else:
                    operator.insertRight(BinaryTree("1"))
                    leftExpression = operator
                    operator = None
                if root is None:
                    root = leftExpression
            elif expression[i] == "0":
                i += 1
                if operator is None:
                    leftExpression = BinaryTree("0")
                else:
                    operator.insertRight(BinaryTree("0"))
                    leftExpression = operator
                    operator = None
                if root is None:
                    root = leftExpression
            elif expression[i] == "&":
                i += 1
                if operator is None:
                    operator = BinaryTree("&")
                    if leftExpression is None:
                        raise Exception("Invalid expression!", expression, i)
                    else:
                        operator.insertLeft(leftExpression)
                        if root == leftExpression:
                            root = operator
                        if root is None:
                            root = operator
                else:
                    raise Exception("Invalid expression!", expression, i)
            elif expression[i] == "|":
                i += 1
                if operator is None:
                    operator = BinaryTree("|")
                    if leftExpression is None:
                        raise Exception("Invalid expression!", expression, i)
                    else:
                        operator.insertLeft(leftExpression)
                        if root == leftExpression:
                            root = operator
                        if root is None:
                            root = operator
                else:
                    raise Exception("Invalid expression!", expression, i)
            elif expression[i] == "(":
                endBracket = self.searchBracket(expression[i: len(expression)])
                subTree = self.generateTree(expression[i + 1: i + endBracket])
                if root is None:
                    root = subTree
                i += endBracket
                if operator is None:
                    leftExpression = subTree
                else:
                    operator.insertRight(subTree)
                    leftExpression = operator
                    operator = None
            else:
                i += 1
        print(expression)
        print("root: ", root.getObj())
        return root

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

    def getValue(self, r: BinaryTree) -> bool:
        if r.getObj() == "0":
            return False
        if r.getObj() == "1":
            return True
        if r.getObj() == "&":
            lvalue = self.getValue(r.lchild)
            rvalue = self.getValue(r.rchild)
            return lvalue & rvalue
        if r.getObj() == "|":
            lvalue = self.getValue(r.lchild)
            rvalue = self.getValue(r.rchild)
            return lvalue | rvalue

    def updateCost(self, r: BinaryTree) -> int:
        if (r.getObj() == "0") | (r.getObj() == "1"):
            return 1
        if r.getObj() == "&":
            lcost = self.updateCost(r.lchild)
            rcost = self.updateCost(r.rchild)
            print(lcost, rcost)
            if (self.getValue(r.lchild) is False) & (self.getValue(r.rchild) is False):
                return min(lcost, rcost) + 1
            else:
                return 1
        if r.getObj() == "|":
            lcost = self.updateCost(r.lchild)
            rcost = self.updateCost(r.rchild)
            if (self.getValue(r.lchild) is True) & (self.getValue(r.rchild) is True):
                return min(lcost, rcost) + 1
            else:
                return 1

    def minOperationsToFlip(self, expression: str) -> int:
        # build up the expression tree
        r = self.generateTree(expression)
        r.printTree()
        return self.updateCost(r)


if __name__ == '__main__':
    obj = Solution()
    tree = obj.minOperationsToFlip("0|(0&0)|(0&0)|((1&0))&0|(0&(0&0)|(0&0))|0&1|((0&0)|(((0&0))&(0&0)&0&(0&0))|(0|0)|((0&0)|(0&0)|(0&0))|((0&0)|0&0&0)|(0&0)&1|0&(((0&0)&(0&0))))|(0&0)|0&1&0&1|1&0|0&((0&0))|1|(1|1|0)&0&(0&0)|(0&0)&0|0&1|1&(1|(0&0))|(0&0)&(0&0)&(0&0)&0|0|(0&0)|0|1|1&0|(0&1)|(0&0)|0|(0&0)|(0&0)|0&(((0&0)))|1&0|0&(((0&0)&1))&1&(0&0&(0&0)|((0))&((0&0))&((0&0))|(0)&0)&((0|1&1|(0&0))|0|((0&0)&(1|(1)&(0&0)&(1&(0)|1|(0&0))|1)&(0&0)|1&1|1&((((0&0))&(0&0)|(0&0))))|(((1&0&1)|(0&0))&(0&0)&(0&0)|(0&0))&(0&0))&(0&0)&(0&0)|0|1&0|(0)|1|((0&0)&(0&0)|0|(0&0)|(0&0)&0|(0&0)|0&1|0&((1&1|(0&0)&((0&0)|1&1)&0)))&(0&0)&1&(0&0)|1|(1)|(0&0)|1&0|1|0|0|(0&0)&((0&0)&1)|1|1&1|1&(0&0)&1|(1|((1&1&1|(0&0))|(0&0))|1)&1&0&0|(0)&0|0|(0)&((0&0))|(0)|0|1|(0&0)|(0&0)|(0&0)&(0&0)|(0&0)|1|1|(0&0)|(0&0)|(0&0)|0&(1&(0&0))&((0&0))|(0&0)|(0&0)|(0&0)&(0&0)|1&0|0|(0&0)|0&0|0|1&1&(0&0)|((1)|((0&0)|0|(0&0))|1&((((0&0))&0)|0)&(0&0)&0|(0&0)&0)&(0&0)|1&1|(0&0)|(0&0)|0&0|0&(0&0)&0|1&0&((0&0)|1&(1&0&0))|1|1&(((0&0)&1&1)|1|(1)|(0)&(0&0))|(1|0&1&(0|((0&0)&(0&0))|1&1|1|(0&0)&1&(0&0)|0)&(((0&0)|1|(0&0))&1|(0&0)))|1&0&1|(0&0)&1|0&1|1|1|(0&0)|0|0|1|0|0|(1)&0&0&(0&0)&1&1|1&(1)&(1)|(((0|1|((0&0)|(0&0)&0|1)|1))&((0&0)|((0&0)|1&((0&0)&((0)&0&((0&1|0|((1|(0&0))|1|(0&0))&0|0)))|(0&0)&(1|1&1|(0&0)|(0&1&(1&0)&((1|1))|(0&0)&(0&0))|((1&1&1)&0|(0&0)&1&0|0|1)&(0&0)|0|0&(0&0))))|(0&0)&(((0&0)&1|(0&0)&(0&0)&(0&0))))&(0&0))&1&1&0&(1|0)|(0&0)|(0&0)|(1&(0&0)|0)&(0&0)|1&(((0&0)&(1))|0&((0)|(0&0)))|1|0&1|1|(0&0)&(0&0)&0&1&(0&0)|0|0|(1)|1|(0&0)|0|(1)|0&1|1|(0&0)&0|(0&(0&0)|(((1|(0&0)&(0&1&1&1|0)&1&((0|1))|(1)|1|(0&0)&(((0&0))&0|1|(0&0)|(0&0))&0&(1)|(0&0))&0&0|1|1)&((0&0)&(0&0))|(0)|0)|(0&0))&(0&0)|((0&(0|1|1&(0&0))&1&((0&0)))&(((1&((1&(((((0&0)&((((1|1|0)|(0&0)|(0|(0)|(1&0)&0|0|(0&0)))|(0))|(0&0)&0)|1)&1&1))|0&(0&0)&(0&0))&(0))&0&0&1|(0&0)|1)|((0&0))|0)&0|(((0&0)&1)&1)&0&(1&(((0))&1|(0&0)&1))&(1&1&1|(0)|(0|0)|1&(0|(0|0&(0&0)&(0&0)|0)|0)&(0&1|((0&0)&1|(0&0)))))|1|(1&((0&0)|(0|0&0)&(0&0)&0&((0&0))|1&1&0&1)|1|(0&0)|1&(1)&1|(0))|1&(0&0)&0&(0&0))&0&1&(0|(0&0)))|(0&0)&1&(0|((0&0)&(0|0&(0&0))&((0&0)|1&(0&0))))&1&(((0&0)&(0&0)|((0&0)|0|1&1|(0))&(0&0)))|0&(0&0)|1&(0&0)&((((0&0)&(0&0)|1|1&1&1|((0&0)|(1|((0&0)&(0&0)&(0&0)|(0|(0&0)|(0&0)&1|((1|0))&(0&0)|(0&0)|0))|1|1))&(0&0))))|0|0|0|(0&0)|(1|0|0&0&(0&0)&0|((0&(0&0))&(((0&0))))&0|(0&0))&0|(0&1&(0&0)|1)|(0&0)&((0&0)&0&1&(0&0)&(0&0))&1&0&(0&0)|(0&0)&(0&0)&1&0|(0&0)&0&0|0&(0&0)&0|(0&0)&(0&0)&(1&0)&((1&(0&0)|(0&0)|1)&(0&0))|(0&0)|0|((0&(0&0)&((1))))&1&1&0|1&1|1|1&1&1&(0&0|1|0)|(0&0)&(0&0)&0|1&1&(0&0)&0&(((0))|((0&0)))&(0&0)&(0&0)|1&(((0|0|1|((0&0))&1|((0&0)|0&(0&0)&0&((1&(0&0|1&0))|0|1)&1)&1|1|(0&0)|(0&0)|1)|1&(0|1))&(0&0)&0&0|((1|(0&0))|((0&0))|(0&0))&1&(((0&0)&1|0|0|1|(0&0)&0|(0&(0&0))|(((((0&0)))|1&0&(0|0&(0&0))|((0&0)&(0&0)|(0&0)|(0&0)&(((0&0)&(((0&0)|1|(0&0)|1|(0&0)))))&(0&0)&((0&0)&(0&0)|1&(0|(0&0)&(0&0)|1))|0)|1&(0&(1)|(0&0)))|0&(0&0)&(((0&0)&((1|(0|(0&0)&(((0&0)&(((0&0)&((1|(0&0)|(0&0)))&0&(((((((0))&(0&0)|0)|0)&1)&(0&0)|1)&0|0|1&0))))|(0&0)&((0&0)|(0&0)&(0&0))|(1)&1&(0&0)))&(0&0)&(1|1))&0&0&0)|1|(1&(0&0)&1)&((((0&0)&0)|(1))|1))&0&1&(0&0))|0)|1|0)|1|((0&0))|0|0)&0)&((1|0&1&(0&0)))&0|1&1|0&0|1|(0&0)&(0&0)|(1&1)&1|1&0&(1&(0&0))|((0&0))|0|1&(0&0)|(0&0)|1|0|0&(0&0)|1|((0&0)&1&1&(0&0))|(0&0)|((0&0)|1|0|((0|(0&(0&0)&0&(0&0))|0|0|(0&0))))&((0|0&0&(((0&0)&1)|(1|1)))&(((0)|(1)|((0&0)))|(1&(0&0)|0|((0&0)|1)))|1)&0&1|1|(0&0)|((0)|1|0&(0&0)&0&((0&0))|(0&0)|(1)&(((1))&((0&0)|1|0))&(0&0))&0|1|0&1|(0&0)&1|(0&0)|(((0&0)|(1&((0&0)&(0)&1|(1)&(0)&(0&0)))&(0&0)&0|1)&0)|0&0|1|(0&0)|(0&0)|(((0&0)|(0&0)|(0&0)|(0)|(0&(1|(0&0))|1&0&0&1|0)&1|(0&0)|(0&0)&1&1&((0&0)|1|0)|1&(0&0)&(0&0|(0&0)&(0&0)&0)))&((0&1)|0&0)|1&0|(((0)|(0&0)&1|0)&(0&0))|0&1&(0&0)|(0&0)&1|0&(0&0)&1&(0&0)&0&(0&0)&0|(1)|(0&0)|0&(0)|(0&(0&0)&(((1)&((0&0)|0&0))|1)|0)&(0|1|((0)))&1&((0&0)|0&(0&0))&0|1|0|1|1&1&0&(0&((0|0|1&(0)|1&0)|1&(0&0)&1)&((0&0)&0&(0&0)))|1|1|(1|1&0&((1))&(0&0))|0|0&(1|0)&0&1&(0&0)&(0&0)|(0&0)|(0&(0)|0)&(0&(1)&1)&(0&0)|1|((1&1&(1)&((0&0)&(0&0)|(1)&(0&0)|(0&0)&((0&0)&0|(0&0)|0&0))|0|(0&0))&0|1|1)|(0&0)&0&(((0&0))&(0&0)|(1&1|(0&0))&((((1&(0&0))|(0&0))&1|0)|0|(0&0)&(0&0)|(0&0))|0&1)|(0|(0|0|1)&0)|0&(0&0)&0&(0&0)|(0&0)|1&(0&0)|(((0|(0&0)&(0&0))|(0&0)&(0&0)))|(0&0)|(1|(0|(0&0)))|(0|(0&0)&(0&0)|(0&0))|((0&0)|0&1&0&0|0|0|((0|(0&0)&(0&0)|1)|(0&0))&1)|1|0&0|(((0&0)|(0&0)|((0)&0|0)&(1)|1&0|(0&0)&(0&0)|0|0|(0&0)&(1)|((0&0)&1&0&0)|(0&0))&1)|0|1|(0&0)|(((0&1|0&0)|1|1&1&(0&0)))&1&(0&0)|(0&0&(0&0)&0|0|(0&0))&1|(1)|((0&0))&0|0&1&0|0&0|((((((1&1)|(0))|1)|(0&0)&0&0&(0&(0&0)|0)&(((0&0))&1&(1))))|(0&0)&1|(0&0)|1)&0|1|((0&0)|((1)))&(1|(0&1|1&0&0|1&(0&0)&(0&0)))&0&(((((0&0)&(0&0)|0))|(1&(0|0|0&(0&0)|1))|(0&0))&(0&0)&0)|(1)&(0&0)&1&0|(0&0)&(((0)|1)&1)&1|1&0|0|1|((0&0)&((0&0)&0)&(0&0)&1|1&((0|1)&(0&0)&1|(0&0)&(0))|0&(0&0)&0)&1&1&(1|(0&0))&(0&0)&0|(0&0)&0|(0|1|(1))&1|(((0&0)|0|1))&(0&0)&(1&(1&(0&0))|0)|(0&0)&(1&1|(0&0))&(0&0)&(0|1&(0&0)&((0)&1))&(0&0)&(1&1)&((0|(1))|1|1&0)&0|((0&0)|0&0)&(0&0)&((0&0))|(0&0)|(0&0)|0|1&(0&0)|(0&0&(0&0)&(0&0))&1|0|0|1&((0&0)|(0)|(0&0))|(0&0)&1&(0&0)|0|(1|(0&0)&0|0|(0&(0))&(1)|(0&0))&(0&0)|(0&0)&1|1|1|(0&0)&(0&1)|(0&0)|(0&0)|0|0|(0&0)|(0&0)|(0|1&(0&0)|(1&(0&0)&((0&0)|1&0|0)&0)|(0&0))&0&(0|(0&0)|(0&0)|0&((1|0|0))|1&(0&0)|0)&(0&0)|((0&0))|1&1&(0)|1|1&(0&0)&((0&(0&0)|(((0&0)))&((0&0)))&(0&0)|1)&1&(0&0)|(0&0)|0|1&0|0|0&0&1|0&1&0|1&((1&(0&0)|(1&(0&0))|((0&0)&0)&(0)&((1|(0&0)&(0&0)|((0&0)&1|(0&0)&(0)&(1&1)&((0&0)|(0&0)))&1|0&1|1|((0&0)|(0&0)|(0&0)|(0&0)|(0&0))&(0&0|0|1&((0&0)&(0&0)|1&((((1)|1|(1)|(((0&0)&(1)|1&0)))|(0&0))&1|((((0&0)|1|1|0|(0&0)&((((((0&0)&(((0&0)))|0|(0|1&0)&((0&0)&1&(1)&(0&0)&(0&0))|1|(1)))))&1&(0)&((0&0)&(0)|(0&0)|(0&0)))|0&(0)|(0&1)|(1&0|0&((0&0)))|(0&0)|(0)|(1&0)|(1)&0&(0&0)&1|(1)&1&1&(1)))|((0)|1|0|((0&0)&(((0&0)|1|0))&0|1)|(0&0))|(1|(0&0)|(1)|0|(0&0)&1|(0))|0))|0)&1)&1)|0&1&(0))&1))|(((0&0)|(0&0)&(((((0&0)|((1)|0&1|(0&0)&1&0|(0&0)&(0&0)))|1))&(0&0)|0)|(0|(0&0))|0)|(0&0)&1)&((0&0)&(0&0)&(0&0))&((0&0)|1|0|(0&0))|((0&0)&(0&0)&1)&(1)|((0&0))|(0|(0&0)|(0&0))|1|1&(0&0)&0|0&0|0|0&0&(0&0)&(0&0)|1&0|(((((1&1&(0&0))&((0&0)|1&1&(0&0)&0&1)))|0&(0&0)|1|0&(0&0))|0|(0&0)&(0&0)|(0&0)&(0|(((0&0)|1&0&(0&0)&(0&0))&1|(0&0)|(0&0))&(1)|(1|0)|(0&0))&(0&0)|((0&0)))&0&1|(0&0)&1&(((((1|1&0)&1&0)&(((1&(1)&(0&1|((0&0))&(0&0)|0&(0&0))|1&(0))|(0&0)|1|(0&0)|0))|((0&1&1|0|((0|(0&0))&0)))|0&0&1|1)|(0&0)&(0&0))|(1)|1&0)&(0&0)&0&0|(0&0)&0|(((0&0)&(1)|1&(0&0))|((((1))&((0&0)|(0&0)&(0&0))&(1|0|(0&0)))|(1|0)))&(((1&(0&0))&1))&1&0|0|(0&0)|0&(0&0)&1|((0&0)&0)|0&((0|0|1&((0&0)&((0&0))|(1)&((0&0))&(1|1|((0&0)&(1&((0|((0|1|0&1))&(1&(0&0)&0|1)|1|0))&(0&0)|(0&0)|1)&1)&1|1)&((0&0))&(0&0)&(0&0)|(0&0)|(0&0))|0)&((0&0)|(0&0)&1))|1|(0&0)&0&1&0|(0)&0&(0&0)|1|(0|1&(0&0)|1&(0&0)|0)|0&1|1&(0&0)&(1|1)&1&(0&0)&1&1&(0&0)&1&0&1&1|1&(0)|(0&0)&1&1|((0&0))&(1&0&1&(0&0))&(0&0)|0|0|1&0&0|0|(0&0)|(0&0)|(0&0)|1&0|(0&0)|0|((0&0)&((1))|(0)|(0&0)&(0&0))&1|(0&0)&(0&0)|((0&0))&(0&0)&(0&0)|(0&0)&1&1&1|1&(((0&1|0&1&(0|(0&0)|1&(0&0)|(((0&0))&0&0&1|0))&1)|(0&0))&(0&1|(0&0)))|((0&(0&0)|1&0|((0&0)&0)&1|0))&((0&0))&(0&0)|1|((0&0)&0|0&(((0&0)&0)&((0&0)|(0&0)&(0&0)&1))|(0&0)&1&(0&0)|(0&0)&1|((0&0)|(0&0)|0&0&(0&0)|1|1&1))|0&(0&0)|(0&0)|(0&0)|(1|(1&(0&0))|0|1)|(1|1)&(0&0)|(0&0)|0|(0&0)&(0&0)|((0&0)|(0&0)|0|0)|0|(0)|1&0&(0&0)&(0&0)|(0)|1&1|(0&0)|0&1&1&(0&0)&(0&0)&1|1|1&(0&0)|1|(0&0)|1&(0&0)|(0&0)|1&(0&0)|0&1|0|0|1|0|(((0&0)&1&0&(0&0)))|(0&0)&0|(1&1|(0))&1|1|(0&0)&1&((0&0)|(0&0))|(0&0)&(0&0)|1&0&1|(0&0)&(0&0)&(0&0)|0&1|(1&(0)&(0&0)&1|(0&0)|(((0&(0&0))|(1&((0&0)|0&(0)))|(0|1))))&0|1&(0&0)&(0&0)&1&1&1|(0&0)&(0&0)&(0&0)&0&0&1|1&1&(0&0)&(0&0)&1|1&(0&0)&(0&0)|1&((0&0)&1)&((1)|(0&0)|((1)|1&0|0|1|((1|1&0|1|(0&0))))|(0&0)&(0&0))&(0&((0&0)|1&(1)|1&(0|(0&0)|1)|0)&0&0|((1&(1)|1|0&1)|(0&0))|(1)&1|1&0|1&1|(0&0)&(0))&(0&0)|1&1|(0&0)|(0&0)&0|1&1&(0&0)|(1&(0&0)&0)&0|(((0&0)&(0&0)&(0&0)&(0&0)|(0&0))&1)&(0&0)&(0|0)&1&(1|0|(0&0))&0&1|0|0|1&((0|1)|(0&0))&1|(0&0)&(1)|(0)|0|1&(1&(0&0)&1&0|0|(0&0))&1&0|((0&0)&0&0)|(0&0)&1&((0&0))&0|0|(0&0)&(0&0)&1|(0&0)&(((0&0))|0)|((0&0)&((0&0))&0|0|0)|1|0|((0&0)&1&0)&(1)&((((1|0|0)&(0|((0&0)&(0&0))&1)|1)&1&1|(0&0)&(1|1&(1|(0&0)|0&(0&0))&0&(1&1)|0&0)&1))&1|(0&0)&(0)&(0&0)&1|1|((0&0))&0&(0&0)|(0&0)&(0&0)|((1&(0&0)&((0&0))|(((0&0)&(1&1)))|(((0&0)|0|((0&0)&(0&0)&(0&0))|1))|0)&(0&0)|(0&0))&(0&((0&0)&1|0)|(0)|0|0&(0&0))|1|(0&0)&0&(((0&0))&0)&0&0|(0&0)&(0&0)|0|0|(1|1)|0&(0&(0&0))&(0)|(0&0)&0|(0&0)|0&1&(((1)))|(0&0)|1|0&0&(0&0)|(0&0)&1&((0))|0|0|((0&0)&0)|1|(0|0&(0&0)|(0&0)&(1|(1|0|1)&(1|(0&(0&0)&((0&(0&0)&(0&0)&(1&1|0)|((0&0)&(0&0)&1|(1)|1&1&0))))&1)|1|((1)|((0&0)|((0&0))&(0&(1)&(0&0)|1&(0&(0&0))|0|((0&0))|1&(0&1)&1)&(0&1)|0)|1&(0&0)&(0&0)&(0&0)|(0&0))|1&1&1)|(0&0)|0)|1&0&1&(0&0)&0&(((0&0)))|1&1&(1&(0|(0&0)|1&((1|1))&(0&0)&(0&(1|(0)|1&(0|1|0|((0&0))))|(0&0)|(0&0)&1)&(1|1&(0|((0|(0&0)|(1)|(1)&(0&0)&1)|(0&0))&((1|0&(0&(0&0)|(0&0))&1)|0|(0&0)&((0&0)|((0&0)&0&1)))|0|1)|(0&0))|(0&0)|(0&0))|1|(1|(0&(0&0))&(0&0)|(0|1|0))|0|0|1&((0&0))&1)&(0&0)|1&((0&0))&1|((0)|(1|(0&0)&0|1|1)&0&(1&0|1&(0)&(0&0)|(0)|1&1&1&(0&0)&(0&0)&1|0|0|0)|((0&0|(0&0)|(0&0)|1|1)|1|1))|0&(0&0)|1&(((0&0)|(0&0)|0|(0&0)&((1)))&1|(((0&0)&(0&0))))|(0&0|((0&0)|(0&0))|((((0&0))|0&(0&0)&0|(1)|0&0&1|(0&0)|0|(0&0)&0&(0&0)|1|0|1)))|(0&0)|(0&0)&(0&0)|1&1|0|(0&0)&0|(0&0)|1|1|0&1&1&1|1|(1&(0&0)|(((1&(0))&0|0|(1|1))&0|1&(((1|1|1&(0&0)|0)))|(0&0)&(0&0))&(0&0)|1|0)|1&(0)&0|1&1|1|((0&0)&0)&1|0&0&(0&0)&((0&1))&((0&0)|1|0&((0&0))&(0&0)|((0|0&(0&0)&1|(0&0)|(0&0)))&1&0)|(1)|(0&0)&(1&0)|0|1|1&(0&0)|1|1&(0&0)|1&(1)&0|(0&0)|1&0&(0&0)&(((0&0)&1&(((1|1)&(0&0)&0&0))|1))&(1)|(0&0)|0|1&(0&0)&1&(0&0)&((0&0)&1&(1|((0&0))|(1&0)&0|((1&(0)|1)&(0&0)&1&(1)|((((0&0)|((0|0)&0&0|(0&0)|0))|((0&(0&0)&1|(0&0)&(0&0)|0|(0&0)&(1)&0)&1)))&(0&0)))|1|0)|((0&0)&(0&0)|1|(1|1))&1|1|1|0&0|1&(((1&(0&0)|((0)&0&1)&(0|(0&0))))&0|((0&0))|(0&0))&1&1&((0&0)|0|(0&0)|(0&0))|(0&0)|(0|((0&0)))|1&1|(((0|(((0&0)|(0|(0&0)|(((0&0)|1|(0&0)|0))&1&0&0)&1&(1))&1&1|0)|(0&0)&(1)&(((0))&(1|0)|1&(0&(0&0)&0&(1&0&1&(0&0)|((0&0)&1|(0&0)|(0&0)|1)&1&(0&0)|(0&0)|(1))|(0&0)|(0&0))&0&0|1|(0&0)|((1))|1|(0&0)|(0&0)&0|(0&0)|((0&0)&0|((0&0)))|0)&(((1&0&0&0&1|(0&0)&0))))|1)|(0&0)&0)|(0&0)&(1)|(0&0)|1|0|0&(0&0)|1&0&0&(1&1&(0&0))&0&1|(0&0)&(0&0)&0&0&(1&1)&0|(1&(0&0))|0|(0&0)&(0|0&1|0&(1)&1|(0&0))&1&(1|1|((1|0|1)&1|0&1)|1|(0&0)&1|1)&((0&0))|(0&0)|((0&0)|(0&0)|0)&1&1&(0&0)|0|(1&1&(0&0)&1&0&(0&0)&(0&0)|0)&1|(((1&(0&0)&(((1&0&(1&(0&0)&0&1&0&(0)|(1))|(0&0))))))&(0&0)|(0&0)&(((1))|1&(0&0))&((0&0)|(0&((0&0))|(0&0)|0)&(0&0)&0|1&1)&0&(0&0))|(0&0)|0&(0&0)|((0&(0&0))&0&((((0&0))|1&(0&0))|(0&0))&(0&0)|0)&0|(0)|0&1|0|0&0&1|0&0&1&1|(0&0)&((0&0)&(0&0))&(0&0)|(0&0)&0|(0&0)&(0&0)|0|(((0&0)&0&0&(1&(0|1))|(0&0)|0)&0)&1&(1|(0)|0)&(1&(0&0)&(0&0)|(0&0)&1&(0&0))&(0&0)&(1&0&0)&(0&0)|(1&1|0|0)|0&(0&0)|1|(0&0)&1&1|1&(0&0)&((0&0)|(0&0)|0)|0&1|1&(1&(0&0)|((0&0)|1))&(0&0)&(1|1)&(0&0)|1|0|0|(1)&(1&(((0&0))&(0&0))|(0&0)&(((0&0)&0|((1))|(0))|1)&((((0&0))|1&1|(0|(0&0)|(0&0)|(1))))&(0&0))&1|1|(1|1|(0&0)|((0&0)))&0&(1&(0&0)|(1&1&((((0&0))|(1))))&(0&0)|((0&0)&(((0&0&(0&0))&(0&0)|((0&0))|(0&0)|((((0&0)&(0&0)|(0&0)&0|1|0)&0&0&((0&0)&1|1|(0&0))|1))&1&0|1))&(((0&0)|(0&0))&1&1)&1&(0&0))&1)|1&0&0&1|0|0|0|0&1|(1)&(((0&0))|(((0&0))|(0&0)|0))|(1)|0&0|1&0|1&(0)|(0&0)|(0|((0&0))|(0&0)|(((0&0)|(1)|1|1|0&0|1)&1|0))|0|(0&0)&(0&0)&(0&0)|((((0&0)|(0&0)|(((0&0))|1&(1|0)|1|(0&((0&0))|(0&0))))))&(0&0)&0|(0&0)|(0&0)|1&((((0&0)))|1)|(0&0)|(0&1|0&0&0&1)&((0&0)|(0&0)|1)|1|((0&0)&(0&0)&(1)|(0&(0&0)|0&0)&(0&0)&((1)&((0|((1))|(0&0)&1)|(1&0|(0&0)|(1|(1&(0&0)|0|0)|1)|1)|(0&0))|0&1&1|1))&1&(0)&(0)&1&(0&0)|1|0|(0&0)|0|((0&0)|1&(1|0&0|(0&0)&(0&0)))|1&((0&0))|(0|0)|(0&0)|(0&0)&0&((0&0))|(0&0)&1|0&(0&0)|((0|1&0))|1|0&1|(0&0)&(0&0)&0|(0&0)&(1)&0&((1)&((0&0)|(0|0|(0&0)|((0&0)|(0&0))|0&1|0)|1)|(0&0)|(0&0)|0|1&(1)&(0&0)|(1))|(0&0)&0&0&0&0|(0&0)|(0&0)|(0&0)|(0&0)&0|0|(0&0)&1&(0)&(0&0)|1&0|0|(0&0)|0&(0&0)&((0&(0)|(((0&0)&((0&0))&1|(((0&0)|0|(0))&0)&0)|(0&0)|((1&1&1|(0&0))&1&(0&0)|1&((0&0)))|(0&(0&0)&(0&1&0|(0&0)&1&1|(0&0)|1|1|(1|(0&0))|0)&((0&0))&(0&0)&((1)|(0&0))|0)))&(0&0)&(0&0)|(0&0)|0|((0&0)))&(0&0)&(1)&1&(1|1)|1&(0&0)|1&0&0&0|1&(((((1)&(0)&(0&0)|((1|(0&0)&0&(0&0)&1&(0&0))))|0|1&(0&0)))&(0&0))|(0&0)|(0&0)|(0&0)|1|1|0|0&((((0&0))&1|((0&0)&1)))&1|0&1&((0&0))|1&(1|0&0)&(0&0)|((0&0)|1)&0|(0&0|0&1|(0&0)|0)|0|(((0))&0&((0&0)&(0)))&(0&0)&(0)&1&0|(0&0)&(0&0)&0|0&0&0|0&(0&0)|1|1&0|(0&0)|(0|(0)|0)&(0|1&1|0&(0&0)|0)&((0&0))|0|0&0&(1)|1&(0|(0&0))|0|((0&0))|(0)|1&(1)&1&1&((((0&1|1&0&((0&0))&(0&0)&((0)|0))))&((((0&(((((0&0)|(0&0)|1)&(0&0))&(0&0)|(0)&(1&0)|(1&0&1|0|(0)&0|(1|(0&0))|0|(0&0))|(0&0)|1|((1&(0&0))|1&(1)&1|1)&((0&0)|0&1)))&1))|0|0|1|1&0)))&1|(0&0)&0|0|1|(0|1|(0&0)|0|(0&0)&0)|(0&0)&0&0&0&(1|(0&0))|(0&0)&((0&0)|(0&0)|((0&0))|0)&(0&0)|0|0|(0&0)|1&(0&0)|(0&0)|((1|0)|0)|(1|0&0|0|(0&0)|(((0))|(0&0)|(1)|(1&1|(0&0)&0|(0&0))&1))|(1&(0&0)|1)|1&(0&0|((0&0)|1&(1&(0)&1&((0&0))&(0&0)))|(0&0))|1&0|0&0&(0&0)&1|(0)|0|0|0|1|(0&0)&0|1|1&(1)|1&0&(0&0)&1&((((0&0))|((0&0)|(0&0)|0|1|1|1|(0&0)&0&(0|0&1&(0&0)&1&(0&0))|1&(0)))|((1|1))&(0))&(0&0)|1|(0&0)&(0&1|((0&1&((1)|1&0&((0&0)|(0&0)&((0&0)&((0)&0&1&((0&0))&0&1)|(0|(0|0&0|0|((0&0)&((0&0)&(0&0)&(0&0)|1&(0&0)|0&1&(0&0)&0|(0&0)|(0&0)))&0)))|0&1|0&1|((0|0&((0&0))|(0&0)&1)|1)))|1&((0&0)|0|0))|(0&0)|(0|((0&0))&0&0|(1|(((0&0)))|(1&1|0)|0)|(0&0)&0))|0&0&1)&1|(0&1)&1&0&0&1&1|(0&0)|(0&0)|(0&0)|0|(0)&(0&0)&(1)|(0&0)&0&(0&0)&(0&0)|0|1&(1|((0&0)&(0&0)&1&(0)))|1&(0&0)&(0&(0&0)|(0&0)&(0&0))&(0&0)|(0&0)&1&1&((1)|1)&0&1&((0&0)&(1)|(0))&1&(1&0|(0&0)&(0&0))|(0&0)|0&(0&0)|(0&0)|1|((0&0))&(0&(((1)&(0&0)&(0&0))&0&1)&0)&1|(1&0)&(0)|((0&0))&(0&0)&(0|0)&0|((0|0&0|1)|(1&(0&0))&(0&0))|(0&0)|0|0|(0&0)|(((0&(1)&0)&(0&0))|(0|0&0&0&(0&0)&(0&0)|1|((0&0))&(0&0)))|(((0&0)&1)|(0)|1)|(0|1)|(0&0)|1|0&(1&((0|1|(0&0)&1&0&0|1|1)&(1)))&0&(1&(0&0)|(0&0)&1|(((1)|0)&(0)|0&(0&0))&(0&0))&1&1|(0&0)|(0&0)|0|(0&0)|1|(0&0)|(0&0)|((0&0))|1&(1)|1&0|(0&0)|(0)&1&(0&0)&0|(0&0)&1&(1&(0&0)&0)|(0&0)|0&0|((((0)&((0&0))))&1)&((0&0))|((((0&0)&0)|(0)|(0&0)&(0&0)|1|(0|1&1))&1)|0&(1&(0&0)|1&(0&0))&0&((0&0)|1|0)|0|(0&0)|(0|(0&0))|(0&0&1|0&(1&1&0)|0|((0&0)|0|(0|(0&0)|1)|1|((0&0)))&((0&1&(0&0)|(0&((0&0)|(0)&((0&0)&1|1&(((0&0)|((0&0)&((0&0)&0&0)&0&((0&0)&(0&0)|0)|1&0))|1|0|((0&0)|((1))&1)&0))&(1)|0&(0&0&(0&0)|(0&0)&((0&0)))|0)&((0|(1|1&0&0&(0&0))|1|0&(0&0)|1)|(0&0)))&(1&(0&0))|0|(0&0))))|(0&0)|(0)|0&1&0|((0|(0&0)|(1&0&1)&(0&0)|1|0&(0&0)|1)&1)&0&(0&0)&0&0|0|1|(0&0)&1|0&((0&0)&(0&0)&(1|0))&(0&0)&0&(0&0)&0|0&1|(0&0)|(0&0)&(0&0)|1|1|((1)|0)|0&1|(0&0)&(0&0)|(0&0)|0&(((0&0)|(1&1&0&(0&0)&1&1)&1&1))&0&(0&0)&0&0&0&(0&0)|1&(1&(0&0)&0&0&0)&(0&0)&1|1&1|1&1|1&0&0&(0&0)|(0&0)|0&(0&0)&(0&0)|((0&0)|0)&1|0&((0&1&1)&1)|0|(1&1&1&(0&0)|0|(0&0))&1&1&1&(0&0)&0|((1&0&(0|(0|1))&(((0&0)|(0&0)|(1&0)|0|0&((0|(0)|0|1)&0)))|1))&(0)&(0&0)|1|0&(0&0)&0&0&1|(1)|1|1|0|1|0|0&((1&0)|0|1)&(0&0)|0&((0&0)|1&((0&0)|0&(1|1)|(0&0)))&0&(0&(0&0)&0&1|1|0|0&0|0|1|(0&0)|(1|0))&1|0|((0&0))|0&0&1|1&(0&0)|0&(0&0)&1|0&(0&0)|(0&0)|1|(0&0)|1&1&((1)&0)|1&1|0|0&0&(0&0)&0|0&(0|0|(1)&(0&0))&(0&0)&((0&0))|1|1&1&(0&0)&0&(0&0)&1&(0&0)&(0&0)|1|(0&0)&1|(0|((0&0)&1&(0&0)|1)&(0&0)&1|1&0&(0)&(0&0))|(0&0)&(0&0)&1&(0|(0&0))&(((0&0))&(0&0)|1)|(0&0)&0&(1)|(0&0)|((0&0)&1|(0|1&((((1|(1)|(0&0))))|1&(0&0)&1)&0&1|0|0|1&1|1)|(0&0)&0|1&(0&0))|((0&0)|(0&0)|(1|(1)|(0)&0))&(((0&0))|0|0&1|(0&0)|0)|1&(0&0)|0|((1)&(0&0)|(0&0)|1|0|1)|(0&0)&0|1|(0&0)|0&(0&0)&1|(0&0)|(0&0)&(0&0)|(0&0)&((0&(0&0)&(0&0)))|1|(0&0)|1|1|1&(0&0)|(0)&((0&0)&(((1|1&(0&0)&0|0)&(0&0)|0&0|(0&0)|1&(0&0)&1)|0|1&0)|1|((1|(1|((0&0)&1))|1)&1&(1|((0&0)&(0&0))&(0&0)|0)|1&0)|1&(1&(0&0)|(0&0))&(0&0)|0)|1|1|((0&0)|1)&0|(0&0)&0|(0&0)&1&0|1&(0&0)&(((0|(((1)&(1|((((0&0)|1|(0&0)|0|(0&0)|((((0&0))|1|((0&0)&0|(0&0))|((0&0))&(0&0)|(0&0)&1)|1&(0|(0&0)|0&((0&0)&1|(1|1&(((0&0))&(0)|(0&0))&(1|(0&0)|0&(0&0)&(0&0)))|1&(0&0)&(0&0)))|(0&0)))|(0&0))&0))|0&0&0|(0))))|(0&((0|1&(0&0)|((0&1|(((1|(0)|1))&(0&0)&(0&0)|1|1)&(0&0)&(0)|(0&0))|(((0&0)&((1&(0&0)|(0&0)&((0&(0|(0&0|(0&0)&0&1&1|(0&0))&(0))&(0&0)|(0&0))&0)|0&(0&(0&0)|(0&0))|(0&0))&(1|(0&0)|(0&0))))|1))&((0&0)&1|(0&0)&1|0|0|(1&1&((0&0)))&0&(0&0))|((0&0)|(0&0)|0&1|(0&0)&(((0&0)|(0&0)&0|1)&1&((0&0)&1))&1|((0&0)&0|0|(1|1)|1&(0&0)&(((0&0)|(((((0&0))|(0&0)&1))|0|1&(0)))|(0&0)&(0&0)&1)|0&(0&0)&(0&0)&(((0&0))|1&0&1|0|(0)|1|1))|(0&0))|1&1&1|(0&0)|(0&0))|(0&0))|0)&1)&1|0|1|0&0&1)&(0&0)|(0&0)&1&1&(0&0)&0|(((0&0)))&(0&0)&(0&0)|1&(0)&0|1|(0&0&(0&0)|(0&0))|(0&0)&(0&0)&0|(0&0)&(0&0)|0&0|(((0&0)&1&(0&0)|(0&0))|(0&0))&(0&0)&(0&0)|(1)|1&1&1&0|(0&0)|1|1&1&(0&0)&1&1|((0&0)|0&0|((0&0))&1)|0&0|(0&0)&(0|0)|(0&0)&(0&0)|((0&0))|1&(0&0)|(0&0)&(0&0)&(0)&(0&(((0&0)|(0&0)|(0&0))&1&(0&0)&0)|0)&0&1&(0&0)&1|1|(0&0)|(1&1|(0&0)&1|(0&0))&(((0&0)|1))&(0&0)&(((0&0)|1|((0&0)&0&((0&1|1&0)|(0&0))&(0&0)|(0&0))&(0&0)|(0&0))&1)|0|0&(0&0)|((0&0)|(0&0)|0|(0&0)|(0&0)&1)&((1&((0&0))|((0&0)&(0&0)|1&1|(0&0)&(0&0)|(0&0)&((0&0)|0|(0|1&((0&0)&1&(0&0)|0&0&(0&0)&(0&0))|(1)&1&1)|1&1))|1|(1)&(0&0))&0)|(0&0)|1|0|0|1|((((0&0)|0&1)&0)|1)|0&1&(1)&(0&0)|1|(0&0)&(0|0)|1&0|1|(0&0)&0&1&0|1|(1&(0|0&((((1|0&0)&0&((1&1))|1)&(1&(0)&1)))&(0&0)&(0&0)))&1|(1&0)|0&((1)|(((0|((1|((0&0))|((0&0)|0)))&(0&0)))|0)&(0&((0&0)|1&1&1&(((0)&1|((0&0)))|(0&0)|1|1&(1)&1)&((0&0))|1|(0&0)&(0|(0|1&(0&0)|(0&1|(0&0)|((0|1|(0&0)|1&(0&0)&(0&0)|0)))|(1|1|(0&0)&0)|(0&0)|1&0)&(0&0)|(0&0))|(0&0)&0|1&1&1|0|((0&0)&1|1&0)|(0&0)&0|1|0))|((1&((((1&1)|0|(0)&(0&0)|0|1&0)&((1&(0&0)&0|1)&((0&0)&((0))|0)|1|1&((0&0))|0)&(0&0))|1)|(1&(0)|(0&0)|1|0))))|0|0|(1|0|(0&0)|((1|1|((0&0)&(0&0)&0|(0)|(1&0|((0|0|0|1))&0))|((0|0|(0&0)&(0&(0&0))&1&(0))|(1)&(1|0&1&((1|1)|1))&(0&0)))|1|0))&0|(0&0)|1&1&1&((0&0))&1|(0&0)&1|(((0&0)|((0&0)|(0&0)&1|1&((0)&(1|0)|1)&(0&0))&(((1&((0&0)|1|((0&0)&((0&0)|1&((0&0)&(0&0)&(0&((0&0)|0|((0&0)&(0&0)|((0&0))|((0&0)|((0&0)|(0&0))))|1)&0|(1)&((1)|1)))|1)&(0&0)|1|1&((0&(0|((0&0)|(1|1&0&0)&(0&(0&0)&0&1)|(0&0)&1&((0&0&(1|(0&0)))&0|0)|0))|0&(0&0)&0&(0)|1)|(((0&0))|1|0|(1&0|1|(0&0))|(0&0))&(0&0))&0))&(0&0)&1&1)&1|(0&0))|1)&1)&(0&0))&(0&0)&(0&0)&1&1|1&(0&0)|0|((0&0)|1|((1&0|(1&((0&0)&0|0)|0|(0&0)))&((1)|(0&0)&((1|1|1)))&0|(0&0)&(((0)|1|0|0|(1&((0&0))&1|(0&0)&(0&0))|0))|(0&0)))|0&0|0&1|(0&(0&0)&1&1)|(1)&1&1|(0&(0&0)|1)&1&(0&0)|1|(0&0)&0&0&((0&0))&1&(1|(0&0)&((0)|(1)|0)&0|(0&0))|(0|1)|(0&0)&1&(0&0)&((0&0)&(0&0))&(0&(((0))&0|0|1&(0&0)&(0&0)|(0&0))|1)&0&1|1&0&0|(0&(0&0))&1&0|1&1|1&(((0&0)|(0&0))|0&0|(0&0)&(0&0))|0&1|0&(1&1)&0&(1&(0))&1|(0&0)&(0)&(0&0)&(0&0)&(0&0)|(0&0)|1&1|((0&0))&((0&0))&(0&0)&0|(0&0)|0&((0&0))|1&0|(1|0)|(0&0)|((0)&0|(0&0))&1&(0&0)&(0&0)|((((0&0))|1)&((0&0)&0|1&((0&0)|1&0&((0&0)&((0&0))&0|1&(0&0))|1)|(0&0)&(0&0)))&(0&0)|1|1|0&(0&0)|((0&0)|(0&0)&(0&0)&1|0)|0|1&1|0&(0&0)&(0&0)&(0|1|0&0)|(0&0)&1&(0&0)|0|(0&0)&0&((0&0))|(0|1|(0&0)&0&0)|1&(0&0)&(0&0)|0&1|((((0&0))&0))&((1&0|1|0|1|1|1|(0&0)|(0&0)|1)|((0&0))&(0&0))|(0&0)|(0&0)&0&(0&0)|(0&0)|(0&0)|((0&0))|1|((0|(0&((0&0)|(0&0)&((0&0)&0|((0&0))|1&0|0|1|0)|1&(1)&(0&0))&1)|1|(1))|0)&(0&0)|0|0&1|(((0&0)|0))|0|(0&(((((0&0))|(0&0)|1|(1|0)&(0&0)&1)|(0&0)&(0&0)))&0&0|(1|1|(0|(0|((0&0))&0|1|0)))&1|1)&1|0&((0|(1)|1|0|(0&0)&1)|(1|(0&0)&1&1)|1)&(0&0)&1&1|(0)&(0&0)&(0&0)|1|0|1|0|(0&0)&1|0&0|(0&0)|1|(0&0)&((((0&0)|1&0&(0&0)))&(0&0))&1|0&(0&0|(0&0))|(0&0)|((0&0)&0|1)|0|0&(0&0)|0|((1|(0&0)|(0&0))&1|1&1)&((0&(0&0)&(1))&1)|1&((((0&0)|((0)&(0&0)&0&0|(1|(1|((0&0)&1|0))&(0)&1|(0&0)|1|1))&(0&0)|((0&0))))|0)|0|(0&0)&0|(0|1)&(0&0)&(0&0)&1|0&(((0&0))|1|(0&0)&1)|1|0&(0&0)|(0&0)|0&0|0&0|(0&0)&((1&0)|1)&0&0&(0&0)&1|((((0&0)|(0&0)&(0&0)&0))|(0&0)&(0&0))|1|(0&0)&(0&0)&(1|(0&0)|0|(((0&0)&((0&0)|1&((0&0)|(0&0)|(0&0)|0&(1&(((0&0)|1)&0&((0&0)&1&(0&0)|0)&1|((0&1|1)|1|1|(0&0)&0))|0)&0&(0&0)|(((0&0)|0|0))&((((0&0))&(1)|(0&0)&(0&0)&(0|0))))&((0&0)|(0&0)|(0&0)&0|(1)))|1))&(0&0))&(0&0)&0&((((1))&(0|1)&(0&0)|1)&0)&1&1|((0&0))&(0)|(0&0)|((0&0)|(0&0))|((0&0)|(1|1)|1|0)&(0&0)&(0&0)|0|(0&0)|(0&0)&1|(0&0)&0&1|1|1&1|1&((1|(0&0)&1))|0&1&0|(((((0&0)&(0&0)&(0&0)&(0|0|1)&(((0&0))|1|1|(0&0))))&(0&1|(0&0))&1&((0&0))&(0&0)|((0&0))))|1|1|0|(0&0)|1&(1)|((0&0))&1&(0&0)|(0&0)&(0&0)|(0&0)|(1)|(0&0)|1|(0&0)|0&0|1&(0&0)|0&1|((0&0)|(0&0))&(0&0)|0&(0&0)|1&(0&0)&(((0&0)|(1&1|0&0&(((1|1))))|0))&(0&0)&(0&0)&(0&0&(1|1|((0&0))))&(0&0)|(0&0)|(((1&0)&(1|0)|(0&0)&(0&0)&(1))&((0&0)|(0)|(0&0)))|0|(0&0)&1|1&(0&0)&1&0&(0&0)|0&(1&(0)|1|(0&0))&((0&0)|((0&0)|((0&0)|(0&1&(1|(0&0)))))&(0&0)|(0&0))&0&(0&0)|1|1&1|1|(0&0)|0|0&(0&0)&1&(1|1&0|0&0|((0&0))&((0|(1)|0&0&0)))|(0&0)|((0|(0&0)&(((0&0)|1|((1)|1|1&0&0&1|0&(0))))|(0&0)|1))&(1|0)&(0&0)&0|1|(1&(0))|(((0&0)&1&((0&0)&1&1|(0&0)|(1)|1)))|1|(0&0)|1|1|0|0&1|1&1|1&(((0&0)|1&1))")
    print(tree)
