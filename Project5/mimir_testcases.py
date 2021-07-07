import unittest
from AVLTree import AVLTree, is_avl_tree, TreeNode

class TestProject1(unittest.TestCase):

#     def test_left_and_right_rotate(self):
#
#         avl = AVLTree()
#         avl.root = TreeNode(3)
#         avl.root.left = TreeNode(2, parent=avl.root)
#         avl.root.left.left = TreeNode(1, parent=avl.root.left)
#         avl.size = 3
#
#         avl.right_rotate(avl.root)
#
#         assert avl.root.value == 2  # 1
#         assert avl.root.left.value == 1  # 2
#         assert avl.root.right.value == 3  # 3
#
#         avl = AVLTree()
#         avl.root = TreeNode(1)
#         avl.root.right = TreeNode(2, parent=avl.root)
#         avl.root.right.right = TreeNode(3, parent=avl.root.right)
#         avl.size = 3
#
#         avl.left_rotate(avl.root)
#
#         assert avl.root.value == 2  # 4
#         assert avl.root.left.value == 1  # 5
#         assert avl.root.right.value == 3  # 6
#
#         avl = AVLTree()
#         avl.root = TreeNode(4)
#         avl.root.left = TreeNode(2, parent=avl.root)
#         avl.root.right = TreeNode(6, parent=avl.root)
#         avl.root.right.right = TreeNode(8, parent=avl.root.right)
#         avl.root.right.right.right = TreeNode(10, parent=avl.root.right.right)
#         avl.left_rotate(avl.root.right)
#
#         assert avl.root.value == 4  # 7
#         assert avl.root.left.value == 2  # 8
#         assert avl.root.right.value == 8  # 9
#         assert avl.root.right.left.value == 6  # 10
#         assert avl.root.right.right.value == 10  # 11
# #
#
    def test_insert(self):
        avl = AVLTree()
        avl.insert(avl.root, 42)
        avl.insert(avl.root, 6)
        avl.insert(avl.root, 62)
        avl.insert(avl.root, 42)
        avl.insert(avl.root, 12)
        avl.insert(avl.root, 42)
        # avl.insert(avl.root, 23)
        # avl.insert(avl.root.left, 4)
        print(avl)
