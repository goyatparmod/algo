class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left = Node(data)  
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def minValue(self,node): 
        current = node 
    
        # loop down to find the leftmost leaf 
        while(current is not None): 
            if current.left is None: 
                break
            current = current.left 
        
        return current

    def inOrderSuccessor(self,n,p=None):  

        if self.data:
            if self.data == n:
                if self.right is not None:
                    a= self.minValue(self.right)

            # p = n.parent 
            # while( p is not None): 
            #     if n != p.right : 
            #         break 
            #     n = p  
            #  p = p.parent 
            # return a.data

    


    def __str__(self):
        print('data',str(self.data),'left', str(self.left),'right',str(self.right))

    def PrintTree(self):
        # print(self)
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
self = Node(12)
self.insert(6)
self.insert(10)
self.insert(14)
self.insert(3)
self.insert(22)
self.insert(20)
self.insert(7)
self.insert(17)

self.PrintTree()

print('Sucessor is ',self.inOrderSuccessor(3))





