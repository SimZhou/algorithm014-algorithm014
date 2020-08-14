# https://leetcode-cn.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.queue = []
        self.k = k
        self.size = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.size < self.k:
            self.queue = [value] + self.queue
            self.size += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.size < self.k:
            self.queue.append(value)
            self.size += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.size:
            return False
        else:
            self.queue.__delitem__(0)
            self.size -= 1
            return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.size:
            return False
        else:
            self.queue.__delitem__(-1)
            self.size -= 1
            return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self.size:
            return -1
        else:
            # self.size -= 1
            return self.queue[0]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self.size:
            return -1
        else:
            # self.size -= 1
            return self.queue[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if not self.size: return True
        else: return False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if self.size == self.k: return True
        else: return False        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()