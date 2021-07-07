import unittest
from PriorityHeap import PriorityHeap, Node, heap_sort, current_medians


class MimirTests(unittest.TestCase):
    
    def test_push(self):
        min_heap = PriorityHeap(False)
        min_heap.push(5, 'c')
        min_heap.push(4, 'y')
        min_heap.push(3, 'n')
        min_heap.push(2, 'd')
        min_heap.push(5, 'y')
        min_heap.push(3, 'o')
        min_heap.pop()
        min_heap.push(2, 'h')
        print(min_heap)
    #     assert len(min_heap._data) == 5
    #     # print(min(min_heap._data[:5]))
    #     # print(min_heap._data[0])
    #     print(min_heap)
    #     assert min(min_heap._data[:5]) == min_heap._data[0]
    #     assert min_heap._data[1] < min_heap._data[3]
    #     assert min_heap._data[1] < min_heap._data[4]
    #     min_heap.push(6, 'y')
    #     assert min_heap._data[2] < min_heap._data[5]
    #
    #     max_heap = PriorityHeap(False)
    #     max_heap.push(5, 'c')
    #     max_heap.push(4, 'y')
    #     max_heap.push(3, 'n')
    #     max_heap.push(2, 'd')
    #     max_heap.push(5, 'y')
    #
    #     assert len(max_heap._data) == 5
    #     # print(max(max_heap._data[:5]))
    #     # print(max_heap._data[0])
    #     assert max(max_heap._data[:5]) == max_heap._data[0]
    #     assert max_heap._data[1] > max_heap._data[3]
    #     assert max_heap._data[1] > max_heap._data[4]
    #     max_heap.push(6, 'y')
    #     assert max_heap._data[2] > max_heap._data[5]
    #
    # def test_pop(self):
    #     # test 1: tests pop returns the root
    #     min_heap = PriorityHeap()
    #     max_heap = PriorityHeap(False)
    #
    #     min_heap.push(5, 'c')
    #     min_heap.push(4, 'y')
    #     min_heap.push(3, 'n')
    #     min_heap.push(2, 'd')
    #     min_heap.push(5, 'y')
    #
    #     max_heap.push(5, 'c')
    #     max_heap.push(4, 'y')
    #     max_heap.push(3, 'n')
    #     max_heap.push(2, 'd')
    #     max_heap.push(5, 'y')
    #
    #     assert min_heap.pop() == Node(2, 'd')
    #     assert max_heap.pop() == Node(5, 'y')
    #
    #     # test 2: checks for length and not empty
    #     min_heap = PriorityHeap()
    #     max_heap = PriorityHeap(False)
    #     min_heap.push(4, 'y')
    #     min_heap.push(3, 'n')
    #     max_heap.push(4, 'y')
    #     max_heap.push(3, 'n')
    #
    #     assert len(min_heap._data) == 2
    #     assert len(max_heap._data) == 2
    #     assert min_heap.pop().value == 'n'
    #     assert max_heap.pop().value == 'y'
    #     assert not min_heap.empty()
    #     assert not max_heap.empty()
    # #
    # def test_min_child(self):
    #     from string import ascii_lowercase
    #     def check_min(pheap, idx, lhs=None, rhs=None):
    #         '''
    #         function helper for validating the min method
    #         '''
    #         min_child = lhs if pheap._data[lhs] < pheap._data[rhs] else rhs
    #         assert min_child == pheap.min_child(idx)
    #
    #     heap = PriorityHeap()
    #     for child in ascii_lowercase:
    #         heap.push(ord(child), child)
    #     assert len(heap._data) == 26
    #
    #     check_min(heap, 0, 1, 2)
    #     check_min(heap, 2, 5, 6)
    #     check_min(heap, 3, 7, 8)
    #
    # def test_max_child(self):
    #     from string import ascii_lowercase
    #     def check_max(pheap, idx, lhs=None, rhs=None):
    #         '''
    #         function helper for validating the max method
    #         '''
    #         max_child = lhs if pheap._data[lhs] > pheap._data[rhs] else rhs
    #         assert max_child == pheap.max_child(idx)
    #
    #     heap = PriorityHeap(False)
    #     for child in ascii_lowercase:
    #         heap.push(ord(child), child)
    #     assert len(heap._data) == 26
    #
    #     check_max(heap, 0, 1, 2)
    #     check_max(heap, 2, 5, 6)
    #     check_max(heap, 3, 7, 8)

    # def test_heap_sort(self):
    #     #     array = [46, 52, 28, 17, 3, 63, 34, 81, 70, 95]  # 46, 52, 28, 17, 3, 63, 34, 81, 70, 95
    #     #     heap = heap_sort(array)
        # print(heap)
        # assert heap == [1, 2, 3, 4, 5]
    #
    # def test_current_medians(self):
    #     data_list = [5, 6, 7, 8, 9, 1, 2, 3]
        # print(current_medians(data_list))
        # assert current_medians(data_list) == [2, 3, 4, 5, 6]


if __name__ == '__main__':
    unittest.main()