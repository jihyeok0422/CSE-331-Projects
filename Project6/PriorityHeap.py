"""
PROJECT 6 - Priority Queues and Heaps
Name:
"""


class Node:
    """
    This class represents a node object with k (key) and v (value)
    Node definition should not be changed in any way
    """

    def __init__(self, k, v):
        """
        Initializes node
        :param k: key to be stored in the node
        :param v: value to be stored in the node
        """
        self.key = k
        self.value = v

    def __lt__(self, other):
        """
        Less than comparator
        :param other: second node to be compared to
        :return: True if the node is less than other, False otherwise
        """
        return self.key < other.key or (self.key == other.key and self.value < other.value)

    def __gt__(self, other):
        """
        Greater than comparator
        :param other: second node to be compared to
        :return: True if the node is greater than other, False otherwise
        """
        return self.key > other.key or (self.key == other.key and self.value > other.value)

    def __eq__(self, other):
        """
        Equality comparator
        :param other: second node to be compared to
        :return: True if the nodes are equal, False otherwise
        """
        return self.key == other.key and self.value == other.value

    def __str__(self):
        """
        Converts node to a string
        :return: string representation of node
        """
        return '({0},{1})'.format(self.key, self.value)

    __repr__ = __str__


class PriorityHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """

    def __init__(self, is_min=True):
        """
        Initializes the priority heap
        """
        self._data = []
        self.min = is_min

    def __str__(self):
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self._data)

    def __len__(self):
        """
        Length override function
        :return: Length of the data inside the heap
        """
        return len(self._data)

    __repr__ = __str__

#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Modify below this line

    def empty(self):
        """
        :return: whether the heap is empty or not
        """
        if self.__len__() == 0:
            return True
        return False

    def top(self):
        """
        :return: the first Node in the heap
        """
        if self.empty():
            return None
        return self._data[0].value

    def push(self, key, val):
        """
        :param key: key of the Node an user want to push
        :param val: value of the Node an user want to push
        :return: None
        """
        new_node = Node(key, val)
        self._data.append(new_node)
        self.percolate_up(self.__len__()-1)

    def pop(self):
        """
        :return: pop the first Node and return that
        """
        if self.empty():
            return None

        self._data[0], self._data[self.__len__() - 1] = self._data[self.__len__() - 1], self._data[0]
        result = self._data.pop()
        self.percolate_down(0)
        return result

    def min_child(self, index):
        """
        :param index: index of the Node to check
        :return: smaller child
        """
        left = 2 * index + 1
        right = 2 * index + 2
        if left >= self.__len__():
            return None
        elif right >= self.__len__():
            return left
        elif self._data[left] < self._data[right]:
            return left
        else:
            return right

    def max_child(self, index):
        """
        :param index: index of the Node to check
        :return: bigger child
        """
        left = 2 * index + 1
        right = 2 * index + 2
        if left >= self.__len__():
            return None
        elif right >= self.__len__():
            return left
        elif self._data[left] > self._data[right]:
            return left
        else:
            return right

    def percolate_up(self, index):
        """
        :param index: index of the Node to move up
        :return:none
        """
        if index <= 0 or index >= self.__len__():
            return

        parent = (index - 1) // 2
        if self.min:
            if self._data[index] < self._data[parent]:
                self._data[index], self._data[parent] = self._data[parent], self._data[index]
                self.percolate_up(parent)

        else:
            if self._data[index] > self._data[parent]:
                self._data[index], self._data[parent] = self._data[parent], self._data[index]
                self.percolate_up(parent)

    def percolate_down(self, index):
        """
        :param index: index of the Node to move down
        :return:none
        """
        if self.min:
            small_child = self.min_child(index)
            if small_child is None:
                return
            elif self._data[small_child] < self._data[index]:
                self._data[small_child], self._data[index] = self._data[index], self._data[small_child]
                self.percolate_down(small_child)

        else:
            big_child = self.max_child(index)
            if big_child is None:
                return
            elif self._data[big_child] > self._data[index]:
                self._data[big_child], self._data[index] = self._data[index], self._data[big_child]
                self.percolate_down(big_child)

def heap_sort(array):
    """
    :param array: the list to sort
    :return: the sorted list
    """
    if array is None:
        return None
    result = []
    heap = PriorityHeap(False)
    for i in range(len(array)):
        heap.push(array[i], array[i])
    for i in range(len(array)):
        result.append(heap.top())
        heap.pop()
    result.reverse()
    return result

def current_medians(values):
    """
    :param values: the list to find medians
    :return: list with medians
    """
    result = []
    high_heap = PriorityHeap()      # min_heap
    low_heap = PriorityHeap(False)  # max_heap
    for i in range(len(values)):
        if len(high_heap) == 0 and len(low_heap) == 0:
            low_heap.push(values[i], values[i])
        else:
            low_top = low_heap.top()
            if low_top < values[i]:
                high_heap.push(values[i], values[i])
                if len(high_heap) - len(low_heap) >= 2:
                    move_num = high_heap.top()
                    high_heap.pop()
                    low_heap.push(move_num, move_num)
            else:
                low_heap.push(values[i], values[i])
                if len(low_heap) - len(high_heap) >= 2:
                    move_num = low_heap.top()
                    low_heap.pop()
                    high_heap.push(move_num, move_num)
        if (len(low_heap) + len(high_heap)) % 2 == 1:          # odd
            if len(low_heap) > len(high_heap):
                result.append(low_heap.top())
            elif len(high_heap) > len(low_heap):
                result.append(high_heap.top())
        else:
            num1 = low_heap.top()
            num2 = high_heap.top()
            num = (num1 + num2) / 2
            if num == int(num):
                num = int(num)
            result.append(num)

    return result