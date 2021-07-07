"""
PROJECT 5 - AVL Trees
Name:
"""
import queue

class TreeNode:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right', 'height'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)


class AVLTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.root is None and other.root is None:
            return True

        if self.size != other.size or self.root != other.root:
            return False  # size & root comp

        return self._is_equal(self.root.left, other.root.left) and self._is_equal(self.root.right, other.root.right)

    def _is_equal(self, root1, root2):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Checks if rootts are both not None then calls _compare, otherwise checks their equality.
        :param root1: root node of first tree
        :param root2: root node of second tree
        :return: True if equal, False if not
        """
        return self._compare(root1, root2) if root1 and root2 else root1 == root2

    def _compare(self, t1, t2):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if not
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        return self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)

    def __str__(self):
        """
        Collects a visual representation of AVL tree
        :return: string of AVL tree
        """
        if not self.root:
            return "Empty AVL Tree..."

        root = self.root
        ans = ""
        bfs_queue = []
        track = {}
        bfs_queue.append((root, 0, root.parent))
        h = AVLTree.height(self.root)

        for i in range(h+1):
            track[i] = []

        while bfs_queue:
            node = bfs_queue.pop(0)
            if node[1] > h:
                break
            track[node[1]].append(node)

            if node[0] is None:
                bfs_queue.append((None, node[1] + 1, None))
                bfs_queue.append((None, node[1] + 1, None))
                continue

            if node[0].left:
                bfs_queue.append((node[0].left, node[1] + 1, node[0]))
            else:
                bfs_queue.append((None,  node[1] + 1, None))

            if node[0].right:
                bfs_queue.append((node[0].right, node[1] + 1, node[0]))
            else:
                bfs_queue.append((None,  node[1] + 1, None))

        spaces = pow(2, h) * 12
        ans += "\n"
        ans += "\t\tVisual Level Order Traversal of AVL Tree - Node (Parent Height)".center(spaces)
        ans += "\n\n"
        for i in range(h+1):
            ans += f"Level {i}: "
            for node in track[i]:
                level = pow(2, i)
                space = int(round(spaces / level))
                if node[0] is None:
                    ans += " " * space
                    continue
                ans += "{} ({} {})".format(node[0], node[2], node[0].height).center(space, " ")
            ans += "\n"
        return ans

    # ------- Implement/Modify the functions below ------- #

    def insert(self, node, value):
        """
        :param node: the root of the [sub]tree
        :param value: the value to insert
        :return:
        """
        new_node = TreeNode(value)
        if node is None:
            self.size += 1
            self.root = new_node
        elif node.value == new_node.value:
            return
        elif node.value > new_node.value:
            if node.left is None:
                self.size += 1
                self.set_child(node, new_node, True)
            else:
                self.insert(node.left, value)

            if node.parent is not None:
                self.rebalance(node.parent)
                self.update_height(node)
        elif node.value < new_node.value:
            if node.right is None:
                self.size += 1
                self.set_child(node, new_node, False)
            else:
                self.insert(node.right, value)

            if node.parent is not None:
                self.rebalance(node.parent)
                self.update_height(node)
        if self.get_balance(node) == -2 or self.get_balance(node) == 2:
            self.rebalance(node)
        self.update_height(node)


    def remove(self, node, value):
        """
        :param node: the root of the [sub]tree
        :param value: the value to remove
        :return:
        """
        if node is None:
            return None

        elif node.value == value:
            self.size -= 1
            if node.left is None and node.right is None:            # leaf
                if node.parent is None:            # if node is the root
                    self.root = None
                elif node.parent.left == node:      # left leaf
                    node.parent.left = None
                else:                               # right leaf
                    node.parent.right = None
                self.rebalance(node.parent)
            elif node.left is not None and node.right is None:      # one child on the left side
                if node.parent is None:             # if node is the root
                    self.root = node.left
                    node.left.parent = None
                else:
                    suc = self.max(node.left)
                    self.replace_child(node.parent, node, suc)
                self.rebalance(node.parent)
            elif node.left is None and node.right is not None:         # one child on the right side
                if node.parent is None:             # if node is the root
                    self.root = node.right
                    node.right.parent = None
                else:
                    suc = self.max(node.right)
                    self.replace_child(node.parent, node, suc)
                self.rebalance(node.parent)
            else:                                                       # two children
                suc = self.max(node.left)
                node.value = suc.value
                self.remove(node.left, suc.value)
                self.rebalance(node.parent)
                self.size += 1

        elif node.value > value:
            self.remove(node.left, value)
        else:
            self.remove(node.right, value)
        if self.get_balance(node) == -2 or self.get_balance(node) == 2:
            self.rebalance(node)
        # self.update_height(node)

    @staticmethod
    def height(node):
        """
        :param node: the node
        :return:
        """
        if node is None:
            return -1
        # left_height = AVLTree.height(node.left)
        # right_height = AVLTree.height(node.right)
        # return max(left_height, right_height) + 1
        return node.height

    @staticmethod
    def update_height(node):
        """
        :param node: the node that needs to update height
        :return:
        """
        if node is None:
            return
        left_height = -1
        if node.left is not None:
            left_height = node.left.height
        right_height = -1
        if node.right is not None:
            right_height = node.right.height
        node.height = max(left_height, right_height) + 1

    def depth(self, value):
        """
        :param value: value to find the depth
        :return: depth of the value
        """
        counter = -1
        cur = self.root
        while cur is not None:
            counter += 1
            if cur.value == value:
                return counter
            elif value < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        return -1

    def search(self, node, value):
        """
        :param node: node to start
        :param value: value to search
        :return: node with the value or potential value
        """
        if node is None:
            return
        elif value == node.value:
            return node
        elif node.left is None and node.right is None:
            return node
        elif value < node.value:
            return self.search(node.left, value)
        else:
            return self.search(node.right, value)

    def inorder(self, node):
        """
        :param node: node to start
        :return: generator object with values in inorder
        """
        if self.root is None:
            yield None

        if node.left is not None:
            yield from self.inorder(node.left)
        yield node
        if node.right is not None:
            yield from self.inorder(node.right)


    def preorder(self, node):
        """
        :param node: node to start
        :return: generator object with values in preorder
        """
        if self.root is None:
            yield None

        yield node
        if node.left is not None:
            yield from self.preorder(node.left)
        if node.right is not None:
            yield from self.preorder(node.right)

    def postorder(self, node):
        """
        :param node: node to start
        :return: generator object with values in postorder
        """
        if self.root is None:
            yield None

        if node.left is not None:
            yield from self.postorder(node.left)
        if node.right is not None:
            yield from self.postorder(node.right)
        yield node

    def bfs(self):
        """
        :return: generator object with values in bfs
        """
        if self.root is None:
            yield None
        else:
            N = queue.Queue(self.size)
            N.put(self.root)
            while N.qsize() > 0:
                node = N.get()
                if node.left is not None:
                    N.put(node.left)
                if node.right is not None:
                    N.put(node.right)
                yield node


    def min(self, node):
        """
        :param node: node to start
        :return: node with minimum value
        """
        if self.root is None:
            return

        if node.left is None:
            return node
        return self.min(node.left)

    def max(self, node):
        """
        :param node: node to start
        :return: node with max value
        """
        if self.root is None:
            return

        if node.right is None:
            return node
        return self.max(node.right)

    def get_size(self):
        """
        :return: number of nodes in the AVLTree
        """
        return self.size

    @staticmethod
    def get_balance(node):
        """
        :param node: node
        :return: balance factor of the node
        """
        if node is None:
            return 0
        left_height = -1
        if node.left is not None:
            left_height = AVLTree.height(node.left)  # node.left.height
        right_height = -1
        if node.right is not None:
            right_height = AVLTree.height(node.right)  # node.right.height
        return left_height - right_height

    @staticmethod
    def set_child(parent, child, is_left):
        """
        :param parent: parent of the child
        :param child: node to insert
        :param is_left: whether node goes to left or not
        :return:
        """
        if is_left is True:
            parent.left = child
        else:
            parent.right = child

        if child is not None:
            child.parent = parent
        AVLTree.update_height(parent)

    @staticmethod
    def replace_child(parent, current_child, new_child):
        """
        :param parent: parent of the child
        :param current_child: current child that is going to get replaced
        :param new_child: new child to replace
        :return:
        """
        if parent.left == current_child:
            AVLTree.set_child(parent, new_child, True)
        elif parent.right == current_child:
            AVLTree.set_child(parent, new_child, False)

    def left_rotate(self, node):
        """
        :param node: node to rotate
        :return: root of the tree
        """
        right_left_child = node.right.left
        if node.parent is not None:
            self.replace_child(node.parent, node, node.right)
        else:
            self.root = node.right
            self.root.parent = None
        self.set_child(node.right, node, True)
        self.set_child(node, right_left_child, False)
        return self.root

    def right_rotate(self, node):
        """
        :param node: node to rotate
        :return: root of the tree
        """
        left_right_child = node.left.right
        if node.parent is not None:
            self.replace_child(node.parent, node, node.left)
        else:
            self.root = node.left
            self.root.parent = None
        self.set_child(node.left, node, False)
        self.set_child(node, left_right_child, True)
        return self.root

    def rebalance(self, node):
        """
        :param node: node to rebalance
        :return: root of the tree
        """
        if self.get_balance(node) == -2:
            if self.get_balance(node.right) == 1:
                self.right_rotate(node.right)
            update = self.left_rotate(node)
            self.update_height(update)
        elif self.get_balance(node) == 2:
            if self.get_balance(node.left) == -1:
                self.left_rotate(node.left)
            update = self.right_rotate(node)
            self.update_height(update)

        if node is None:
            self.update_height(self.root)
        else:
            self.update_height(node.parent)
        return self.root



# ------- Application Problem ------- #
def is_avl_tree(node):
    pass
