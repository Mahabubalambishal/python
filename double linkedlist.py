class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Doublelinklist:
    def __init__(self):
        self.head=None
    def add_item(self,newdata):
        newnode=Node(newdata)
        newnode.next=self.head
        while self.head is not None:
            self.head.prev=newnode
        self.head=newnode
    def __print_list(node):
        while node is not None:
            print(node.data)
            last=node
            node=node.next
linkedlist=Doublelinklist()
linkedlist.add_item(1000)
linkedlist.add_item(2000)
linkedlist.add_item(3000)
print_list(linkedlist.head)