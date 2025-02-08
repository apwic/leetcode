class NumberContainers:
    def __init__(self):
        self.hash_num = defaultdict(list)
        self.hash_idx = defaultdict(int)

    def change(self, index: int, number: int) -> None:
        print("CHANGE", index, number)
        # No number in the index, no need to replace
        if self.hash_idx[index] == 0:
            self.hash_idx[index] = number
            # add to the hash_num too
            heappush(self.hash_num[number], index)
            return

        # Replace the num
        prev = self.hash_idx[index]
        if prev == number:
            return
        self.hash_idx[index] = number

        # Find the corresponding index in hash_num and replace
        heap = self.hash_num[prev]
        indexs = []
        while heap:
            idx = heappop(heap)
            if idx == index:
                break
            indexs.append(idx)

        for idx in indexs:
            heappush(heap, idx)

        # add to the hash_num too
        heappush(self.hash_num[number], index)

    def find(self, number: int) -> int:
        print("FIND", number)
        heap = self.hash_num[number]

        if len(heap) == 0:
            return -1
        
        return heap[0]

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)