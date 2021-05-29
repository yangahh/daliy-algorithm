class Node:
    def __init__(self, value):
        self.val = value
        self.next = self.pre = None # next, pre는 Node의 instance (어떤 값이 아니라 Node 오브젝트 그 자체)
  

class MyLinkedList():

    def __init__(self):
        self.head = Node(None)
        self.size = 0

    # index번째 node의 value를 리턴    
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index > self.size:
            return 1
        elif index == 0:
            return self.head.val
        else:
            target = self.head
            for _ in range(index):
                target = target.next
            return target.val

    # 맨 앞에서 node 추가(=appendleft)
    def addAtHead(self, val):
        """
        :type val: int
        """
        if self.size == 0:
            self.head = Node(val)
        else:
            before_head = self.head
            self.head = Node(val)
            self.head.next = before_head
        self.size += 1

    # 맨 뒤에서 node 추가(=append)
    def addAtTail(self, val):
        """
        :type val: int
        """
        if self.size == 0:
            self.head = Node(val)
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            new_tail = Node(val)
            tail.next = new_tail
        self.size += 1

    # insert
    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        """
        if index == self.size:
            self.addAtTail(val=val)
        elif index == 0:
            self.addAtHead(val)
        elif index > self.size:
            return
        else:
            new_node = Node(val)

            pre_target = self.head
            for _ in range(index-1):
                pre_target = pre_target.next

            next_target = pre_target.next
            pre_target.next = new_node
            new_node.next = next_target

            self.size += 1

    # remove
    def deleteAtIndex(self, index):
        """
        :type index: int
        """
        if self.size == 0 or index > self.size:
            return
        elif self.size == 1:
            self.head = Node(None)
            self.size = 0
        elif index == 0:
            before_head = self.head
            self.head = before_head.next
            del(before_head)
            self.size -= 1
        else:
            pre_target = self.head
            for _ in range(index-1):
                pre_target = pre_target.next
            del_target = pre_target.next
            pre_target.next = del_target.next
            del(del_target)

            self.size -= 1
    
    def printAll(self):
        target = self.head
        while target:
            if target.next:
                print(target.val, '-> ', end='')
                target = target.next
            else:
                print(target.val)
                target = target.next
        print(f'size: {self.size}')


# linkedList = MyLinkedList()
# linkedList.addAtHead(1)
# linkedList.addAtTail(3)
# linkedList.addAtIndex(1, 2)
# linkedList.addAtIndex(1, 10)
# linkedList.addAtIndex(1, 20)
# linkedList.printAll()
# print()
# linkedList.deleteAtIndex(1)
# linkedList.printAll()
# print()
# linkedList.deleteAtIndex(2)
# linkedList.printAll()
# print()
