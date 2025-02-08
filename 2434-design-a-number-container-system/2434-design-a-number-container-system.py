class NumberContainers:
    def __init__(self):
        self.hash_num = defaultdict(list)
        self.hash_idx = defaultdict(int)

    def change(self, index: int, number: int) -> None:
        self.hash_idx[index] = number
        heappush(self.hash_num[number], index)

    def find(self, number: int) -> int:
        heap = self.hash_num[number]
        if not heap:
            return -1
        
        # Lazy remove, only when the index is found in another number
        while heap:
            idx = heap[0]
            if self.hash_idx[idx] == number:
                return idx

            heappop(heap)

        return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)