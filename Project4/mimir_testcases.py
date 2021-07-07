import unittest
from circularqueue import CircularQueue, QStack, digit_swap

class TestProject1(unittest.TestCase):

    def test_accessors(self):
        queue = CircularQueue()

        # manually set queue variables to test accessors
        queue.data = [5, 10, 15, None]
        queue.head = 0
        queue.tail = 3
        queue.size = 3

        assert queue.is_empty() == False
        assert len(queue) == 3
        assert queue.head_element() == 5
        assert queue.tail_element() == 15

    def test_grow(self):
        queue = CircularQueue(5)
        queue.data = [0, 1, 2, 3, 4]
        queue.head = 0
        queue.tail = 5
        queue.size = 5

        queue.grow()
        # print("Queue grow:", queue.data)
        assert queue.data == [0, 1, 2, 3, 4, None, None, None, None, None]
        assert queue.head == 0
        assert queue.tail == 5
        assert queue.size == 5
        assert queue.capacity == 10

    def test_shrink(self):
        queue = CircularQueue(8)
        queue.data = [0, 1, None, None, None, None, None, None]
        queue.size = 2
        queue.head = 0
        queue.tail = 2

        queue.shrink()
        # print("Queue shrink:", queue.data)
        assert queue.data == [0, 1, None, None]
        assert queue.size == 2
        assert queue.capacity == 4
        assert queue.head == 0
        assert queue.tail == 2

    def test_enqueue(self):
        queue = CircularQueue()

        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        # print("Enqueue:", queue.data)
        assert queue.data == [10, 20, 30, None]
        assert queue.size == 3
        assert queue.head == 0
        assert queue.tail == 3
        assert queue.capacity == 4

    def test_dequeue(self):
        queue = CircularQueue(5)

        for i in range(0, 4):
            queue.enqueue(i * 5)

        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        result = queue.dequeue()
        # print("Dequeue:", queue.data)
        # print("Dequeue_result:", result)
        # assert queue.data == [None, 5, 10, 15, 20, None, None, None]
        # assert queue.size == 4
        # assert queue.capacity == 6
        # assert queue.head == 1
        # assert queue.tail == 5

    def test_qstack_top(self):
        stack = QStack()

        #manually enqueue to test top accessor function
        stack.cq.enqueue(10)
        stack.size = 1

        assert stack.top() == 10

    def test_qstack_push(self):
        stack = QStack()
        stack.push(10)

        assert stack.top() == 10
        assert stack.size == 1

        stack.push(20)

        assert stack.top() == 20
        assert stack.size == 2

    def test_qstack_pop(self):
        stack = QStack()

        stack.push(1)
        stack.push(2)
        stack.push(3)
        print(stack)
        assert stack.pop() == 3
        assert stack.top() == 2
        assert stack.size == 2

    # def test_digit_swap(self):
    #     nums = "5656"
    #     replacements = 2
    #     assert digit_swap(nums, replacements) == 4  # example input 1
    #
    #     nums = "56787776646"
    #     replacements = 1
    #     assert digit_swap(nums, replacements) == 5  # example input 2

if __name__ == '__main__':
    unittest.main()