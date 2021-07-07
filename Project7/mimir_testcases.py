import unittest
from hashtable import HashTable, HashNode, hurdles


class TestProject1(unittest.TestCase):

    def test_initialization(self):
        table = HashTable(capacity=100)
        assert (table.capacity == 100)
        assert (table.size == 0)
        assert (table.table == [None for _ in range(100)])

    def test_hash(self):
        table = HashTable(capacity=16)

        table.table = [None, None, None,
                       HashNode('class_ever', 1), HashNode(None, None, True),
                       HashNode(None, None, True), None, None, None,
                       None, HashNode(None, None, True), None,
                       None, None, HashNode('cse331', 100), None]

        # Should insert in the first available bin
        # print(table.hash("is_the", inserting=True))
        assert (4 == table.hash("is_the", inserting=True))

        # Should search until the first None/unused bin
        # print(table.hash("is_the"))
        assert (15 == table.hash("is_the"))

        # Should insert in the first available bin
        assert (5 == table.hash("yash", inserting=True))

        # Should search until the first None/unused bin
        assert (7 == table.hash("yash"))

        assert (3 == table.hash("class_ever"))

    def test_setitem(self):
        table = HashTable()

        solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                    None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        table["cse331"] = 100
        table["is_the"] = 3005

        assert (table.size == 2)
        assert (table.capacity == 8)

        table['best'] = 42
        table['class_ever'] = 1

        assert (table.size == 4)
        assert (table.capacity == 16)
        # print(table)
        assert (solution == table.table)

    def test_getitem(self):
        table = HashTable()

        solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                    None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        table["cse331"] = 100
        table["is_the"] = 3005

        assert (table.size == 2)
        assert (table.capacity == 8)

        table['best'] = 42
        table['class_ever'] = 1

        assert (table.size == 4)
        assert (table.capacity == 16)
        # print(table)
        assert (solution == table.table)
        for i in solution:
            if i:
                # print(table[i.key])
                # print(i.value)
                assert (table[i.key] == i.value)

    def test_delitem(self):
        table = HashTable()

        pre_solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                        None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        post_solution = [None, None, None, HashNode('class_ever', 1), HashNode(None, None), None, None, None, None,
                         None,
                         HashNode(None, None), None, None, None, HashNode('cse331', 100), None]

        table["cse331"] = 100
        table["is_the"] = 3005

        assert (table.size == 2)
        assert (table.capacity == 8)

        table['best'] = 42
        table['class_ever'] = 1

        assert (table.size == 4)
        assert (table.capacity == 16)
        # print(table)

        assert (pre_solution == table.table)

        delete = ['best', 'is_the']
        for k in delete:
            del table[k]

        assert (post_solution == table.table)
        # print(table)

    def test_contains(self):
        table = HashTable()
        assert ('key' in table) == False

        table['key'] = 7

        assert ('key' in table) == True
        assert ('new_key' in table) == False

    def test_update(self):
        table = HashTable()

        table["birds"] = 10
        table["real"] = 15

        table.update([("aren't", 20), ("real", 8)])

        assert table["aren't"] == 20
        assert table["real"] == 8

    def test_keys_values_items(self):
        table = HashTable()

        initial_keys = ['one', 'two', 'three', 'four']
        initial_values = [1, 2, 31, 6]
        initial_items = [('one', 1), ('two', 2), ('three', 31), ('four', 6)]

        for i in range(4):
            table[initial_keys[i]] = initial_values[i]

        keys = table.keys()
        values = table.values()
        items = table.items()
        # for i in values:
        #     if i:
        #         print(i)
        #
        kset = set()
        vset = set()
        iset = set()


        for i in range(4):
            kset.add(next(keys, None))
            vset.add(next(values, None))
            iset.add(next(items, None))

        assert set(initial_keys) == kset
        assert set(initial_values) == vset
        assert set(initial_items) == iset

    def test_setdefault(self):
        table = HashTable()

        table.setdefault('hey', 10)

        assert table['hey'] == 10

        table['hey'] = 12

        assert table['hey'] == 12

        table.setdefault('test')
        assert table['test'] is None

    def test_clear(self):
        table = HashTable()

        table['table'] = 1
        table['will'] = 2
        table['be'] = 3
        table['cleared'] = 4

        table.clear()

        assert table.size == 0
        for node in table.table:
            assert node is None

        table.clear()

        assert table.size == 0
        for node in table.table:
            assert node is None

        table['one'] = 1

        table.clear()

        assert table.size == 0
        for node in table.table:
            assert node is None

    def test_hurdles(self):
        # input from picture in specs
        grid = [[1, 2, 2, 1],
                [3, 1, 2],
                [1, 3, 2],
                [2, 4],
                [3, 1, 2],
                [1, 3, 1, 1]]
        # print(hurdles(grid))
        assert hurdles(grid) == 2

        grid = [[5, 2, 2, 1],
                [3, 2, 5],
                [1, 2, 1, 2, 1, 2, 1]]

        assert hurdles(grid) == 1
    #
    # def test_all(self):
    #     table = HashTable()
    #
    #     pre_solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
    #                     None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]
    #
    #     post_solution = [None, None, None, HashNode('class_ever', 1), HashNode(None, None), None, None, None, None,
    #                      None, HashNode(None, None), None, None, None, HashNode('cse331', 100), None]
    #
    #     table['cse331'] = 100
    #     table['is_the'] = 3005
    #
    #     assert (table.size == 2)
    #     assert (table.capacity == 8)
    #
    #     table['best'] = 42
    #     table['class_ever'] = 1
    #
    #     assert (table.size == 4)
    #     assert (table.capacity == 16)
    #     print(table)
    #
    #     assert (pre_solution == table.table)
    #
    #     delete = ['best', 'is_the']
    #     for k in delete:
    #         del table[k]
    #
    #     assert (post_solution == table.table)
    #     print(table)
    #
    #     with self.assertRaises(KeyError):
    #         print(table['best'])


if __name__ == '__main__':
    unittest.main()
