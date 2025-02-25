import unittest
from algorithms.minheap import MinHeap

class TestMinHeap(unittest.TestCase):
    def test_insert_get_min(self):
        heap = MinHeap()
        heap.insert(10)
        heap.insert(5)
        heap.insert(15)
        self.assertEqual(heap.getMin(), 5)

    def test_delete_element(self):
        heap = MinHeap()
        heap.insert(10)
        heap.insert(5)
        heap.insert(20)
        heap.delete(5)
        self.assertEqual(heap.getMin(), 10)

    def test_search(self):
        heap = MinHeap()
        heap.insert(10)
        heap.insert(25)
        self.assertTrue(heap.search(10))
        self.assertFalse(heap.search(5))

    def test_empty_heap(self):
        heap = MinHeap()
        self.assertIsNone(heap.getMin())
        self.assertFalse(heap.search(1))

    def test_min_heapify(self):
        heap = MinHeap()
        heap.a = [10, 20, 15, 30, 40]

        heap.minHeapify(0, len(heap.a))

        self.assertEqual(heap.a, [10, 20, 15, 30, 40])

        heap.a = [40, 10, 30, 50, 20]
        heap.minHeapify(0, len(heap.a))

        self.assertEqual(heap.a, [10, 20, 30, 50, 40])

        heap.a = [50, 40, 30, 20, 10]
        heap.minHeapify(0, len(heap.a))

        self.assertEqual(heap.a, [30, 40, 50, 20, 10])

if __name__ == '__main__':
    unittest.main()
