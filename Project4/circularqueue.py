"""
Project 4 - Circular Queues
Name:
"""
from collections import defaultdict


class CircularQueue:
    """
    Circular Queue Class.
    """

    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0

    def __eq__(self, other):
        """
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False

        if self.head != other.head or self.tail != other.tail:
            return False

        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False

        return True

    def __str__(self):
        """
        String representation of the queue
        :return: the queue as a string
        """
        if self.is_empty():
            return "Empty queue"

        str_list = [str(self.data[(self.head + i) % self.capacity]) for i in range(self.size)]
        return "Queue: " + ", ".join(str_list)

    # -----------MODIFY BELOW--------------

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def head_element(self):
        if self.is_empty():
            return None
        return self.data[self.head]

    def tail_element(self):
        if self.is_empty():
            return None
        return self.data[self.tail-1]

    def grow(self):
        if self.size == self.capacity:
            result = CircularQueue(self.capacity)
            result.data = [None] * self.capacity
            result.head = 0
            self.capacity *= 2
            for i in range(self.size):
                result.data[i] = self.data[i]
            self.data = [None] * self.capacity
            temp_loc = self.head
            for a in range(self.size):
                self.data[a] = result.data[temp_loc]
                temp_loc = (1 + temp_loc) % result.capacity
            self.head = 0
            self.tail = self.size


    def shrink(self):
        if self.capacity // 2 >= 4 and self.size * 4 <= self.capacity:
            temp = self.data
            self.capacity = self.capacity // 2
            self.data = [None] * self.capacity
            temp_loc = self.head
            for a in range(self.size):
                self.data[a] = temp[temp_loc]
                temp_loc = (1 + temp_loc) % len(temp)
            self.head = 0
            self.tail = self.size


    def enqueue(self, val):
        self.data[self.tail] = val
        self.tail += 1
        self.size += 1
        if self.tail > self.capacity - 1:
            self.tail = 0
        self.grow()
        return None


    def dequeue(self):
        if self.is_empty():
            return None
        result = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        self.shrink()
        return result


class QStack:
    """
    Stack class, implemented with underlying Circular Queue
    """
    # DO NOT MODIFY THESE METHODS
    def __init__(self):
        self.cq = CircularQueue()
        self.size = 0

    def __eq__(self, other):
        """
        Defines equality for two QStacks
        :return: true if two stacks are equal, false otherwise
        """
        if self.size != other.size:
            return False

        if self.cq != other.cq:
            return False

        return True

    def __str__(self):
        """
        String representation of the QStack
        :return: the stack as a string
        """
        if self.size == 0:
            return "Empty stack"

        str_list = [str(self.cq.data[(self.cq.head + i) % self.cq.capacity]) for i in range(self.size)]
        return "Stack: " + ", ".join(str_list)

    # -----------MODIFY BELOW--------------
    def push(self, val):
        self.cq.enqueue(val)

        for i in range(self.size):
            temp = self.cq.dequeue()
            self.cq.enqueue(temp)
        self.size += 1
        return None

    def pop(self):
        if self.size == 0:
            return None
        result = self.cq.dequeue()
        self.size -= 1
        return result

    def top(self):
        if self.size == 0:
            return None
        result = self.pop()
        self.push(result)
        return result


def digit_swap(nums, replacements):
    return yes
