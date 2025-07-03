from app.data_structures.array import Array
class maxHeap:
    def __init__(self):
        self.heap = Array()
    

    def left_child(self, i) -> int:
        return 2 * i + 1

    def right_child(self, i) -> int:
        return 2 * i + 2

    def parent(self, i) -> int:
        return (i - 1) // 2

    def heapify(self, arr, heap_size, i) -> None:
        l = self.left_child(i)
        r = self.right_child(i)
        biggest = i

        if l < heap_size:
            if arr[l].score > arr[biggest].score:
                biggest = l
            elif arr[l].score == arr[biggest].score:
                if arr[l].license_date_int > arr[biggest].license_date_int:
                    biggest = l

        if r < heap_size:
            if arr[r].score > arr[biggest].score:
                biggest = r
            elif arr[r].score == arr[biggest].score:
                if arr[r].license_date_int > arr[biggest].license_date_int:
                    biggest = r

        if biggest != i:
            arr[i], arr[biggest] = arr[biggest], arr[i]
            self.heapify(arr, heap_size, biggest)

            

    def build_max_heap(self, arr) -> list:
        n = len(arr)
        for i in range((n // 2) -1, -1, -1):
            self.heapify(arr, n, i)
        return arr
    
    @property
    def heap_sort(self, arr) -> list:
        arr = self.biuld_max_heap(arr)
        n = len(arr)

        for i in range(n-1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            n -= 1
            self.heapify(arr, n, 0)
        return arr
    
    def insert(self, key):
        self.heap.append(key)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def max_heap_maximum(self) -> int:
        if len(self.heap) == 0:
            raise IndexError("Heap UnderFlow")
        return self.heap[0]

    def max_heap_extract_max(self) -> int:
        heap_size = len(self.heap)
        max_value = self.max_heap_maximum()
        self.heap[0] = self.heap[heap_size -1]
        self.heap.delete(heap_size -1)
        self.heapify(self.heap, len(self.heap), 0)
        return max_value

