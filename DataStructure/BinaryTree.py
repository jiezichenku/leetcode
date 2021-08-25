class BinaryTree:
    def __init__(self, obj):
        self.obj = obj
        self.lchild = None
        self.rchild = None

    def insertLeft(self, lchild):
        if self.lchild is None:
            self.lchild = lchild
        else:
            self.lchild.setObj(lchild.getObj)

    def insertRight(self, rchild):
        if self.rchild is None:
            self.rchild = rchild
        else:
            self.rchild.setObj(rchild.getObj)

    def getLeft(self):
        return self.lchild

    def getRight(self):
        return self.rchild

    def getObj(self):
        return self.obj

    def setObj(self, obj):
        self.obj = obj

    def preorderTraversal(self, order):
        order.append(self.getObj())
        if self.lchild is not None:
            self.lchild.preorderTraversal(order)
        if self.rchild is not None:
            self.rchild.preorderTraversal(order)

    def inorderTraversal(self, order):
        if self.lchild is not None:
            self.lchild.inorderTraversal(order)
        order.append(self.getObj())
        if self.rchild is not None:
            self.rchild.inorderTraversal(order)

    def postorderTraversal(self, order):
        if self.lchild is not None:
            self.lchild.postorderTraversal(order)
        if self.rchild is not None:
            self.rchild.postorderTraversal(order)
        order.append(self.getObj())

    def printTree(self):
        inorder = []
        self.inorderTraversal(inorder)
        print("Inorder:")
        print(inorder)
        preorder = []
        self.preorderTraversal(preorder)
        print("Preorder:")
        print(preorder)
