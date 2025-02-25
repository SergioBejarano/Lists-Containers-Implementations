import unittest
from algorithms.disjset import DisjSet


class TestDisjSet(unittest.TestCase):
    def test_initial_sets(self):
        ds = DisjSet(5)
        self.assertEqual(ds.getNumberOfSets(), 5)
        for i in range(5):
            self.assertEqual(ds.find(i), i)

    def test_union_find(self):
        ds = DisjSet(5)
        ds.Union(0, 1)
        self.assertEqual(ds.find(0), ds.find(1))
        ds.Union(2, 3)
        ds.Union(3, 4)
        self.assertEqual(ds.find(2), ds.find(4))
        self.assertNotEqual(ds.find(0), ds.find(2))

    def test_all_sets(self):
        ds = DisjSet(4)
        ds.Union(0, 1)
        ds.Union(2, 3)
        sets = ds.getAllSets()
        self.assertEqual(len(sets), 2)
        self.assertIn([0, 1], sets)
        self.assertIn([2, 3], sets)

if __name__ == '__main__':
    unittest.main()