#         assert avl.root.value == 5  # 1
#         assert avl.root.left.value == 1  # 2
#         assert avl.root.left.right.value == 3  # 3
#         assert avl.root.right.value == 10  # 4
#         assert avl.root.right.left.value == 7  # 5
# #
#         ### REQUIRES ROTATES ###
#         avl2 = AVLTree()
#         avl2.insert(avl2.root, 3)
#         avl2.insert(avl2.root, 2)
#         avl2.insert(avl2.root, 1)
#         avl2.insert(avl2.root, 4)
#         avl2.insert(avl2.root, 5)
#
#         assert avl2.root.value == 2  # 6
#         assert avl2.root.left.value == 1  # 7
#         assert avl2.root.right.value == 4  # 8
#         assert avl2.root.right.left.value == 3  # 9
#         assert avl2.root.right.right.value == 5  # 10
#
#         avl3 = AVLTree()
#         avl3.insert(avl3.root, 1)
#         avl3.insert(avl3.root, 5)
#         avl3.insert(avl3.root, 2)
#         avl3.insert(avl3.root, 9)
#         avl3.insert(avl3.root, 10)
#         avl3.insert(avl3.root, 20)
#         avl3.insert(avl3.root, 7)
#
#         assert avl3.root.value == 9  # 11
#         assert avl3.root.left.value == 2  # 12
#         assert avl3.root.left.left.value == 1  # 13
#         assert avl3.root.left.right.value == 5  # 14
#         assert avl3.root.left.right.right.value == 7  # 15
#         assert avl3.root.right.value == 10  # 16
#         assert avl3.root.right.right.value == 20  # 17
#
#     def test_remove(self):
#         avl = AVLTree()
#
#         avl.insert(avl.root, 10)
#         avl.insert(avl.root, 5)
#         avl.insert(avl.root, 15)
#         avl.insert(avl.root, 1)
#         avl.insert(avl.root, 7)
#         avl.insert(avl.root, 13)
#         avl.insert(avl.root, 19)
#         print(avl)
#         avl.remove(avl.root, 10)
#         print(avl)
#         avl.remove(avl.root, 7)
#         print(avl)
#         avl.remove(avl.root, 15)
#         print(avl)
#
#         # assert avl.root.left.right == None  # 1
#
#         avl.remove(avl.root, 1)
#
#         # assert avl.root.left.left == None  # 2
#
#         avl.remove(avl.root, 5)
#
#         # assert avl.root.value == 15  # 3
#         # assert avl.root.left.value == 10  # 4
#         # assert avl.root.right.value == 19  # 5
#         # assert avl.root.left.right.value == 13  # 6
#
#     def test_update_height(self):
#
#         """
#                             4 (None 2)
#                   2 (4 1)                 5 (4 1)
#            1 (2 0)     3 (2 0)                 6 (5 0)
#         """
#
#         a = AVLTree()
#         a.root = TreeNode(4)
#         a.root.left = TreeNode(2)
#         a.root.left.left = TreeNode(1)
#         a.root.left.right = TreeNode(2)
#         a.root.right = TreeNode(4)
#         a.root.right.right = TreeNode(6)
#
#         a.update_height(a.root.right.right)  # updating 6 (testing heights of zero)
#         assert a.height(a.root.right.right) == 0  # 1
#
#         a.update_height(a.root.right)  # updating 5 (testing heights of one w one child)
#         assert a.height(a.root.right) == 1  # 2
#
#         a.update_height(a.root.left)  # updating 2 (testing heights of one w two children)
#         assert a.height(a.root.left) == 1  # 3
#
#         a.update_height(a.root)  # updating 2 (testing heights of 2+ w two children)
#         assert a.height(a.root) == 2  # 4
#
#         a.update_height(None)  # should not error
#
#     def test_depth_height(self):
#         avl = AVLTree()
#
#         avl.insert(avl.root, 21)
#         avl.insert(avl.root, 10)
#         avl.insert(avl.root, 32)
#         avl.insert(avl.root, 5)
#         avl.insert(avl.root, 16)
#         avl.insert(avl.root, 27)
#         avl.insert(avl.root, 39)
#
#         assert avl.depth(5) == 2  # 1
#         assert avl.depth(32) == 1  # 2
#         assert avl.depth(100) == -1
#         assert avl.depth(21) == 0
#         assert avl.height(avl.root) == 2  # 3
#         assert avl.height(avl.root.left) == 1  # 4
#
#     def test_search(self):
#         avl = AVLTree()
#
#         avl.insert(avl.root, 30)
#         avl.insert(avl.root, 20)
#         avl.insert(avl.root, 40)
#         avl.insert(avl.root, 10)
#         avl.insert(avl.root, 25)
#         avl.insert(avl.root, 35)
#         avl.insert(avl.root, 50)
#         assert avl.search(avl.root, 10) == avl.root.left.left  # 1
#         assert avl.search(avl.root, 50) == avl.root.right.right  # 2
#         assert avl.search(avl.root, 20) == avl.root.left  # 3
#         assert avl.search(avl.root, 9) == avl.root.left.left
#         assert avl.min(avl.root).value == 10
#         assert avl.max(avl.root).value == 50
# #
#     def test_traversals(self):
#         avl = AVLTree()
#
#         avl.insert(avl.root, 14)
#         avl.insert(avl.root, 7)
#         avl.insert(avl.root, 21)
#         print(avl.root.height)
#         avl.insert(avl.root, 3)
#         avl.insert(avl.root, 10)
#         avl.insert(avl.root, 17)
#         avl.insert(avl.root, 25)
#         print(avl)
#         gen1 = avl.preorder(avl.root)
#         gen2 = avl.postorder(avl.root)
#         gen3 = avl.inorder(avl.root)
#         gen4 = avl.bfs()
#     #
#         pre = [14, 7, 3, 10, 21, 17, 25]
#         post = [3, 10, 7, 17, 25, 21, 14]
#         inorder = sorted(post)
#         bfs = [14, 7, 21, 3, 10, 17, 25]
#     #
#         for i in range(7):
#             assert next(gen1, None).value == pre[i]  # 1
#             assert next(gen2, None).value == post[i]  # 2
#             assert next(gen3, None).value == inorder[i]  # 3
#             assert next(gen4, None).value == bfs[i]  # 4
#     #
#     # def test_min_and_max(self):
#     #     avl = AVLTree()
#     #
#     #     avl.insert(avl.root, 10)
#     #     avl.insert(avl.root, 5)
#     #     avl.insert(avl.root, 15)
#     #     avl.insert(avl.root, 3)
#     #     avl.insert(avl.root, 8)
#     #     avl.insert(avl.root, 12)
#     #     avl.insert(avl.root, 18)
#     #
#     #     assert avl.min(avl.root).value == 3  # 1
#     #     assert avl.max(avl.root).value == 18  # 2
#     #
#     def test_get_balance(self):
#
#         # Node is None
#         a = AVLTree()
#         assert a.get_balance(a.root) == 0  # 1
#
#         """
#                       3
#         """
#         # Balance Factor: 0
#         a.root = TreeNode(3)
#
#         assert a.get_balance(a.root) == 0  # 2
#
#         """
#                       3
#                    /  \
#                   2       4
#         """
#         # Balance Factor: 0
#         a.root.left = TreeNode(2)
#         a.root.right = TreeNode(4)
#
#         assert a.get_balance(a.root) == 0  # 3
#
#         """
#                       3
#                    /  \
#                   2       4
#                  /
#                 1
#         """
#         # Balance Factor: 1
#         a.root.left.left = TreeNode(1)
#         a.root.left.height = 1
#         a.root.right = TreeNode(4)
#
#         assert a.get_balance(a.root) == 1  # 4
#
#         """
#                        3
#                    /
#                   2
#                  /
#                 1
#         """
#         # Balance Factor: 2
#
#         a.root.right = None
#
#         assert a.get_balance(a.root) == 2  # 5
#
#         """
#                        3
#                       \
#                          4
#
#         """
#         # Balance Factor: -1
#         a.root.left = None
#         a.root.right = TreeNode(4)
#
#         assert a.get_balance(a.root) == -1  # 6
#
#         """
#                        3
#                       \
#                           4
#                         \
#                          5
#         """
#         # Balance Factor: -2
#         a.root.right.height = 1
#         a.root.right.right = TreeNode(5)
#
#         assert a.get_balance(a.root) == -2  # 7
#
#     def test_get_balance(self):
#
#         # SET CHILD
#         """
#               1
#
#             - - - - - -
#
#                 1
#                  \
#                         2
#         """
#
#         a = AVLTree()
#         a.root = TreeNode(1)
#         a.set_child(a.root, TreeNode(2), False)
#
#         assert a.root.value == 1  # 1
#         assert a.root.right.value == 2  # 2
#         assert a.root.height == 1  # 3
#
#         # REPLACE CHILD
#         """
#               1
#                \
#                       2
#
#             - - - - - -
#
#                 1
#                  \
#                         3
#         """
#
#         a.root.right = TreeNode(2)
#         a.replace_child(a.root, a.root.right, TreeNode(3))
#
#         assert a.root.value == 1  # 4
#         assert a.root.right.value == 3  # 5
#         assert a.root.height == 1  # 6
#
#     def test_rebalance(self):
#
#         # DOUBLE RIGHT LEFT ROTATE
#         """
#               1
#                \
#                 3
#                /
#               2
#           - - - - - -
#               2
#             /   \
#            1     3
#         """
#
#         a = AVLTree()
#         a.root = TreeNode(1)
#         a.root.right = TreeNode(3)
#         a.root.right.parent = a.root
#         a.root.right.left = TreeNode(2)
#         a.root.right.left.parent = a.root.right
#
#         a.root.height = 2
#         a.root.right.height = 1
#
#         a.rebalance(a.root)
#         # root
#         assert a.root.value == 2  # 1
#         assert a.root.height == 1  # 2
#         assert a.root.parent is None  # 3
#
#         # left
#         assert a.root.left.value == 1  # 4
#         assert a.root.left.height == 0  # 5
#         assert a.root.left.parent.value == 2  # 6
#
#         #right
#         assert a.root.right.value == 3  # 7
#         assert a.root.right.height == 0  # 8
#         assert a.root.right.parent.value == 2  # 9
#
#     #
#     # def test_is_avl_tree(self):
#     #
#     #     a = AVLTree()
#     #     assert is_avl_tree(a.root) is True  # 1
#     #
#     #     a.root = TreeNode(2)
#     #     assert is_avl_tree(a.root) is True  # 2
#     #
#     #     a.root.left = TreeNode(1)
#     #     assert is_avl_tree(a.root) is True  # 3
#     #
#     #     a.root.left.left = TreeNode(0)
#     #
#     #     assert is_avl_tree(a.root) is False  # 4
#     #
#     #     a.root.right = TreeNode(0)
#     #     assert is_avl_tree(a.root) is True  # 5
#     #
#     #
#
if __name__ == "__main__":
    unittest.main()
