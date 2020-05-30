class MyListNode:
    def __init__(self, val=None, next_node=None, prev_node=None):
        self.val = val
        self.next = next_node
        self.prev = prev_node

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def get_val(self):
        return self.val

    def __str__(self):

        if self.next:
            next_val = str(self.next.val)
        else:
            next_val = "None"

        if self.prev:
            prev_val = str(self.prev.val)
        else:
            prev_val = "None"

        return "[val: " + str(self.val) + " , next:" + next_val + " , prev:" + prev_val + "]"


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.head = None
        self.node_count = 0

    def get_node(self, index: int) -> MyListNode:
        index_cur = 0
        node = self.head

        if node:
            while True:
                # val = node.val
                if index_cur == index:
                    return node
                else:
                    if node.next:
                        node = node.next
                        index_cur += 1
                    else:
                        return None
        else:
            return None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self.get_node(index)
        if node:
            return node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head:
            temp_node = MyListNode(val, next_node=self.head, prev_node=None)
            self.head.prev = temp_node
            self.head = temp_node
            self.node_count += 1
        else:
            self.head = MyListNode(val)
            self.node_count += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        '''node = self.head

        if node:
            while True:
                if node.next:
                    node = node.next
                else:
                    node.next = MyListNode(val,next_node=None,prev_node=node)
                    break
        else:
            self.head = MyListNode(val)'''

        if self.node_count > 0:
            node = self.get_node(self.node_count - 1)
            #print("Last ")
            temp_node = MyListNode(val, next_node=None, prev_node=node)
            node.next = temp_node
            self.node_count += 1
        else:
            self.head = MyListNode(val)
            self.node_count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if 0 < index < self.node_count:
            prev_neighbor = self.get_node(index - 1)
            next_neighbor = prev_neighbor.next
            temp_node = MyListNode(val)
            prev_neighbor.next = temp_node
            temp_node.next = next_neighbor
            temp_node.prev = prev_neighbor
            next_neighbor.prev = temp_node
            self.node_count += 1
        elif index == 0:
            self.addAtHead(val)
            #self.node_count += 1
        elif index == self.node_count:
            self.addAtTail(val)
            #self.node_count += 1

    def deleteAtIndex(self, index: int) -> None:

        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        node = self.get_node(index)

        if node:
            #print("called inside node to delete is " + str(node) )
            prev_node = node.prev
            next_node = node.next

            if prev_node:
                prev_node.next = next_node
            else:
                self.head = next_node
            if next_node:
                next_node.prev = prev_node




            self.node_count -= 1

    def __str__(self):
        node = self.head
        val = "node_count: " + str(self.node_count)
        if node:
            while True:
                val = val + str(node)
                if node.next:
                    val = val + " , "
                    node = node.next
                else:
                    return val
                    break
        else:
            return "None"


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

linkedList = MyLinkedList()  # Initialize empty LinkedList
print(linkedList)
linkedList.addAtHead(1)
print(linkedList)
linkedList.addAtTail(3)
print(linkedList)
linkedList.addAtIndex(1, 2)  # // linked list becomes 1->2->3
print(linkedList)
linkedList.get(1)  # // returns 3
print(linkedList)
linkedList.deleteAtIndex(0)  # // now the linked list is 1->3
print(linkedList)
linkedList.get(0)  # // returns 3
print(linkedList)
