
class Node:
    """Single node item
    Attributes:
        value (int) - node value, default 0
        left (Node) - left child, default None
        right (Node) - right child, default None
    """

    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    """Class used to aggregate methods for tree, built using Node objects
    Attributes:
        root (Node) - root of tree, default None - empty tree
    Methods:
        sum()
        average()
        median()
    """

    def __init__(self, root=None):
        self.root = root

    def sum(self):
        """Public sum method
        Returns a sum of the entire tree if it isn't empty, otherwise return None.
        """
        if self.root:
            return self._recursive_sum(self.root)
        else:
            return None

    def _recursive_sum(self, node):
        """Return sum from subtree given by node"""
        sum = 0
        if node is None:
            return 0
        sum += node.value
        sum += self._recursive_sum(node.left)
        sum += self._recursive_sum(node.right)
        return sum

    def average(self):
        """Return average of tree if it isn't empty, otherwise return None"""
        if self.root:
            sum = self.sum()
            count = self._size(self.root)
            return sum/count
        else:
            return None

    def _size(self, node):
        """Return size of subtree given by node"""
        count = 0
        if node is None:
            return 0
        count += 1
        count += self._size(node.left)
        count += self._size(node.right)
        return count

    def median(self):
        """Return median of tree if it isn't empty, otherwise return None"""
        if self.root:
            values_list = self._tree_values(self.root)
            values_list.sort()
            list_len = len(values_list)
            if list_len > 0:
                if list_len == 1:
                    return values_list[0]
                elif list_len % 2 == 0:
                    return (values_list[int(list_len/2)-1] + values_list[int(list_len/2)])/2
                else:
                    return values_list[int(list_len/2)]
            else:
                return None
        else:
            return None

    def _tree_values(self, node):
        """Return list of values in tree, inorder tree walk"""
        values = []
        if node is None:
            return values
        values += self._tree_values(node.left)
        values.append(node.value)
        values += self._tree_values(node.right)
        return values
