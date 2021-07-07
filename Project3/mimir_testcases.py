import unittest
from HybridSort import *


class TestProject3(unittest.TestCase):
    def test_get_pivot(self):
        ex = [13,51,49,35,7,48,55,23,15,3,28,37,32,17]
        pivot = find_pivot(ex,0,len(ex)-1)
        print(pivot)
        assert pivot == 17

    def test_quick_sort(self):
        ex = [13, 51, 49, 35, 7, 48, 42]
        quick_sort(ex,0,0,len(ex)-1)
        print(ex)
        assert ex == [7,13,35,42,48,49,51]
        quick_sort(ex, 0, 0, len(ex) - 1, True)
        print("Reverse: ", ex)
        assert ex == [51,49,48,42,35,13,7]

    def test_insertion_sort(self):
        ex = [13, 51, 49, 35, 7, 48, 42]
        insertion_sort(ex, 0, len(ex) - 1, False)
        print(ex)
        assert ex == [7, 13, 35, 42, 48, 49, 51]
        insertion_sort(ex, 0, len(ex) - 1, True)
        print("Reverse: ",ex)
        assert ex == [51,49,48,42,35,13,7]

    def test_hybrid_sort(self):
        ex = [13, 51, 49, 35, 7, 48, 42]
        quick_sort(ex,4,0,len(ex) - 1)
        print(ex)
        assert ex == [7, 13, 35, 42, 48, 49, 51]
        quick_sort(ex, 2, 0, len(ex) - 1, True)
        print(ex)
        assert ex == [51,49,48,42,35,13,7]

    def test_max_diff(self):
        ex = [13, 51, 49, 35, 7, 48, 42]
        diff = largest_sequential_difference(ex)
        print(diff)
        assert diff == 22


if __name__ == "__main__":
    unittest.main()