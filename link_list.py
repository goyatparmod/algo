# class Node: 
  
#     # Constructor to initialize the node object 
#     def __init__(self, data, next=None): 
#         self.data = data 
#         self.next = next

# class link_list:
#     def __init__(self):
#         self.head = None
      
#     def push(self, data):
#         new_node = Node(data,self.head) 
#         self.head = new_node

#     def reverse(self): 
#         prev = None
#         current = self.head 
#         while (current is not None):
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next
#         self.head = prev

         

#     def printList(self):
#         temp = self.head
#         lstr = ''
#         while(temp):
#             lstr += '->' + str(temp.data )
#             print(temp.data)
#             temp = temp.next
#         print(lstr)


class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data, next=None): 
        self.data = data 
        self.next = next

class link_list:
    def __init__(self):
        self.head = None

    def push(self,data):
        newNode = Node(data,self.head)
        self.head = newNode

    
    def printList(self):
        temp = self.head
        lstr = ''
        while(temp):
            lstr += '->' + str(temp.data )
            print(temp.data)
            temp = temp.next
        print(lstr)    


       
llist = link_list() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(85) 
  
 
llist.printList() 
# llist.reverse()
# llist.printList() 
# 1.next
# 1.head
# 2.next
# 2.head

# ->85->15->4->20
# Head         Next   

