import unittest
from algorithms.dll import dll, node

class TestDLL(unittest.TestCase):
    def test_insert_head_tail(self):
        linked_list = dll()
        n1, n2, n3 = node(10), node(20), node(30)
        linked_list.insert(n1)
        linked_list.insert_tail(n2)
        linked_list.insert_tail(n3)
        self.assertEqual(linked_list.size(), 3)

    def test_insert_between(self):
        linked_list = dll()
        n1, n2 = node(10), node(20)
        linked_list.insert(n1)
        linked_list.insert_between(n1, n2)
        self.assertEqual(linked_list.size(), 2)

    def test_empty_list(self):
        linked_list = dll()
        self.assertEqual(linked_list.size(), 0)


if __name__ == '__main__':
    unittest.main()
