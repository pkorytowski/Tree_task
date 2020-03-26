import pytest
from tree import Node, Tree


@pytest.fixture
def create_tree():
    eight = Node(8)
    eight.right = Node(5)

    zero = Node(0)
    zero.right = eight
    zero.left = Node(2)

    seven = Node(7)
    seven.right = zero
    seven.left = Node(1)

    three = Node(3)
    three.right = Node(5)
    three.left = Node(2)

    root = Node(5)  # root of tree from the task
    root.right = seven
    root.left = three

    left_tree = Node(1)
    left_tree.left = Node(2)
    left_tree.left.left = Node(3)
    left_tree.left.left.left = Node(4)

    minus_tree = Node(-5)
    minus_tree.left = Node(-15)
    minus_tree.right = Node(-10)
    minus_tree.right.right = Node(0)

    odd_tree = Node(9)
    odd_tree.left = Node(7)
    odd_tree.right = Node(3)
    return [Tree(root), Tree(), Tree(Node(5)), Tree(left_tree), Tree(minus_tree), Tree(odd_tree)]


def test_sum(create_tree):
    assert create_tree[0].sum() == 38, "Test failed"
    assert create_tree[1].sum() is None, "Test failed"
    assert create_tree[2].sum() == 5, "Test failed"
    assert create_tree[3].sum() == 10, "Test failed"
    assert create_tree[4].sum() == -30, "Test failed"
    assert create_tree[5].sum() == 19, "Test failed"


def test_average(create_tree):
    assert create_tree[0].average() == 3.8, "Test failed"
    assert create_tree[1].average() is None, "Test failed"
    assert create_tree[2].average() == 5, "Test failed"
    assert create_tree[3].average() == 2.5, "Test failed"
    assert create_tree[4].average() == -7.5, "Test failed"
    assert create_tree[5].average() == 6.333333333333333, "Test failed"


def test_median(create_tree):
    assert create_tree[0].median() == 4.0, "Test failed"
    assert create_tree[1].median() is None, "Test failed"
    assert create_tree[2].median() == 5, "Test failed"
    assert create_tree[3].median() == 2.5, "Test failed"
    assert create_tree[4].median() == -7.5, "Test failed"
    assert create_tree[5].median() == 7, "Test failed"
